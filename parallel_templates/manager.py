# -*- encoding: utf-8 -*-

"""Each class in the *metadata* module is managed by a facade on present module.
"""

import os
import yaml

from . import loader
from . import metadata


class TemplateManager(object):
    """A facade to access the ``metadata.Template```functionalities."""

    def list_templates(self):
        return loader.list_template_dirs()

    def get_template_detail(self,template_name):

        # Template info is described in the parallel.yml metadata file
        parallel_file = loader.get_parallel_file(template_name)

        data = None
        if parallel_file:
            data = parallel_file.description()
        
        return data

    def render_template_to_data(self,template_name,context_str):

        template = loader.get_template(template_name)
        parallel = loader.get_parallel_file(template_name)

        data = None
        if template and parallel:
            context =  metadata.ContextFile(context_str)
            source_code = template.render(context)

            data = [
                {
                    'name': source_code.file_name,
                    'ftype': source_code.file_type,
                    'text': source_code.file_text
                },
                {
                    'name': parallel.file_name,
                    'ftype': parallel.file_type,
                    'text': parallel.source
                }
            ]

        return data