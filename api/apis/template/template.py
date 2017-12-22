from flask import request
from flask_restplus import Namespace, Resource

from catt.manager import TemplateManager

from . import models


# Defining the name space for templates resuce.
api = Namespace('templates',description='Allows to obtain information of the available templates.')


# Defining cafile model
cafile = api.model('Cafile',models.cafile_model)


@api.route('')
class TemplateList(Resource):
    """list Cellular Automata available templates."""

    def head(self):
        """Used for clients to check if template resource is available."""
        data = {}
        return data

    def get(self):
        """Return a list of the available c99 source code templates."""
        manager = TemplateManager()
        data = manager.list_templates()
        return data


@api.route('/<string:name>')
class TemplateDetail(Resource):
    """Cellular Automata Templates detail and rederization."""

    def get(self,name):
        """Returns the template info given its name."""
        manager = TemplateManager()
        data = manager.get_template_detail(name)

        return data

    @api.expect(cafile)
    def post(self,name):
        """Returns c99 source code give a cafile metadata."""

        cafile_data = request.get_json()
        raw_cafile = cafile_data.get('text','')
        
        manager = TemplateManager()
        data = manager.render_to_data(name,raw_cafile)

        return data