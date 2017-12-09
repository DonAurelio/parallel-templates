# Cellular Automata Templates Tool (catt)

In principle, this tool focusses on the programming of **cellular automata models** in C/C++. What is sought is to provide the programmer with a basic template to program cellular automatas that can be easily parallelized with tools such as OpenMP and OpenACC, among others.

<!-- ## Why catt? -->
<!-- Promover las buenas pacticas de programación parallela en principio en modelos de automatas celulares, a pesar de que existe herramientas para simular sistemas dinamicos, los fisicos y muchos investigadores prefieren tener acceso a todo el detalle del sistema modelado, es por ello 
que escogen l camino dificil, la idea de esta herramienta es brindar al cientifico una base en código 
para programar automatas celulares, siendo que esta base permite la facil paralelización dle modelo resultante -->

## Introduction
A **cellular automata** is a numerical method (like finite differences,
finite elements, and the Monte-Carlo method) used to simulate and solve **partial diferential equations** which depicts the behavior of great variety of dynamical systems such as, Traffic Flow, [Gases](https://en.wikipedia.org/wiki/Lattice_gas_automaton), Climate, betwenn other. This method has been very popular in history for the simplicity it provides to model dynamic systems, and also thanks to its nature it is easy to parallelize.


## How does **catt** works?

**catt** consists mainly of 4 files. 

* **C Source Code Template**, a basic C source code with some jinja2 template syntax. This templates should enclose a given parallel programmig pattern.  

* Cafile.yml, a basic YML file which describes information that will be inserted on the **C Source Code Template** to generate a **C Source Code**.

* **C Source Code**, a basic C source code **without** template syntax. 

* **Parallel.yml**, a YML file with a basic syntax to describe how a program should be parallelized.

### C Source Code Template

Altough [jinja2](http://jinja.pocoo.org/) is used mainly to generate HTML code for web applications. We use its syntax to generate C code. in the following, an example of a template is shown.

```c
{% autoescape off %}
#include <stdlib.h>         /* Standard Library: malloc, calloc, free, ralloc */
#include <stdbool.h>        /* Bool type libary */

#define RowDim {{ lattice.rowdim }}
#define ColDim {{ lattice.coldim }}
#define Generations {{ generations }}

#define MOD(a,b) ((((a)%(b))+(b))%(b))

struct Neighborhood
{
    {% for neighbor in lattice.neighborhood.keys %}
    {{ lattice.type }} {{ neighbor }};
    {% endfor %}
};

void initialize({{ lattice.type }} * matrix)
{
    for (int i=0; i<(RowDim*ColDim); ++i)
    {
        matrix[i] = 0;
    }

    /* x = i * coldim + j */
    matrix[10*ColDim+10] = 1;
    matrix[10*ColDim+11] = 1;
    matrix[10*ColDim+12] = 1;
    matrix[11*ColDim+11] = 1;
    // matrix[9*ColDim+11] = 1;
}

{{ lattice.type }} function(struct Neighborhood nbhd)
{
    /* Defined Neighborhood
    {% for key, value in lattice.neighborhood.items %}nbhd.{{ key }} {{ value }}; {% endfor%}    
    */ 

    // int sum = nbhd.c0 + nbhd.c2 + nbhd.c3 + nbhd.c4 + nbhd.c5 + nbhd.c6 + nbhd.c7 + nbhd.c8;
    // int site = nbhd.c1;
    // return ( site == 1 ) ? ( sum == 2 || sum == 3 ) ? 1:0 : ( sum == 3 ) ? 1:0;

    return 0;
}

struct Neighborhood neighborhood(const {{ lattice.type }} * matrix, int i)
{
    struct Neighborhood nbhd;

    int row = i / ColDim;
    int col = MOD(i,ColDim);

    {% for key, value in lattice.neighborhood.items %}
    nbhd.{{ key }} = matrix[ MOD(row + ({{ value.0 }}),RowDim)*ColDim + MOD(col + ({{ value.1 }}),ColDim) ];
    {% endfor%}

    return nbhd;
}

void evolve({{ lattice.type }} * in, {{ lattice.type }} * out)
{
    struct Neighborhood nbhd;
    {{ lattice.type }} * temp = in;

    for (int i = 1; i <= Generations; ++i)
    {
        for (int i = 0; i < (RowDim*ColDim); ++i)
        {
            nbhd = neighborhood(in,i);
            out[i] = function(nbhd);
        }

        temp = in;
        in = out;
        out = temp;
    }
}

int main(int argc, char const **argv)
{

    {{ lattice.type }} * in = ({{ lattice.type }} *) malloc(RowDim*ColDim*sizeof( {{ lattice.type }} ));
    {{ lattice.type }} * out = ({{ lattice.type }} *) malloc(RowDim*ColDim*sizeof( {{ lattice.type }} ));

    initialize(in);
    initialize(out);
    evolve(in,out);

    /* -- Releasing resources -- */
    free(in);
    free(out);

    return EXIT_SUCCESS;
}
{% endautoescape %}

```


### Cafile.yml

The variables that are in a **Template**, must be rendered or replaced according to a *context*. In the catt jargon, we call this *context* a **Cafile**. An example of this file is shown below.


```yml
lattice: 
  rowdim: 20
  coldim: 20
  type: bool
  neighborhood:
    up: [-1,1]
    down: [1,1]
    left: [1,1]
    right: [-1,-1]
generations: 20

```


### C Source Code

A **C Source Code** in the *catt* jargon is the result of render a **C Source Code Template** in a **Cafile** context. Then, the resulting code is depicted below.


```c
#include <stdlib.h>         /* Standard Library: malloc, calloc, free, ralloc */
#include <stdbool.h>        /* Bool type libary */

#define RowDim 1000
#define ColDim 1000
#define Generations 0

#define MOD(a,b) ((((a)%(b))+(b))%(b))

struct Neighborhood
{
    
};

void initialize(int * matrix)
{
    for (int i=0; i<(RowDim*ColDim); ++i)
    {
        matrix[i] = 0;
    }

    /* x = i * coldim + j */
    matrix[10*ColDim+10] = 1;
    matrix[10*ColDim+11] = 1;
    matrix[10*ColDim+12] = 1;
    matrix[11*ColDim+11] = 1;
    // matrix[9*ColDim+11] = 1;
}

int function(struct Neighborhood nbhd)
{
    /* Defined Neighborhood
        
    */ 

    // int sum = nbhd.c0 + nbhd.c2 + nbhd.c3 + nbhd.c4 + nbhd.c5 + nbhd.c6 + nbhd.c7 + nbhd.c8;
    // int site = nbhd.c1;
    // return ( site == 1 ) ? ( sum == 2 || sum == 3 ) ? 1:0 : ( sum == 3 ) ? 1:0;

    return 0;
}

struct Neighborhood neighborhood(const int * matrix, int i)
{
    struct Neighborhood nbhd;

    int row = i / ColDim;
    int col = MOD(i,ColDim);

    

    return nbhd;
}

void evolve(int * in, int * out)
{
    struct Neighborhood nbhd;
    int * temp = in;

    for (int i = 1; i <= Generations; ++i)
    {
        for (int i = 0; i < (RowDim*ColDim); ++i)
        {
            nbhd = neighborhood(in,i);
            out[i] = function(nbhd);
        }

        temp = in;
        in = out;
        out = temp;
    }
}

int main(int argc, char const **argv)
{

    int * in = (int *) malloc(RowDim*ColDim*sizeof( int ));
    int * out = (int *) malloc(RowDim*ColDim*sizeof( int ));

    initialize(in);
    initialize(out);
    evolve(in,out);

    /* -- Releasing resources -- */
    free(in);
    free(out);

    return EXIT_SUCCESS;
}

{% endautoescape %}

```

### Parallel.yml

It is a complementary file witch gives a basic description a **C Source Code Template**. for example the **name** key tell us which parallel programming pattern we code in a given **C Source Code Template**. The **description** key depics more information about it. Now the most interesting part of this file and of course a proposal to describe how a given C code should be parallelized using **compiler directives**. 

This file proposes to separate the semantic of paralelization from the semantic of the sequential code, mainly to those users who are not familiar with parallel programming, but look for its applications to be easily parallelizable in a near future.

In addition, this file is intended to be a standard applied to sequential code analyzers in search of parallelism. So that in this way, they generate a file like the **Parallel.yml** describing the parallelism found in a given sequential code. In the same way this file can be taken by a code annotator to write it with the corresponding directives indicated by the analyzer. This will finally allow to divide the compilation process into two parts: code analysis and annotation, in **automatic parallelizer compilers**.


```yml
name: 'stencil'
description: |
    Linealized matrix template with stencil parallel programming pattern.
    support OpenMP loop coarse grain parallelization and OpenACC fine
    grain parallelization. 
functs:
    all: # Defines the functions available in the template
        - main
        - initialize
        - function
        - neighborhood
        - evolve
    editable: # Defines just the functions that can be modified by the user
        - initialize
        - function
    parallel: # Defines just the functions that are paralleizable and hoy to parallelize them
        evolve:
            openmp:
                - loop_nro: 0
                  private:
                    - i
                    - j  
                - loop_nro: 1
                  shared: # First loop from the code
                    - in
                    - out
                  default: none
```

# API 

This tool has an API to interact with the templates available in the application, at the moment it only has the template of the stencil parallel programming pattern. However, you can contribute to the growth of these. the Api was made with [Flask Restplus](https://flask-restplus.readthedocs.io/en/stable/). To run a API install requirements and run the application as follows:

```bash
pip3 install -r ./api/requirements.txt
python3 api/app.py
```

The application expose the following endpoints to interact with.

| HTTP Method | URI | Action |
|---|---|---|
| GET | http://[hostname]/templates | Retrieve list of templates |
| GET | http://[hostname]/templates/[template_name] | Retrieve a template detail |
| POST | http://[hostname]/templates/[template_name] | Render a template |


# References

[Structured Parallel Programming: Patterns for Efficient Computation](https://www.amazon.com/Structured-Parallel-Programming-Efficient-Computation/dp/0124159931)

[Designing a RESTful API using Flask-RESTful](https://blog.miguelgrinberg.com/post/designing-a-restful-api-using-flask-restful)

[Flask-RESTful](http://flask-restful.readthedocs.io/en/latest/)

[Designing a RESTful API with Python and Flask](https://blog.miguelgrinberg.com/post/designing-a-restful-api-with-python-and-flask)

[AJAX with jQuery](http://flask.pocoo.org/docs/0.12/patterns/jquery/)

[Flask Examples Github](https://github.com/pallets/flask/tree/master/examples/jqueryexample)