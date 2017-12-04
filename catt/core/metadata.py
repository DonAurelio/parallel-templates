# -*- encoding: utf-8 -*-

import os
import yaml
import shutil
from . import settings


class CAFile(object):

    def __init__(self,data):
        self._data = data

    @property
    def data(self):
        """Returns the Cafile data."""
        return self._data

    @property
    def pattern_name(self):
        return self._data['pattern_name']


class Parallel(object):

    def get_info(self,template_dir_path):
        """Returns the info of a parallel file."""

        file_path = os.path.join(template_dir_path,settings.PARALLEL_FILE_NAME)

        # Some isses: Verify if the parallel file exists into the template_name
        # folder
        if not os.path.exists(file_path):
            pass

        # Some isses: The 'name' and 'descriptions keys' 
        # could not be in the data dictionary. So it will
        # raise an exception.
        template_data = {}
        with open(file_path,'r') as infile:
            data = yaml.load(cafile)
            template_data['name'] = data['name']
            template_data['description'] = data['description']

        return template_data