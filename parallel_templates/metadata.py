# -*- encoding: utf-8 -*-
"""Define a class for each file in a template directory.

Each template folder contains 4 files:

* template.c
* context.yml
* parallel.yml
* Makefile

So each defined file contains a class on this metadata module to
be accesible for the application. 

"""

import os
import yaml
import shutil
import jinja2


class SourceCode(object):
        
    def __init__(self,name,ftype,text):
        """Contains information about a given c99 source code."""

        self._name = name
        self._ftype = ftype
        self._text = text

    @property
    def file_name(self):
        """str: Source code file name."""
        return self._name

    @property
    def file_type(self):
        """str: Source code file type."""
        return self._ftype

    @property
    def file_text(self):
        """str: Source code file content"""
        return self._text


class Template(object):

    def __init__(self,template_string,pattern_name='unnamed',origin='unknown'):
        """A C99 Source Code Template.

        A *C99 Source Code template* is a C99 source file with some 
        template syntax as depicted in the ``Example``. The C99
        template follows a given parallel programming pattern. This 
        style of programming enable the easy parallelization of source 
        code.

        Example:

            #ifndef Generations
            #define Generations {{ generations }}
            #endif

            #ifndef RowDim
            #define RowDim {{ lattice.rowdim }}
            #endif

            #ifndef ColDim
            #define ColDim {{ lattice.coldim }}
            #endif


            struct Neighborhood
            {
                {% for neighbor in lattice.neighborhood.keys() %}
                {{ lattice.type }} {{ neighbor }};
                {% endfor %}

            };
            ...

        """

        #: str: The raw C99 source code with template syntax
        self.source = template_string

        #: str: The parallel programming pattern name
        self.pattern_name = pattern_name

        #: str: Path to the file
        self.origin = origin

    @property
    def file_name(self):
        """str: template.c."""
        return 'template.c'

    @property
    def file_type(self):
        """str: template."""
        return 'template'

    def render(self,context):
        """Returns a source code given a context instance."""
        template = jinja2.Template(self.source)
        source = template.render(dict(context.data))

        file_name = self.pattern_name + '.c'
        file_type = 'c99'
        file_text = source

        source_code_file = SourceCode(
            file_name,
            file_type,
            file_text 
        )

        return source_code_file


class Parallel(object):

    def __init__(self,parallel_string):
        """Contains parallelization metadata in YML format.

        A paralelization metadata file contains information
        about how a given c99 source code can be parallelized
        or annotated with compiler directives (example: OpenMP
        and OpenACC).

        Example:
            A parallel.yml for the following code

            #include <stdlib.h>
            #include <stdio.h>

            #define N 10

            void some_function(){

                int A[N];
                int B[N];
                int C[N];

                for(int i=0; i<N; ++i){
                    C[i] = A[i] + B[i];
                }
            }

            int main(){
                some_function();
            }

            may look as follows:

            version: 1.0
            name: 'c99 source code file name'
            description: ...
            functs:
                all.
                    - main
                    - some_function
                parallel:
                    some_function:
                        omp:
                            parallel_for:
                                scope: 0
                                clauses:
                                    shared: [A,B]
                        acc:
                            data:
                                scope: 0
                                clauses:
                                    copy: [A,B]

        """

        #: dict: The parallelization metadata as dict.
        self.data = yaml.load(parallel_string)
        #: string: Parallelization metadata as string.
        self.source = parallel_string

    @property
    def file_name(self):
        """str: the string parallel.yml."""
        return 'parallel.yml'

    @property
    def file_type(self):
        """str: the string 'yml'."""
        return 'yml'


    def description(self):
        """Returns description field data from parallel file."""
        data = {
            'name': self.data.get('name',''),
            'description': self.data.get('description','')
        }
        return data


class Context(object):
    """Contains metadata which is placed in a given template.

    A Context file is a YML formtted file which describes information
    that will be rendered in a give template.

    Example:
        For the following *stencil* parallel programming pattern
        template.

        #ifndef Generations
        #define Generations {{ generations }}
        #endif

        #ifndef RowDim
        #define RowDim {{ lattice.rowdim }}
        #endif

        #ifndef ColDim
        #define ColDim {{ lattice.coldim }}
        #endif


        struct Neighborhood
        {
            {% for neighbor in lattice.neighborhood.keys() %}
            {{ lattice.type }} {{ neighbor }};
            {% endfor %}

        };

        ....

        the context file may look as follows:

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

    """

    def __init__(self,context_string):

        #: dict: The Cafile containing data.
        self.data = yaml.load(context_string)
        #: string: The raw cafile data in yaml format.
        self.source = context_string

    @property
    def file_name(self):
        """str: the string 'context.yml'."""
        return 'context.yml'

    @property
    def file_type(self):
        """str: the string 'yml'."""
        return 'yml'


class Makefile(object):

    def __init__(self,file_string):
        """Contains rules defined to compile and run a C source code."""

        #: string: The Makefile content.
        self.source = file_string

    @property
    def file_name(self):
        """str: the string 'Makefile'."""
        return 'Makefile'

    @property
    def file_type(self):
        """str: the string 'plain/text'."""
        return 'plain/text'
