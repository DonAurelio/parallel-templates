# C99 Cellular Automata Templates

The purpose of this folder is to contain some C99 code that can serve to other people as a template to perform experiments regarding to Cellular Automata Experimentation.

On this directory will reside a set of C99 Cellular Automata templates (each forlder is a template name). Each folder should contains:

* **A template.c**, this file use C99 code and Django Templates Langauge to create a C99 source code template that can be rendered with the template.py class.

* **A parallel.yml** (optional), it is a metadata file or format created to give information to another tool about how the rendered *template.c* can be parallelized. **Note: This metadata file can be created by the user by hand or by another tool given an analysis over the Syntax Asbtract Tree of the Code.**

For example the template folder *stencil* has a Cellaular Automata Template code with the Stecil Parallel Programming Pattern, so problems that follow stencil pattern can be take advantage of this template.

Additioanlly, this directory contains an example of a **cafile.yml**, every template should be rendered given the metadata resideing on this file.

