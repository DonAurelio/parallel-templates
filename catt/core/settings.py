# -*- encoding: utf-8 -*-

import os


# Catt Directory
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Templates Folder Manager Settings
TEMPLATES_DIR = 'templates'
TEMPLATE_DIRS = (
	os.path.join(BASE_DIR,TEMPLATES_DIR),
)

TEMPLATE_FILE_NAME = 'template.c'

# Required for template rendering
from django.conf import settings
settings.configure(TEMPLATE_DIRS=TEMPLATE_DIRS)

# Parallel File Settings
PARALLEL_FILE_NAME = 'parallel.yml'

# Cellular Automata Specification File Settings
CAFILE_NAME = 'cafile.yml'
CAFILE_PATH = os.path.join(BASE_DIR,TEMPLATES_DIR,CAFILE_NAME)
