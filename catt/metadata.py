# -*- encoding: utf-8 -*-

"""Each file in a template folder has a respectve class.
This module defines a class for each file in the templates folder
of catt.
"""

import os
import yaml
import shutil
import jinja2

class Template(object):

    def __init__(self,template_string,pattern_name='unnamed',origin='unknown'):
        """A C99 Source Code Template.

        A *C99 Source Code template* is a C99 source file with some 
        template syntax as depicted in the ``Example``. The C99
        template follows a given parallel programming pattern. This 
        style of programming enable the easy parallelization of the 
        code in a near future.

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

        #: str: The raw C99 source code with template syntax
        self.source = template_string

        #: str: The parallel programming pattern name
        self.pattern_name = pattern_name

        #: str: Path to the file
        self.origin = origin

    def render(self,cafile_obj):
        """Render the C99 Source Code Template given a Cafile instance.

        Args:
            cafile_obj (Cafile): The data that will be placed in the
                C99 Source Code Template to generate a C99 Source Code.

        Returns:
            A raw string C99 Source Code.

        """
        template = jinja2.Template(self.source)
        print('data',cafile_obj.data)
        source = template.render(cafile_obj.data)
  
        return source

    @property
    def file_name(self):
        return self.pattern_name + '.c'

    @property
    def file_type(self):
        return 'c99'

    def to_dict(self):
        data = {
            'name': self.file_name,
            'ftype': self.file_type,
            'text': self.source
        }

        return data 


class Parallel(object):

    def __init__(self,parallel_string):

        #: dict: The Cafile containing data.
        self.data = yaml.load(parallel_string)
        #: string: The raw cafile data in yaml format.
        self.source = parallel_string

    @property
    def pattern_name(self):
        return self.data.get('name','')

    @property
    def file_name(self):
        return 'parallel.yml'

    @property
    def file_type(self):
        return 'yml'

    def to_dict(self):
        data = {
            'name': self.file_name,
            'ftype': self.file_type,
            'text': self.source
        }

        return data


class Cafile(object):

    def __init__(self,cafile_string):
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
            cafile_string (str): A string containing cellular 
                automata system settings.
        """

        #: dict: The Cafile containing data.
        self.data = yaml.load(cafile_string)
        #: string: The raw cafile data in yaml format.
        self.source = cafile_string

    @property
    def file_name(self):
        """Returns a name for a given cafile."""
        return 'cafile.yml'

    @property
    def file_type(self):
        return 'yml'
