#include <stdio.h>  /* Standard I/O Library: printf */
#include <stdlib.h> /* Standard Library: malloc, calloc, free, ralloc */
#include <stdbool.h>

#define MOD(a,b) ((((a)%(b))+(b))%(b))

#ifndef Generations
#define Generations 1
#endif

#ifndef N
#define N 20
#endif

#define RowDim N
#define ColDim N


struct Neighborhood
{
    bool up;
    bool center;
    bool down;
    bool left;
    bool left_up;
    bool left_down;
    bool right;
    bool right_up;
    bool right_down;

};

void initialize(bool ** matrix){
    for (int i=0; i<RowDim; ++i){
        for (int j=0; j<ColDim; ++j) matrix[i][j] = 0;
    }
    matrix[10][10] = 1;
    matrix[10][11] = 1;
    matrix[11][11] = 1;
    matrix[10][12] = 1;
}


struct Neighborhood neighborhood(bool ** matrix, int row, int col){
    struct Neighborhood nbhd;

    nbhd.up = matrix[ MOD(row - 1,RowDim) ][ col ];
    nbhd.down = matrix[ MOD(row + 1,RowDim) ][ col ];
    nbhd.center = matrix[row][col];
    
    nbhd.left = matrix[ row ][ MOD(col - 1,ColDim) ];
    nbhd.left_up = matrix[ MOD(row - 1,RowDim) ][ MOD(col - 1,ColDim) ];
    nbhd.left_down = matrix[ MOD(row + 1,RowDim) ][ MOD(col - 1,ColDim) ];
    
    nbhd.right = matrix[ row ][ MOD(col + 1,ColDim) ];
    nbhd.right_up = matrix[ MOD(row - 1,RowDim) ][ MOD(col + 1,ColDim) ];
    nbhd.right_down = matrix[ MOD(row + 1,RowDim) ][ MOD(col + 1,ColDim) ];

    // printf("Neighborhood of %d,%d\n", row, col);
    // printf("%d\t%d\t%d\n%d\t%d\t%d\n%d\t%d\t%d\n",
    //     nbhd.left_up,nbhd.up,nbhd.right_up,
    //     nbhd.left,nbhd.center,nbhd.right,
    //     nbhd.left_down,nbhd.down,nbhd.right_down);

    return nbhd;
}


bool function(struct Neighborhood nbhd){
    
    int sum = nbhd.left_up + nbhd.up + nbhd.right_up + nbhd.left + nbhd.right + nbhd.left_down + nbhd.down + nbhd.right_down;
    int site = nbhd.center;
    int life = ( site == 1 ) ? ( sum == 2 || sum == 3 ) ? 1:0 : ( sum == 3 ) ? 1:0;

    return life;
}

void see(bool ** matrix){
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

void save(bool ** matrix, const char * name){
    FILE * pf = fopen(name,"w");
    for (int i=0; i<RowDim; ++i){
        for (int j=0; j<ColDim; ++j) fprintf(pf, "%d\t", matrix[i][j]);
        fprintf(pf, "\n");
    }
    fclose(pf);
}

void evolve(bool ** in, bool ** out){

    for (int i = 1; i <= Generations; ++i){
        for (int i = 0; i < RowDim; ++i){
            for (int j = 0; j < ColDim; ++j){
                struct Neighborhood nbhd = neighborhood(in,i,j);
                out[i][j] = function(nbhd);
            }
        }

        bool ** temp = in;
        in = out;
        out = temp;

    }
}

void check(bool ** in){
    bool a = (in[6][11] == 1);
    bool b = (in[7][11] == 1);
    bool c = (in[8][11] == 1);
    bool d = (in[12][11] == 1);
    bool e = (in[13][11] == 1);
    bool f = (in[14][11] == 1);

    bool g = (in[10][7] == 1);
    bool h = (in[10][8] == 1);
    bool i = (in[10][9] == 1);
    bool j = (in[10][13] == 1);
    bool k = (in[10][14] == 1);
    bool l = (in[10][15] == 1);

    bool result = a && b && c && d && e && f && g && h && i && j && k && l;

    printf("%d \t\t %d \t\t %s \t\t ", RowDim , ColDim, (result==1) ? "Ok": "Fail");
    

}

int main(int argc, char const **argv)
{

    /* -- Celular space initialization -- */

    bool ** in = (bool **) malloc(RowDim*sizeof( bool *));
    bool ** out = (bool **) malloc(RowDim*sizeof( bool *));

    for (int i=0; i<RowDim; ++i){ 
        in[i] = (bool *) malloc(ColDim*sizeof(bool));
        out[i] = (bool *) malloc(ColDim*sizeof(bool));
    }

    char file_name[100];
    
    initialize(in);
    initialize(out);
    evolve(in,out);
    check(in);

    /* -- Releasing resources -- */
    for (int i=0; i<RowDim; ++i) free(in[i]);
    free(in);
    for (int i=0; i<RowDim; ++i) free(out[i]);
    free(out);

    return EXIT_SUCCESS;
}
