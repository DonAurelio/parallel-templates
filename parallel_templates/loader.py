"""
Allows to find files of a determined template and returns
an object which represents the given file.
"""

import os
from . import settings
from . import metadata


def find_template_path(template_name):
    """Return the path to the template with the given template_name."""
    
    template_path = ''
    for templates_dir in settings.TEMPLATE_DIRS:
        if template_name in os.listdir(templates_dir):
            template_path = os.path.join(templates_dir,template_name)

    return template_path


def list_template_dirs():
    """List names of directories containnig parallel programming templates."""

    dirs = []
    for templates_dir in settings.TEMPLATE_DIRS:
        for template_dir in os.listdir(templates_dir):
            path = os.path.join(templates_dir,template_dir)
            if os.path.isdir(path):
                dirs.append(template_dir) 

    return dirs


def get_template(template_dir):
    """Return a template object given a template dir name."""

    path = find_template_path(template_dir)
    file_name = settings.TEMPLATE_FILE_NAME
    file_path = os.path.join(path,file_name)

    template = None
    # If the template_dir is founded path will have a valid value,
    # so the template is loaded, otherwise, a None value is returned
    if path:
        with open(file_path,'r') as file:
            template_raw = file.read()
            template = metadata.Template(template_raw,pattern_name=template_dir)
            
    return template


def get_parallel_file(template_dir):
    """Return a Parallel instance given a template dir name."""

    path = find_template_path(template_dir)
    file_name = settings.PARALLEL_FILE_NAME
    file_path = os.path.join(path,file_name)

    parallel = None
    if path:
        with open(file_path,'r') as file:
            parallel_file_raw = file.read()
            parallel = metadata.Parallel(parallel_file_raw)
    
    return parallel

def get_context_file(template_dir):
    """Return a Context instance given a template dir name."""

    path = find_template_path(template_dir)
    file_name = settings.CONTEXT_FILE_NAME
    file_path = os.path.join(path,file_name)

    context = None
    if path:
        with open(file_path,'r') as file:
            context_str = file.read()
            context = metadata.Context(context_str)

    return context


def get_makefile(template_dir):
    """Return a Makefile instance given a template dir name."""

    path = find_template_path(template_dir)
    file_name = settings.MAKEFILE_FILE_NAME
    file_path = os.path.join(path,file_name)

    makefile = None
    if path:
        with open(file_path,'r') as file:
            makefile_str = file.read()
            makefile = metadata.Makefile(makefile_str)

    return makefile
