import os
import yaml
from django import template as django_template
from . import settings


class ParallelFileManager(object):

    def get_file_info(self,template_name):
        """Returns the info of a parallel file."""

        file_path = os.path.join(template_name,settings.TEMPLATE_FILE_NAME)
        
        engine = django_template.engine.Engine(dirs=settings.TEMPLATE_DIRS)
        template = engine.get_template(file_path)
        dir_path = os.path.dirname(template.origin.name)
        file_path = os.path.join(dir_path,settings.PARALLEL_FILE_NAME)

        # Some isses: Verify if the parallel file exists into the template_name
        # folder
        if not os.path.exists(file_path):
            pass

        # Some isses: The 'name' and 'descriptions keys' 
        # could not be in the data dictionary. So it will
        # raise an exception.
        template_data = {}
        with open(file_path,'r') as infile:
            data = yaml.load(infile)
            template_data['name'] = data['name']
            template_data['description'] = data['description']

        return template_data


class TemplateFileManager(object):

    def get_template_object(self,template_name):

        file_path = os.path.join(template_name,settings.TEMPLATE_FILE_NAME)
        engine = django_template.engine.Engine(dirs=settings.TEMPLATE_DIRS)
        template = engine.get_template(file_path)

        return template


    def get_template_info(self,template_name):

        template = self.get_template(template_name)
        dir_path = os.path.dirname(template.origin.name)
        parallel_file_manager = ParallelFileManager()
        return parallel_file_manager.get_file_info(dir_path)


class CafileManager(object):

    def get_cafile_syntax(self):
        file_path = settings.CAFILE_PATH
        with open(file_path,'r') as infile:
            return yaml.load(infile)



class TemplateFolderManager(object):
    """TemplateManager is the administrator of the templates directory."""

    def list_available_templates(self):
        """List all available directories in the templates directory."""

        available_templates = []
        for search_dir in settings.TEMPLATE_DIRS:
            available_templates += [ name for name in os.listdir(search_dir) 
            if os.path.isdir(os.path.join(search_dir,name))]

        return available_templates


    def get_template_info(self,template_name):

        manager = ParallelFileManager()
        info = manager.get_file_info(template_name)

        return info

    def get_cafile_syntax_json(self):

        manager = CafileManager()
        cafile = manager.get_cafile_syntax_json()
        return cafile
