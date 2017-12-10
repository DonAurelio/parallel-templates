from flask import request
from flask_restplus import Namespace, Resource
from catt.core.manager import TemplatesFolderManager
from catt.core.manager import TemplateManager
from catt.core.manager import ParallelManager
from .cafile import cafile_model


# Defining the name space for Catt templates
api = Namespace('templates',description='Allows to obtain information of the available templates.')


@api.route('')
class TemplateList(Resource):
    """Deals with templates list tasks."""

    def get(self):
        """Returns a list of the available parallel pattern templates."""
        manager = TemplatesFolderManager()
        data = {
            'success':"The template list was loaded successfully.",
            'data':{
                'template_list': manager.list_available_templates()
            }
        }
        return data


@api.route('/<string:name>')
class TemplateDetail(Resource):
    """Deals with templates detail tasks."""

    def get(self,name):
        """Returns the template info given its name."""
        manager = TemplateManager()
        info = manager.get_template_info(name)
        data = {
            'template_datail': info
        }
        return data

    @api.expect(cafile_model)
    def post(self,name):
        """Returns c99 source code give a cafile metadata."""

        data = request.json

        t_manager = TemplateManager()
        template_file_data = t_manager.get_template_data(name,data)
        
        p_manager = ParallelManager()
        parallel_file_data = p_manager.get_parallel_file_data(name)

        data = {
            'success':"The template '%s' was loaded successfully." % name,
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
