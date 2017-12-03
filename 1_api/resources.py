from flask_restful import Resource
from catt.core.manager import TemplateFolderManager

class TemplateList(Resource):

    def get(self):
        """Retrieve a list of the available parallel pattern templates."""
        manager = TemplateFolderManager()
        data = {}
        data['template_list'] = manager.list_available_templates()
        return data

class TemplateDetail(Resource):

    def get(self,name):
        """Retrieve a list of the available parallel pattern templates."""
        manager = TemplateFolderManager()
        detail = manager.get_template_info(name)

        data = {}
        if not detail:
            data['message'] = 'template %s does not exist.' % (name,)
        
        data['template_detail'] = manager.get_template_info(name)
        return data


class Catt(Resource):
    """docstring for Catt"""

    def get(self):
        manager = TemplateFolderManager()
        data = {}
        data['cafile'] = manager.get_cafile_syntax_json()
        return data

    def post(self):
        pass


