from flask_restplus import Api
from .template import template


api = Api(
    title='C99 Parallel Template Api',
    version='1.0',
    description="""Provides a set of parallel programming 
    templates for easy parallelization."""
)

# Adding template resource namesace to the API
api.add_namespace(template.api)
