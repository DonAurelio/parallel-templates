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

        # Template info is described in the parallel.yml metadata
        parallel_file = loader.get_parallel_file(template_name)
        data = parallel_file.description()
        return data

    def render_to_data(template_name,cafile_string):

        template = loader.get_template(template_name)
        cafile =  metadata.Cafile(cafile_string)
        raw_code = template.render(cafile)

        parallel_file = loader.get_parallel_file(template_name)

        data = [
            {
                'name': template_name,
                'ftype': template.file_type,
                'text': raw_code
            },
            {
                'name': parallel_file.file_name,
                'ftype': parallel_file.file_type,
                'text': parallel_file.source
            }
        ]

        return data