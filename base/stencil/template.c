#include <stdio.h>  /* Standard I/O Library: printf */
#include <stdlib.h> /* Standard Library: malloc, calloc, free, ralloc */

#define MOD(a,b) ((((a)%(b))+(b))%(b))

#define Generations {{ generations }}
#define RowDim {{ lattice.rowdim }}
#define ColDim {{ lattice.coldim }}

struct Neighborhood
{
    {% for neighbor in lattice.neighborhood.keys %}
    {{ lattice.type }} {{ neighbor }};
    {% endfor %}

};

void initialize({{ lattice.type }} ** matrix){

}

struct Neighborhood neighborhood({{ lattice.type }} ** matrix, int row, int col){
    struct Neighborhood nbhd;

    {% for key, value in lattice.neighborhood.items %}
    nbhd.{{ key }} = matrix[ MOD(row + {{ value.0 }},RowDim) ][ MOD(col + {{ value.1 }},CowDim) ];
    {% endfor%}

    return nbhd;
}

{{ lattice.type }} function(struct Neighborhood nbhd){
    
    int sum = nbhd.left_up + nbhd.up + nbhd.right_up + nbhd.left + nbhd.right + nbhd.left_down + nbhd.down + nbhd.right_down;
    int site = nbhd.center;
    int life = ( site == 1 ) ? ( sum == 2 || sum == 3 ) ? 1:0 : ( sum == 3 ) ? 1:0;

    return life;
}

void see({{ lattice.type }} ** matrix){
    printf("\n");
    int i = 0;
    for (i=0; i<RowDim; ++i){
        int j = 0;
        for (j=0; j<ColDim; ++j){
            if(matrix[i][j] == 0)
                printf(" \t");
            else
                printf("%d\t",matrix[i][j]);
        } 
        printf("\n");
    }
    printf("\n");
}

void save({{ lattice.type }} ** matrix, const char * name){
    FILE * pf = fopen(name,"w");
    for (int i=0; i<RowDim; ++i){
        for (int j=0; j<ColDim; ++j) fprintf(pf, "%d\t", matrix[i][j]);
        fprintf(pf, "\n");
    }
    fclose(pf);
}

void evolve({{ lattice.type }} ** in){

    {{ lattice.type }} ** out = ({{ lattice.type }} **) malloc(RowDim*sizeof( {{ lattice.type }} *));

    for (int i=0; i<RowDim; ++i){ 
        out[i] = ({{ lattice.type }} *) malloc(ColDim*sizeof({{ lattice.type }}));
    }

    #pragma acc data copy(in[0:RowDim][0:ColDim]), create(out[0:RowDim][0:ColDim]) 
    {

        for (int g = 1; g <= Generations; ++g){

            #pragma acc parallel loop vector_length(ColDim) num_gangs(RowDim) gang 
            for (int i = 0; i < RowDim; ++i){
                #pragma acc loop vector
                for (int j = 0; j < ColDim; ++j){
                    struct Neighborhood nbhd = neighborhood(in,i,j);
                    out[i][j] = function(nbhd);
                }
            }

            #pragma acc parallel loop 
            for (int i = 0; i < RowDim; ++i){
                #pragma acc loop
                for (int j = 0; j < ColDim; ++j){
                    in[i][j] = out[i][j];
                }
            }
        }

    }

    for (int i=0; i<RowDim; ++i) free(out[i]);
    free(out);
}

void check({{ lattice.type }} ** in){
   

}

int main(int argc, char const **argv)
{

    /* -- Initialization -- */
    {{ lattice.type }} ** in = ({{ lattice.type }} **) malloc(RowDim*sizeof( {{ lattice.type }} *));

    for (int i=0; i<RowDim; ++i){ 
        in[i] = ({{ lattice.type }} *) malloc(ColDim*sizeof({{ lattice.type }}));
    }

    initialize(in);
    evolve(in);
    check(in);

    /* -- Releasing resources -- */
    for (int i=0; i<RowDim; ++i) free(in[i]);
    free(in);

    return EXIT_SUCCESS;
}
