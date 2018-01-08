# Parallel Templates Folder

The purpose of this folder is to contain some C99 parallel programming patterns templates that can serve to other people to construct easy to parallelize source code.

Each template must constain:

* `template.c`, a C99 source code with jinja2 template syntax which allows the user to modify the template easily for different problems that follows the same parallel programming pattern.

* `context.yml`, a file that can be modified by the user to make the template.c match the requirements of an specific problem.

* `parallel.yml`, file a file that is made by the template designer, on this file may reside the information about how `template.c` file could be parallelized. In general this file is related with [#pragcc](https://github.com/DonAurelio/pragcc) tool.

* `Makefile`, it will contain the neccesary rules to compile and run the code, sequential and parallel.

