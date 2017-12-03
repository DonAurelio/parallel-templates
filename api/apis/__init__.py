from flask_restplus import Api

# from .cafile import api as cafile_namespace
from .template import api as template_namespace


api = Api(
    title='Catt Api',
    version='1.0',
    description="""Provides a set of parallel programming 
    patterns in c 99 source code for efficient parallelization."""
)

# api.add_namespace(cafile_namespace)
api.add_namespace(template_namespace)
