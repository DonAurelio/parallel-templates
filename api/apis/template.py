from flask import request
from flask_restplus import Namespace, Resource, fields
from catt.manager import TemplatesFolderManager
from catt.manager import TemplateManager
from catt.manager import ParallelManager


# Defining the name space for templates resuce.
api = Namespace('templates',description='Allows to obtain information of the available templates.')


# Defining cafile model
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

Cafile = api.model(
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


@api.route('')
class TemplateList(Resource):
    """List templates."""

    def get(self):
        """Return a list of the available c99 source code templates."""
        manager = TemplatesFolderManager()
        data = {
            'message':"The template list was loaded successfully.",
            'data':{
                'template_list': manager.list_available_templates()
            }
        }
        return data


@api.route('/<string:name>')
class TemplateDetail(Resource):
    """Cellular Automata Templates detail and rederization."""

    def get(self,name):
        """Returns the template info given its name."""
        manager = TemplateManager()
        info = manager.get_template_info(name)
        data = {
            'message':"The template list was loaded successfully. ",
            'data': {
                'template_detail': info
            }
        }
        return data

    @api.expect(Cafile)
    def post(self,name):
        """Returns c99 source code give a cafile metadata."""

        data = request.get_json()
        t_manager = TemplateManager()
        template_file_data = t_manager.get_template_data(name,data)
        
        p_manager = ParallelManager()
        parallel_file_data = p_manager.get_parallel_file_data(name)

        data = {
            'message':"The template '%s' was loaded successfully." % name,
            'data': {
                'files':[
                    template_file_data,
                    parallel_file_data
                ]
            }
        }

        return data


# Defining error handlers
from django.template import TemplateDoesNotExist


@api.errorhandler(TemplateDoesNotExist)
def handle_template_does_not_exist(error):
    """Returns a custom message for TemplateDoesNotExist."""
    return {'message':'Some error has ocurred !!','error':error}
