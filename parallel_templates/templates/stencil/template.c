{% autoescape off %}
#include <stdio.h>  /* Standard I/O Library: printf */
#include <stdlib.h> /* Standard Library: malloc, calloc, free, ralloc */


/**
 * Used in the 'neighborhood' function.
 */
#define MOD(a,b) ((((a)%(b))+(b))%(b))

#ifndef Generations
#define Generations {{ generations }}
#endif

#ifndef RowDim
#define RowDim {{ lattice.rowdim }}
#endif

#ifndef ColDim
#define ColDim {{ lattice.coldim }}
#endif


/**
 * Represents the neighborhood of a given cell.
 */
struct Neighborhood
{
    {% for neighbor in lattice.neighborhood.keys() %}
    {{ lattice.type }} {{ neighbor }};
    {% endfor %}

};


/**
 * Used for cellular space initialization.
 */
void initialize({{ lattice.type }} ** matrix){
    // place cellular space initialization code here ...
}


/**
 * Returns the neighborhood of a given cell in the cellular space.
 * A periodic boundary condition is considered. If another type
 * of neighborhood is required, you must modify this function.
 */
struct Neighborhood neighborhood({{ lattice.type }} ** matrix, int row, int col){
    struct Neighborhood nbhd;

    {% for key, value in lattice.neighborhood.items() %}
    nbhd.{{ key }} = matrix[ MOD(row + {{ value.0 }},RowDim) ][ MOD(col + {{ value.1 }},ColDim) ];
    {% endfor%}

    return nbhd;
}


/**
 * Elemental function.
 * Returns the new state of a cell given its neighborhood.
 * This function is applied to each element in the celular space.
 */
{{ lattice.type }} function(struct Neighborhood nbhd){
    
    // place the code here ...

    // you need to return the new state
    // return 0;
}



/**
 * It is responsible for the evolution of the system.
 * Note: This function should not be modified.
 */
void evolve({{ lattice.type }} ** in){

    {{ lattice.type }} ** out = ({{ lattice.type }} **) malloc(RowDim*sizeof( {{ lattice.type }} *));

    /* checking if there is enough memory space to create the celular space */
    if( out == NULL ){
        perror("Not Enough Memory\n");
        exit(-1);
    }

    for (int i=0; i<RowDim; ++i){ 
        out[i] = ({{ lattice.type }} *) malloc(ColDim*sizeof({{ lattice.type }}));
    }

    /* cellular space processing */
    for (int g = 1; g <= Generations; ++g){
     
        for (int i = 0; i < RowDim; ++i){
            for (int j = 0; j < ColDim; ++j){
                struct Neighborhood nbhd = neighborhood(in,i,j);
                out[i][j] = function(nbhd);
            }
        }

        for (int i = 0; i < RowDim; ++i){
            for (int j = 0; j < ColDim; ++j){
                in[i][j] = out[i][j];
            }
        }
    }


    for (int i=0; i<RowDim; ++i) free(out[i]);
    free(out);
}


/**
 * Main function.
 * Note: This function should not be modified.
 */
int main(int argc, char const **argv)
{

    /* allocate memory for the celular space */
    {{ lattice.type }} ** in = ({{ lattice.type }} **) malloc(RowDim*sizeof( {{ lattice.type }} *));

    /* checking if there is enough memory space to create the celular space */
    if( in == NULL ){
        perror("Not Enough Memory\n");
        exit(-1);
    }

    for (int i=0; i<RowDim; ++i){ 
        in[i] = ({{ lattice.type }} *) malloc(ColDim*sizeof({{ lattice.type }}));
    }

    initialize(in);
    evolve(in);

    /* releasing resources */
    for (int i=0; i<RowDim; ++i) free(in[i]);
    free(in);

    return EXIT_SUCCESS;
}

{% endautoescape %}
