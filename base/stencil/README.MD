# Stencil Parallel Programming Pattern

It is a generalization of the **map** pattern, in which a **elementary function** not only has access to a single element of a collection of input data, but can also access a set of neighbors. Like the map, there is an **elementary function** that must be applied to each element of a data collection, but in this case, the elementary function takes as input the **neighborhood** corresponding to each element of the collection. In other words, the new value for each element of the collection must strictly depend on its neighbors. In general, in this pattern the data collection takes the form of a matrix. For this pattern it is necessary to establish **boundary conditions**, since in the borders or border of the matrix the indexing of the neighbors for each element in the border changes. In these cases you can choose one of the following alternatives, modify the indexing for out-of-bounds accesses or executing versions of special cases of the elementary function.

This pattern is commonly used not only to study dynamical and complex systems but also it is used as a partial differential equations solver.

The follwing is a description of the models taken into consideration to construct the function that will allow the parallelization of the **elemental function**, with the objective of choosing the function that presents the best performance and also from this, a template can be created. 


## Model 1

* Can be executed sequentialy
* Can be executed in paralle with OpenMP with goog improvemts
* The paralleization with OpenACC present some issues given the pointer swaping.

```c
void evolve(bool ** in, bool ** out){

    for (int g = 1; g <= Generations; ++g){
        #pragma omp parallel for num_threads(4)
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
```

## Model 2

* Can be executed sequentialy
* Can be executed in paralle with OpenMP with goog improvemts
* The paralleization with OpenACC present some issues by the pointer swaping.

```c
void evolve(bool ** in,bool ** out){

    for (int g = 1; g <= Generations; ++g){
        #pragma omp parallel for num_threads(4)
        for (int i = 0; i < RowDim; ++i){
            for (int j = 0; j < ColDim; ++j){
                struct Neighborhood nbhd = neighborhood(in,i,j);
                out[i][j] = function(nbhd);
            }
        }

        #pragma omp parallel for num_threads(4)
        for (int i = 0; i < RowDim; ++i){
            for (int j = 0; j < ColDim; ++j){
                in[i][j] = out[i][j];
            }
        }
    }
}
```

### OpenACC Implementation 1

```c
void evolve(bool ** in){

    bool ** out = (bool **) malloc(RowDim*sizeof( bool *));

    for (int i=0; i<RowDim; ++i){ 
        out[i] = (bool *) malloc(ColDim*sizeof(bool));
    }

    #pragma acc data copy(in[0:RowDim][0:ColDim]), create(out[0:RowDim][0:ColDim]) 
    {

        for (int g = 1; g <= Generations; ++g){

            #pragma acc parallel loop gang
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
```

### OpenACC Implementation 2

```c
void evolve(bool ** in){

    bool ** out = (bool **) malloc(RowDim*sizeof( bool *));

    for (int i=0; i<RowDim; ++i){ 
        out[i] = (bool *) malloc(ColDim*sizeof(bool));
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
```