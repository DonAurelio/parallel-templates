# Parallel Templates

[![Build Status](https://travis-ci.org/DonAurelio/parallel-templates.svg?branch=master)](https://travis-ci.org/DonAurelio/parallel-templates)

It is a set of templates of parallel programming patterns in C (for High Performance Compiting). For example: **stencil** to programing differential equation solvers and cellular automatas; **map** to replicate an operation or function over a collection, bettwen other parallel programing patterns. 

Each template consists of 3 files: **template.c**, **parallel.yml** and **context.yml**

```bash
parallel-templates
│
└───templates
        ├── stencil
        │   ├── template.c
        │   ├── parallel.yml
        │   ├── context.yml
        │   └── Makefile 
        └── map
            ├── template.c
            ├── parallel.yml
            ├── context.yml
            └── Makefile 
```

## Files Descrition 

* template.c

...It is a code wirtten C, but with some [jinja2](http://jinja.pocoo.org/) template syntax to add more flexibility to the user using the same template for different problems related with the same parallel programming pattern. This template must have a parallel programming pattern implicit. Additionally it must also be easily reusable.

* parallel.yml

...It is a metadata file in YAML format which in addition to having information of the template. It contains details of how it should be parallelized. That is, what OpenMP and OpenACC compile directives should go in each function and what loop lexicographically. This file is related with [#pragcc](https://github.com/DonAurelio/pragcc) tool.

* context.yml

...It is a metadata file in YAML format which contains values for the variables defined in a given template. This file can be modified by the user to get the same template with different values required by the problem to be specified in code.

* Makefile

...Contains the neccesary rules to compile and run the code, sequential and parallel.

## Tests

The parallel_templates module is automatic tested by [Travis CI](https://travis-ci.org/), but you can perform test individually from the root directory ad follows.  

```bash
python3 -m unittest tests/loader.py
python3 -m unittest tests/templates.py
```

## API

This tool has an API to interact with the templates available in the application, at the moment it only has the stencil parallel programming pattern template. However, **you can contribute to the growth of these**. 

The Api was developed with [Flask Restplus](https://flask-restplus.readthedocs.io/en/stable/). To run a API install requirements and run the application from the root directory ad follows:


```bash
pip3 install -r ./api/requirements.txt
python3 api/app.py
```

The API with run at [http://localhost:5000](http://localhost:5000)

### Deployment

The API can run inside a Docker Container. To get it done, perform the following commands from the root directory.

```sh
docker build -t templates .
docker run -d -v ${PWD}:/usr/src/app --name templates -p 5000:5000 templates
```


# References

[Structured Parallel Programming: Patterns for Efficient Computation](https://www.amazon.com/Structured-Parallel-Programming-Efficient-Computation/dp/0124159931)

[Designing a RESTful API using Flask-RESTful](https://blog.miguelgrinberg.com/post/designing-a-restful-api-using-flask-restful)

[REST API response format using HTTP status codes](https://github.com/adnan-kamili/rest-api-response-format)

[Flask-RESTful](http://flask-restful.readthedocs.io/en/latest/)

[Designing a RESTful API with Python and Flask](https://blog.miguelgrinberg.com/post/designing-a-restful-api-with-python-and-flask)

[AJAX with jQuery](http://flask.pocoo.org/docs/0.12/patterns/jquery/)

[Flask Examples Github](https://github.com/pallets/flask/tree/master/examples/jqueryexample)
