from flask import request
from flask_restplus import Namespace, Resource, fields
from catt.core.manager import CafileManager


# Defining the name space for Catt cafile
api = Namespace('cafile',description='Allows to get a c99 source code given a cafile object.')

neighborhood_fields = api.model('Neighborhood',{})

lattice_fields = api.model('Lattice',{
    'rowdim': fields.Integer(required=True, description="Cellular space height."),
    'coldim': fields.Integer(required=True, description="Cellular space width."),
    'type': fields.String(required=True, description="Cells state type."),
    'neighborhood': fields.Nested(neighborhood_fields)
})

cafile = api.model('Cafile',{
    'pattern_name': fields.String(required=True, description="The parallel programming pattern"),
    'lattice': fields.Nested(lattice_fields),
    'generations': fields.Integer(required=True, description='Number of generations the system would evolve.')
})

# Schema model
# cafile = api.schema_model('Person', {
#     'required': ['address'],
#     'properties': {
#         'name': {
#             'type': 'string'
#         },
#         'age': {
#             "type": "object",
#             "minProperties": 1,
#             'patternProperties': {
#                 "^(/[^/]+)+$": {}
#             }
#         }
#     },
#     'type': 'object'
# })


@api.route('/render')
class CafileRender(Resource):
    """Deals with cafile renderization tasks."""

    @api.expect(cafile)
    def post(self):
        """Given a cafile, render it into a c99 source code."""

        data = request.json

        return data
