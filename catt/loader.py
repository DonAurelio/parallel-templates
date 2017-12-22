"""
Allows to find files of a determined template and returns a object 
in Python that represents that file.
"""

import os
from . import settings
from . import metadata


def find_template_path(template_name):
    
    template_path = None
    for templates_dir in settings.TEMPLATE_DIRS:
        if template_name in os.listdir(templates_dir):
            template_path = os.path.join(templates_dir,template_name)

    return template_path


def list_template_dirs():


    dirs = []
    for templates_dir in settings.TEMPLATE_DIRS:
        for template_dir in os.listdir(templates_dir):
            path = os.path.join(templates_dir,template_dir)
            if os.path.isdir(path):
                dirs.append(template_dir) 

    return dirs


def get_template(template_dir):


    path = find_template_path(template_dir)
    file_name = settings.TEMPLATE_FILE_NAME
    file_path = os.path.join(path,file_name)

    with open(file_path,'r') as file:
        template_raw = file.read()
        template = metadata.Template(template_raw,pattern_name=template_dir)
        return template


def get_parallel_file(template_dir):

    path = find_template_path(template_dir)
    file_name = settings.PARALLEL_FILE_NAME
    file_path = os.path.join(path,file_name)

    with open(file_path,'r') as file:
        parallel_file_raw = file.read()
        parallel = metadata.Parallel(parallel_file_raw)
        return parallel
