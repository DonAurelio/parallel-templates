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
        cafile_dict = self._cafile.data
        return self._template.render(template.Context(cafile_dict))

    @property
    def path_to_file(self):
        return self._django_template.origin.name