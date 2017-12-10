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

    @staticmethod
    def _get_file_path(pattern_name):

        file_path = os.path.join(pattern_name,settings.TEMPLATE_FILE_NAME)
        
        engine = template.engine.Engine(dirs=settings.TEMPLATE_DIRS)
        django_template = engine.get_template(file_path)
        dir_path = os.path.dirname(django_template.origin.name)
        file_path = os.path.join(dir_path,settings.PARALLEL_FILE_NAME)

        return file_path

    @staticmethod
    def _load_data(file_path):
        with open(file_path,'r') as infile:
            return yaml.load(infile)

    @staticmethod
    def _load_raw(file_path):
        with open(file_path,'r') as infile:
            return infile.read()

    def __init__(self,pattern_name):
        """An interface to the parallel.yml file data.
        A basic parallel file data in YML format is depicted in the 
        followig ``Example``, *basically a parallel.yml contains some metadata
        related with a c99 source code*, additionally  gives a description about 
        how the related c99 source code should be parallelized.

        Example:
            ...
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
            ...

        Args:
            pattern_name (str): The parallel programming pattern from 
                whitch we require the parallel file.

        """

        file_path = self._get_file_path(pattern_name)

        #: dict: The parallel file containing data.
        self._data = self._load_data(file_path)

        self._raw = self._load_raw(file_path)

        self._pattern_name = pattern_name

        self._file_name = os.path.basename(file_path)

    @property
    def data(self):
        return self._data

    @property
    def raw(self):
        return self._raw

    @property
    def pattern_name(self):
        return self._pattern_name

    @property
    def file_name(self):
        return self._file_name

    def get_basic_info(self):
        """Returns the info of a parallel file."""

        basic_data = {
            'name': self._data['name'],
            'description': self._data['description']
        }

        return basic_data


class Template(object):

    def __init__(self,pattern_name):
        """An interface to a C99 Source Code Template.
        A *C99 Source Code Template* is a C99 source file with some 
        django template syntax as depicted in the ``Example``. This 
        syntax allow us to generate C99 code. The structure of the 
        template follows a given parallel programming pattern. This 
        style of programming enable the easy parallelization of the 
        code in a near future.

        Note:
            The variables specified in the template will be replaced
            with the data specified in a given *Cafile*, this step is 
            called template renderization.

        Example:
            ...
            struct Neighborhood
            {
                {% for neighbor in lattice.neighborhood.keys %}
                {{ lattice.type }} {{ neighbor }};
                {% endfor %}
            };
            ...
        """

        #: str: The parallel programming pattern name.
        self._pattern_name = pattern_name

        file_path = os.path.join(pattern_name,settings.TEMPLATE_FILE_NAME)
        engine = template.engine.Engine(dirs=settings.TEMPLATE_DIRS)
        self._django_template = engine.get_template(file_path)

    def render(self,cafile_obj):
        """Render the C99 Source Code Template given a Cafile instance.

        Args:
            cafile_obj (Cafile): The data that will be placed in the
                C99 Source Code Template to generate a C99 Source Code.

        Returns:
            A raw string C99 Source Code.

        """
        cafile_dict = cafile_obj.data
        return self._django_template.render(template.Context(cafile_dict))

    @property
    def path_to_file(self):
        """Returns the path to the file."""
        return self._django_template.origin.name

    @property
    def file_name(self):
        return self._pattern_name + '.c'