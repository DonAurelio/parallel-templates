# -*- encoding: utf-8 -*-

"""Each file in a template folder has a respectve class.
This module defines a class for each file in the templates folder
of catt.
"""

import os
import yaml
import shutil
import jinja2


class SourceCodeFile(object):
    
    def __init__(self,name,ftype,text):

        self._name = name
        self._ftype = ftype
        self._text = text

    @property
    def file_name(self):
        return self._name

    @property
    def file_type(self):
        return self._ftype

    @property
    def file_text(self):
        return self._text


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

    @property
    def file_name(self):
        return 'template.c'

    @property
    def file_type(self):
        return 'template'

    def render(self,context):
        """Returns a source code froma given template."""
        template = jinja2.Template(self.source)
        source = template.render(dict(context.data))

        file_name = self.pattern_name + '.c'
        file_type = 'c99'
        file_text = source

        source_code_file = SourceCodeFile(
            file_name,
            file_type,
            file_text 
        )

        return source_code_file


class Parallel(object):

    def __init__(self,parallel_string):

        #: dict: The Cafile containing data.
        self.data = yaml.load(parallel_string)
        #: string: The raw cafile data in yaml format.
        self.source = parallel_string

    @property
    def file_name(self):
        return 'parallel.yml'

    @property
    def file_type(self):
        return 'yml'


    def description(self):
        data = {
            'name': self.data.get('name',''),
            'description': self.data.get('description','')
        }
        return data


class ContextFile(object):

    def __init__(self,context_string):

        #: dict: The Cafile containing data.
        self.data = yaml.load(context_string)
        #: string: The raw cafile data in yaml format.
        self.source = context_string

    @property
    def file_name(self):
        """Returns a name for a given cafile."""
        return 'context.yml'

    @property
    def file_type(self):
        return 'yml'
