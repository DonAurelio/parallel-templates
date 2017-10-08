# -*- encoding: utf-8 -*-

import os

# Project Directory
BASE_DIR = os.path.dirname(os.path.realpath(__file__))

# Django Templates Engine Settings
TEMPLATES_DIR = 'templates'
TEMPLATE_DIRS = ( 
    os.path.join(BASE_DIR,TEMPLATES_DIR), 
    os.path.join(BASE_DIR,TEMPLATES_DIR,'stencil'), 
)
TEMPLATE_NAME = 'template.c'

from django.conf import settings
settings.configure(TEMPLATE_DIRS=TEMPLATE_DIRS)

# Cellular Automata Specification File Settings
CAFILE_NAME = 'cafile.yml'
CAFILE_PATH = os.path.join(BASE_DIR,TEMPLATES_DIR,CAFILE_NAME)
