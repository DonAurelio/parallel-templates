# -*- encoding: utf-8 -*-

from parallel_templates import loader
from parallel_templates import settings 
from . import data

import unittest
import os


class TestLoader(unittest.TestCase):

    def test_find_template_path(self):
        template_name = 'stencil'
        template_path = loader.find_template_path(template_name)
        real_template_path = os.path.join(settings.BASE_DIR,'templates','stencil')

        # When template is funded the path to the template is returned
        self.assertEqual(real_template_path,template_path)

        template_name = 'other'
        template_path = loader.find_template_path(template_name)

        # When template is not founded '' is returned
        self.assertEqual(template_path,'')

        template_name = ''
        template_path = loader.find_template_path(template_name)

        # When empty template name is provided
        self.assertEqual(template_path,'')

    def test_template_dirs(self):

        template_dirs = loader.list_template_dirs()

        template_dirs_path = os.path.join(settings.BASE_DIR,'templates')
        real_template_dirs = os.listdir(template_dirs_path)
        real_template_dirs.remove('README.MD')

        self.assertEqual(real_template_dirs,template_dirs)

    def test_get_template(self):

        # Looking for an existing template
        template_name = 'stencil'
        template = loader.get_template(template_name)

        self.assertIsNotNone(template)

        # Looking for a non existing template
        template_name = 'other'
        template = loader.get_template(template_name)

        self.assertIsNone(template)