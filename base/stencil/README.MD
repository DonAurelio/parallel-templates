# Stencil Parallel Programming Pattern

*It is a generalization of the **map** pattern, in which a **elementary function** not only has access to a single element of a collection of input data, but can also access a set of neighbors. Like the map, there is an **elementary function** that must be applied to each element of a data collection, but in this case, the elementary function takes as input the **neighborhood** corresponding to each element of the collection. In other words, the new value for each element of the collection must strictly depend on its neighbors. In general, in this pattern the data collection takes the form of a matrix. For this pattern it is necessary to establish **boundary conditions**, since in the borders or border of the matrix the indexing of the neighbors for each element in the border changes. In these cases you can choose one of the following alternatives, modify the indexing for out-of-bounds accesses or executing versions of special cases of the elementary function. This pattern is commonly used not only to study dynamical and complex systems but also it is used as a partial differential equations solver.* This template is based in the [Game of Life Cellular Automata](https://en.wikipedia.org/wiki/Conway%27s_Game_of_Life).

The folders, **model 1** and **model 2**, were the tests used to select the model that would best behave in terms of execution time. the template.c file is based in the mode on the folder **model 2/acc_1**.


## Refrences 

[structured parallel programming patterns for efficient computation](https://www.amazon.com/Structured-Parallel-Programming-Efficient-Computation/dp/0124159931)