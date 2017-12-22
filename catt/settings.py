# -*- encoding: utf-8 -*-

import os


# Catt Directory
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
print(BASE_DIR)

# Templates
TEMPLATES_DIR = 'templates'
TEMPLATE_DIRS = (
	os.path.join(BASE_DIR,TEMPLATES_DIR),
)

TEMPLATE_FILE_NAME = 'template.c'

PARALLEL_FILE_NAME = 'parallel.yml'

# Cellular Automata Specification File Settings
CAFILE_NAME = 'cafile.yml'
CAFILE_DIR = os.path.join(BASE_DIR,TEMPLATES_DIR)
