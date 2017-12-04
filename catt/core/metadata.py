# -*- encoding: utf-8 -*-

import os
import yaml
import shutil
from . import settings
from django import template


class CAFile(object):

    def __init__(self,cafile_dict):
        self._data = cafile_dict

    @property
    def data(self):
        """Returns the Cafile data."""
        return self._data

    @property
    def pattern_name(self):
        return self._data['pattern_name']


class Parallel(object):

    def __init__(self,pattern_name):

        file_path = os.path.join(pattern_name,settings.TEMPLATE_FILE_NAME)
        
        engine = template.engine.Engine(dirs=settings.TEMPLATE_DIRS)
        django_template = engine.get_template(file_path)
        dir_path = os.path.dirname(django_template.origin.name)
        file_path = os.path.join(dir_path,settings.PARALLEL_FILE_NAME)

        self._data = {}
        with open(file_path,'r') as infile:
            self._data = yaml.load(infile)

    def get_basic_info(self):
        """Returns the info of a parallel file."""

        file_path = os.path.join(template_dir_path,settings.PARALLEL_FILE_NAME)

        basic_data = {
            'name': self._data['name'],
            'descrition': self._data['descrition']
        }

        return basic_data


class Template(object):

    def __init__(self,template_name):

        self._pattern_name = template_name

        file_path = os.path.join(template_name,settings.TEMPLATE_FILE_NAME)
        engine = django_template.engine.Engine(dirs=settings.TEMPLATE_DIRS)
        self._django_template = engine.get_template(file_path)

    def render(self,cafile_obj):
        """Render the template given a cafile instance.

        Args:
            cafile_obj: It is a CAFile object.

        Returns:
            An string with a rendered C99 raw code.

        """
        cafile_dict = cafile_obj.data
        return self._django_template.render(template.Context(cafile_dict))

    @property
    def path_to_file(self):
        return self._django_template.origin.name