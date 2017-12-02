from flask_restful import Resource
from catt.core.manager import TemplateFolderManager

class TemplateList(Resource):

    def get(self):
        """Retrieve a list of the available parallel pattern templates."""
        manager = TemplateFolderManager()
        data = {}
        data['templates'] = manager.list_available_templates()
        return data

class TemplateDetail(Resource):

    def get(self,name):
        """Retrieve a list of the available parallel pattern templates."""
        manager = TemplateFolderManager()
        data = {}
        data['template'] = manager.get_template_info(name)
        return data


class Catt(Resource):
    """docstring for Catt"""

    def get(self):
        pass

    def post(self):
        pass


