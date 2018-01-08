# -*- encoding: utf-8 -*-

"""
This module contains constants definitions, like the location
of the parallel programming templates directory, etc.
"""

import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
"""str: Paralel templates projet base dir path.
"""

TEMPLATES_DIR = 'templates'
"""str: Name of the parallel programming template dir.
"""

TEMPLATE_DIRS = (os.path.join(BASE_DIR,TEMPLATES_DIR),)
"""List[str]: Location parallel programming templates directory.
"""

TEMPLATE_FILE_NAME = 'template.c'
"""str: template file name.
"""

PARALLEL_FILE_NAME = 'parallel.yml'
"""str: parallel file name.
"""

CONTEXT_FILE_NAME = 'context.yml'
"""str: context file name.
"""

MAKEFILE_FILE_NAME = 'Makefile'
"""str: Makefile file name.
"""
