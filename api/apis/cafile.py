from flask_restplus import Namespace, Resource, fields
from catt.core.manager import CafileManager


# Defining the name space for Catt cafile
api = Namespace('cafile',description='Defines a cafile object.')

# Defining cafile json model
neighborhood_fields = api.model('Neighborhood',{})

lattice_fields = api.model(
    'Lattice',{
        'rowdim': fields.Integer(
            required=True,
            default=1000,
            description="Cellular space height."
        ),
        'coldim': fields.Integer(
            required=True,
            default=1000,
            description="Cellular space width."
        ),
        'type': fields.String(
            required=True,
            default='int',
            description="Cells state type (int|float|double)"
        ),
        'neighborhood': fields.Nested(
            neighborhood_fields,
            required=True,
            default={
                'up': [-1,1],
                'down': [1,1],
                'left': [1,1],
                'right': [-1,-1]
            },
            description="Neighbors name and relative offsets",
        )
})

cafile_model = api.model(
    'Cafile',{
        'pattern_name': fields.String(
            required=True,
            default='stencil',
            description="The parallel programming pattern"
        ),
        'lattice': fields.Nested(lattice_fields),
        'generations': fields.Integer(
            required=True, 
            description='Number of generations the system would evolve.'
        )
})