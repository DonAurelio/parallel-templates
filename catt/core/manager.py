# -*- encoding: utf-8 -*-

"""Each class in the *metadata* module is managed by a facade on present module.
"""

import os
import yaml

from . import metadata
from . import settings


class ParallelManager(object):

    def __init__(self):
        """A facade to access the ``metadata.Parallel`` class functionalities."""
        pass

    def get_file_info(self,template_name):
        """Returns the info of a parallel file.
        The basic info of a parallel file is the *name* of 
        the parallel proramming pattern an a *description*
        of the semantic of the same.

        Args:
            template_name (str): The name of the parallel programming
                pattern template we request info.

        Returns:
            Dict containing the parallel file basic info.
        """

        parallel = metadata.Parallel(template_name)
        info = parallel.get_basic_info()

        return info


class TemplateManager(object):
    """A facade to access the ``metadata.Template```functionalities."""

    def get_rendered_template(self,template_name,cafile_dict):
        """Render a ``metadat.Template`` instance given a 
        A   *C99 template
            *C99 source code.  
        """

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