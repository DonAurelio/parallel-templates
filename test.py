# -*- encoding: utf-8 -*-

import os
import shutil
import pprint


BASE_DIR = os.path.dirname(os.path.realpath(__file__))
TEST_DIR = os.path.join(BASE_DIR,'tests')

if __name__ == '__main__':
    import template
    import metadata

    print('Cellular Automata Template')
    ca_template = template.CATemplate('stencil')
    print(ca_template)

    print('Cellular Automata Source Code')
    cafile = metadata.CAFile.create_file(dir_path=TEST_DIR)
    rendered_file_path = ca_template.render_to_file(cafile=cafile,dir_path=TEST_DIR)
    print('The code was rendered in:', rendered_file_path)
