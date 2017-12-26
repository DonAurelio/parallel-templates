from flask import request
from flask_restplus import Namespace, Resource

from parallel_templates.manager import TemplateManager

from . import models


# Defining the name space for templates resuce.
api = Namespace(
    'templates',
    description='Allows to obtain information about available parallel programing c99 templates.')


# Defining cafile model
context = api.model('Context',models.context_model)


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

        if not data:
            return {'message':"The template '%s' does not exist" % name}, 404

        return data

    @api.expect(context)
    def post(self,name):
        """Returns c99 source code give a cafile metadata."""

        context = request.get_json()
        context_text = context.get('text','')
        manager = TemplateManager()
        data = manager.render_template_to_data(name,context_text)

        if not data:
            return {'message':"The template '%s' does not exist" % name}, 404

        return data