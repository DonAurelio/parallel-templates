# -*- encoding: utf-8 -*-

"""
References:
[1] Working without settings with django template engine 
http://stackoverflow.com/questions/98135/how-do-i-use-django-templates-without-the-rest-of-django
[2] Django Template 
https://docs.djangoproject.com/en/1.11/ref/templates/api/
[3] Django Engine Source
https://docs.djangoproject.com/en/1.11/_modules/django/template/engine/#Engine.get_template
[4] Autoscape django template
http://stackoverflow.com/questions/11306669/django-template-escaping
"""

import os
from django import template
from . import settings


class CATemplate(object):

    def __init__(self,cafile):
        """Cellular automata template class.

        Manage all templates located in settings.TEMPLATE_DIRS. Allows
        template selection and template rendering. A template is created
        given a ``pattern_name``, this name match with a folder in
        settings.TEMPLATE_DIRS wich has a template.c file.

        Note:
            No notes.

        Args:
            pattern_name (str): The name of the cellular autómata programming 
                pattern we require.

        """

        #: str: an instance of CAFile which content additional data for template rendering
        self._cafile = cafile

        #: str: A path, the unique location to the file
        self._file_path = os.path.join(cafile.pattern_name,settings.TEMPLATE_NAME)

        engine = template.engine.Engine(dirs=settings.TEMPLATE_DIRS)
        #: Django Template:  Template corresponding to the selected pattern
        self._template = engine.get_template(self._file_path)

    def render(self):
        """Render the template given a cafile instance.

        Args:
            cafile: It is a CAFile object.

        Returns:
            An string with a rendered C99 raw code.

        """
        cafile_dict = self._cafile.data
        return self._template.render(template.Context(cafile_dict))

    def render_to_file(self,dir_path):
        """Render the template, but the output is a dir_path.


        Creates a rendered file named as ``_pattern_name`` attribute, 
        given a CAFile instance and a directory path on which the file
        will be writen.

        Args:
            cafile: It is a CAFile object.
            dir_path: It is the unique location to the folder on which
                the code will be rendered.

        Returns:
            The file_path on which the C99 source file was rendered.

        """

        file_name = self._cafile.pattern_name + '.c'
        file_path = os.path.join(dir_path,file_name)
        with open(file_path,'w') as codefile:
            raw_code = self.render()
            codefile.write(raw_code)

        return file_path

    def __str__(self):
        """Returns and string represenation of the selected template."""
        with open(self._template.origin.name,'r') as template_file:
            return template_file.read()
        
    def __unicode__(self):
        """Returns and string represenation of the selected template."""
        with open(self._template.origin.name,'r') as template_file:
            return template_file.read()
