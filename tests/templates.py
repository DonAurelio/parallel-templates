# -*- encoding: utf-8 -*-

from parallel_templates import loader
from parallel_templates import settings
from parallel_templates import metadata

import unittest
import os


class TestStencilTemplate(unittest.TestCase):

    def setUp(self):
        self._template_name = 'stencil'

    def test_template_rendering(self):
        template = loader.get_template(self._template_name)
        context = loader.get_context_file(self._template_name)

        source_code = template.render(context)

        self.assertIsInstance(source_code,metadata.SourceCode)

    def test_template_paralel_file_existence(self):
        parallel = loader.get_parallel_file(self._template_name)
        self.assertIsNotNone(parallel)

    def test_template_context_file_existence(self):
        context = loader.get_context_file(self._template_name)
        self.assertIsNotNone(context)

    def test_template_makefile_existence(self):
        makefile = loader.get_makefile(self._template_name)
        self.assertIsNotNone(makefile)


