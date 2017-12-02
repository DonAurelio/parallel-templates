import os
from django import template
from . import settings as catt_settings


class TemplateManager(object):
    """TemplateManager is the administrator of the templates directory."""

    def list_available_templates(self):
        """List all available directories in the templates directory."""

        available_templates = []
        for search_dir in catt_settings.TEMPLATE_DIRS:
            available_templates += [ name for name in os.listdir(search_dir) 
            if os.path.isdir(os.path.join(search_dir,name))]

        return available_templates


    def get_template(self):

        engine = template.engine.Engine(dirs=catt_settings.TEMPLATE_DIRS)
        file_path = os.path.join(template_name,catt_settings.TEMPLATE_FILE_NAME)
        
        #: Django Template:  Template corresponding to the selected pattern
        template = engine.get_template(file_path)

        return template

        # with open(self._template.origin.name,'r') as template_file:
        #     return template_file.read()

    def get_template_info(template_name):
        pass


     # ?¿
    def get_template_content(template_name):
        pass