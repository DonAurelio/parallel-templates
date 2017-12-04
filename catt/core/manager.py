import os
import yaml

from . import metadata
from . import settings


class ParallelManager(object):

    def get_file_info(self,template_name):
        """Returns the info of a parallel file."""

        parallel = metadata.Parallel(template_name)
        info = parallel.get_basic_info()

        return info


class TemplateManager(object):

    def get_template_info(self,template_name):

        manager = ParallelManager()
        info = manager.get_file_info(template_name)
        
        return info

    def get_rendered_template(self,template_name,cafile_dict):

        template = metadata.Template(template_name)
        cafile = metadata.Cafile(cafile_dict)

        rendered_template = template.render(cafile)

        return rendered_template


class CafileManager(object):

    def __init__(self):
        pass



class TemplatesFolderManager(object):
    """TemplateManager is the administrator of the templates directory."""

    def list_available_templates(self):
        """List all available directories in the templates directory."""

        available_templates = []
        for search_dir in settings.TEMPLATE_DIRS:
            available_templates += [ name for name in os.listdir(search_dir) 
            if os.path.isdir(os.path.join(search_dir,name))]

        return available_templates