from flask_restplus import Api
from .template import template


api = Api(
    title='Catt Api',
    version='1.0',
    description="""Provides a set of parallel programming 
    templates for cellular automata programming in c99 source 
    code which allow easy parallelization."""
)

# Adding template resource namesace to the API
api.add_namespace(template.api)
