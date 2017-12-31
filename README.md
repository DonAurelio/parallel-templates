# Parallel Templates

It is a set of templates of parallel programming patterns in C (for High Performance Compiting). For example: **stencil** to programing differential equation solvers and cellular automatas; **map** to replicate an operation or function over a collection, bettwen other parallel programing patterns. 

Each template consists of 3 files: **template.c**, **parallel.yml** and **context.yml**

```bash
parallel-templates
│
└───templates
        ├── stencil
        │   ├── template.c
        │   ├── parallel.yml
        │   └── context.yml    
        └── map
            ├── template.c
            ├── parallel.yml
            └── context.yml
```

###### template.c
it is a normal code in C, but with some [jinja2](http://jinja.pocoo.org/) template syntax to add more flexibility to the template user. This template must have a parallel programming pattern implicit. Additionally it must also be easily reusable.

###### parallel.yml

It is a metadata file in YAML format which in addition to having information of the template. It contains details of how it should be parallelized. That is, what OpenMP and OpenACC compile directives should go in each function and what loop lexicographically.
<!-- 
It is a complementary file witch gives a basic description a **C Source Code Template**. for example the **name** key tell us which parallel programming pattern we code in a given **C Source Code Template**. The **description** key depics more information about it. Now the most interesting part of this file and of course a proposal to describe how a given C code should be parallelized using **compiler directives**. 

This file proposes to separate the semantic of paralelization from the semantic of the sequential code, mainly to those users who are not familiar with parallel programming, but look for its applications to be easily parallelizable in a near future.

In addition, this file is intended to be a standard applied to sequential code analyzers in search of parallelism. So that in this way, they generate a file like the **Parallel.yml** describing the parallelism found in a given sequential code. In the same way this file can be taken by a code annotator to write it with the corresponding directives indicated by the analyzer. This will finally allow to divide the compilation process into two parts: code analysis and annotation, in **automatic parallelizer compilers -->

###### context.yml

It is a metadata file in YAML format which contains values for the variables defined in a given template.

<!-- ## Example

one of the implemented templates follows the stencil parallel programming pattern.  -->

## Tests

```bash
python3 -m unittest tests.parallel_templates_loader
```

#### Play with the API

This tool has an API to interact with the templates available in the application, at the moment it only has the template of the stencil parallel programming pattern. However, you can contribute to the growth of these. the Api was made with [Flask Restplus](https://flask-restplus.readthedocs.io/en/stable/). To run a API install requirements and run the application as follows:

```bash
pip3 install -r ./api/requirements.txt
python3 api/app.py
```

#### API Enpoints

The application expose the following endpoints to interact with.

| HTTP Method | URI | Action |
|---|---|---|
| GET | http://[hostname]/templates | Retrieve list of templates |
| GET | http://[hostname]/templates/[template_name] | Retrieve a template detail |
| POST | http://[hostname]/templates/[template_name] | Render a template |

## Deployment with Docker

Perform the following commands to build the **parallel_templates** image, then to run the **parallel_templates** API in a container. These command need to be 
performed from the project root directory.

```sh
docker build -t parallel_templates .
docker run -d -v ${PWD}:/usr/src/app --name parallel_templates -p 5000:5000 parallel_templates
```
<!-- 
## Todo

* Una funcionalidad en manager que termita checkear si un template puede ser renderizado con su contexto apropiadamente.

* Una funcionalidad que permita verificar que todos los templates pueden ser renderizados con su contexto de ejemplo correctamente. -->

## References

[Structured Parallel Programming: Patterns for Efficient Computation](https://www.amazon.com/Structured-Parallel-Programming-Efficient-Computation/dp/0124159931)

[Designing a RESTful API using Flask-RESTful](https://blog.miguelgrinberg.com/post/designing-a-restful-api-using-flask-restful)

[REST API response format using HTTP status codes](https://github.com/adnan-kamili/rest-api-response-format)

[Flask-RESTful](http://flask-restful.readthedocs.io/en/latest/)

[Designing a RESTful API with Python and Flask](https://blog.miguelgrinberg.com/post/designing-a-restful-api-with-python-and-flask)

[AJAX with jQuery](http://flask.pocoo.org/docs/0.12/patterns/jquery/)

[Flask Examples Github](https://github.com/pallets/flask/tree/master/examples/jqueryexample)