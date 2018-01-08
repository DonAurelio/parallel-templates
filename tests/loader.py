# -*- encoding: utf-8 -*-

from parallel_templates import loader
from parallel_templates import settings 

import unittest
import os


class TestLoader(unittest.TestCase):

    def test_find_existing_template_dir(self):
        template_name = 'stencil'
        template_path = loader.find_template_path(template_name)
        real_template_path = os.path.join(settings.BASE_DIR,'templates','stencil')

        # When template is funded the path to the template is returned
        self.assertEqual(real_template_path,template_path)

    def test_find_no_existing_template_dir_1(self):
        template_name = 'other'
        template_path = loader.find_template_path(template_name)

        # When template is not founded '' is returned
        self.assertEqual(template_path,'')

        template_name = ''
        template_path = loader.find_template_path(template_name)

        # When empty template name is provided
        self.assertEqual(template_path,'')

    def test_get_template_dirs(self):

        template_dirs = loader.list_template_dirs()

        template_dirs_path = os.path.join(settings.BASE_DIR,'templates')
        real_template_dirs = os.listdir(template_dirs_path)
        real_template_dirs.remove('README.MD')

        self.assertEqual(real_template_dirs,template_dirs)

    def test_get_existing_template(self):

        # Looking for an existing template
        template_name = 'stencil'
        template = loader.get_template(template_name)

        self.assertIsNotNone(template)

    def test_get_no_existing_template(self):

        # Looking for a non existing template
        template_name = 'other'
        template = loader.get_template(template_name)

        self.assertIsNone(template)

    def test_get_existing_parallel_file(self):

        # Looking for the parallel file of the stencil template
        template_name = 'stencil'
        parallel = loader.get_parallel_file(template_name)

        self.assertIsNotNone(parallel)

    def test_get_no_existing_parallel_file(self):

        # Looking for the parallel file of a non existing template
        template_name = 'other'
        parallel = loader.get_parallel_file(template_name)

        self.assertIsNone(parallel)

    def test_get_existing_context_file(self):

        # Looking for the context file of the stencil template
        template_name = 'stencil'
        context = loader.get_context_file(template_name)

        self.assertIsNotNone(context)

    def test_get_no_existing_context_file(self):

        # Looking for the context file of a non existing template
        template_name = 'other'
        context = loader.get_context_file(template_name)

        self.assertIsNone(context)

    def test_get_existing_makefile(self):

        # Looking for the Makefile file of the stencil template
        template_name = 'stencil'
        makefile = loader.get_makefile(template_name)

        self.assertIsNotNone(makefile)

    def test_get_no_existing_makefile(self):

        # Looking for the Makefile file of a non existing template
        template_name = 'other'
        makefile = loader.get_makefile(template_name)

        self.assertIsNone(makefile)
