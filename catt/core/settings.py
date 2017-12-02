# -*- encoding: utf-8 -*-

import os


# Catt Directory
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Templates Folder Manager Settings
# Register your templates here

TEMPLATE_DIRS = (
	os.path.join(BASE_DIR,'templates'),
)

TEMPLATE_FILE_NAME = 'template.c'

# # Cellular Automata Specification File Settings
# CAFILE_NAME = 'cafile.yml'
# CAFILE_PATH = os.path.join(BASE_DIR,TEMPLATES_DIR,CAFILE_NAME)
