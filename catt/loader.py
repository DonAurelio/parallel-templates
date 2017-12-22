"""
Allows to find files of a determined template and returns a object 
in Python that represents that file.
"""

import os
from . import settings

def find_template_dir(template_name):
    """Return the path to a template directory with the give template name.
    
    Args:
        template_name (str): the name of the folder 
            we are looking for.
    """
    
    template_path = None
    for templates_dir in settings.TEMPLATE_DIRS:
        if template_name in os.listdir(templates_dir):
            template_path = os.path.join(templates_dir,template_name)

    return template_path


def get_template(template_name):
    """Return a template object from the given template name directory."""
    pass


def render_to_string(template_name,context):
    pass



def from_string(self, template_code):
    pass