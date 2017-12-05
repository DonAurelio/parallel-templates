# Cellular Automata Templates Tool (catt)

In principle, this tool focusses on the programming of **cellular automata models** in C/C++. What is sought is to provide the programmer with a basic template to program cellular automatas that can be easily parallelized with tools such as OpenMP and OpenACC, among others.

## Why catt?

## Introduction
A **cellular automata** is a numerical method (like finite differences,
finite elements, and the Monte-Carlo method) used to simulate and solve **partial diferential equations** which depicts the behavior of great variety of dynamical systems such as, Traffic Flow, [Gases](https://en.wikipedia.org/wiki/Lattice_gas_automaton), Climate, betwenn other. This method has been very popular in history for the simplicity it provides to model dynamic systems, and also thanks to its nature it is easy to parallelize.

<!-- Promover las buenas pacticas de programación parallela en principio en modelos de automatas celulares, a pesar de que existe herramientas para simular sistemas dinamicos, los fisicos y muchos investigadores prefieren tener acceso a todo el detalle del sistema modelado, es por ello 
que escogen l camino dificil, la idea de esta herramienta es brindar al cientifico una base en código 
para programar automatas celulares, siendo que esta base permite la facil paralelización dle modelo resultante -->

## How does **catt** works?

**catt** consists mainly of 4 files. 

* **C Source Code Template**, a basic C source code with some jinja2 template syntax. This templates should enclose a given parallel programmig pattern.  

* Cafile.yml, a basic YML file which describes information that will be inserted on the **C Source Code Template** to generate a **C Source Code**.

* **C Source Code**, a basic C source code **without** template syntax. 

* **Parallel.yml**, a YML file with a basic syntax to describe how a program should be parallelized.

### C99 Source Code Template

Altough [jinja2](http://jinja.pocoo.org/) is used mainly to generate HTML code for web applications. We use its syntax to generate C code. 

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


Cafile.yml

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

C99 Source Code

```c


```

Parallel.yml
 
<!-- ha sido usados como vehiculos para modelar sistemas dinamicos y complejos y tambien para resolver ecuaciones diferenciales parciales.
La problematica que se presenta con los automatas celulares es que son programador de muchas maneras distintas por varios programadores, por lo tanto su paralelización se hace en algunos casos muy sencilla 
y en otros muy complicada. esta plantilla retende dar al programdor un codigo base para programar automatas celulares que garantiza que el sistemas va a poder ser paralelizado facilmente. -->