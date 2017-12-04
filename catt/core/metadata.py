# -*- encoding: utf-8 -*-

"""Each file in a template folder has a respectve class.
This module defines a class for each file in the templates folder
of catt.
"""

import os
import yaml
import shutil
from . import settings
from django import template


class Cafile(object):

    def __init__(self,cafile_dict):
        """An interface to the cafile.yml file data.
        A basic cafile data in YML format is depicted as follows,
        basically a cafile specifies some properties needed to 
        contruct a celular automata model in c99 source code.

        Example:

            lattice: 
              rowdim: 20
              coldim: 20
              type: bool
              neighborhood:
                up: [-1,1]
                down: [1,1]
                left: [1,1]
                right: [-1,-1]
            generations: 20

        Args:
            cafile_dict (dict): A dict with a description of a 
                given cellular automata.
        """

        #: dict: The Cafile containing data.
        self._data = cafile_dict

    @property
    def data(self):
        """Returns the Cafile data."""
        return self._data


class Parallel(object):

    def __init__(self,pattern_name):
        """An interface to the parallel.yml file data.
        A basic parallel file data in YML format is depicted in the 
        followig ``Example``, basically a parallel file is a description
        about how a given code should be parallelized.

        Example:
            parallel:
              # Function
                evolve:
                  # OpenMP direcives
                  omp:
                    parallel:
                      # Parallel directive clauses
                      num_threads: '4'
                      shared: [C,A,B]
                      default: none

        Args:
            pattern_name (str): The parallel programming pattern from 
                whitch we require the parallel file.

        """

        file_path = os.path.join(pattern_name,settings.TEMPLATE_FILE_NAME)
        
        engine = template.engine.Engine(dirs=settings.TEMPLATE_DIRS)
        django_template = engine.get_template(file_path)
        dir_path = os.path.dirname(django_template.origin.name)
        file_path = os.path.join(dir_path,settings.PARALLEL_FILE_NAME)

        #: dict: The parallel file containing data.
        self._data = {}
        with open(file_path,'r') as infile:
            self._data = yaml.load(infile)

    def get_basic_info(self):
        """Returns the info of a parallel file."""

        basic_data = {
            'name': self._data['name'],
            'description': self._data['description']
        }

        return basic_data


class Template(object):

    def __init__(self,pattern_name):
        """An interface to a template.c file.
        A *template.c* file, is a common c99 source code that enclose a 
        parallel programming pattern, so it is a piece of code from which 
        the programer should start if he/she would like to parallelize 
        the code in a near future.
        """

        #: str: The parallel programming name.
        self._pattern_name = pattern_name

        file_path = os.path.join(pattern_name,settings.TEMPLATE_FILE_NAME)
        engine = template.engine.Engine(dirs=settings.TEMPLATE_DIRS)
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
        """Returns the path to the file."""
        return self._django_template.origin.name