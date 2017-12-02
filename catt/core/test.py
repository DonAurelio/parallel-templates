# -*- encoding: utf-8 -*-

import os
import shutil
import pprint


BASE_DIR = os.path.dirname(os.path.realpath(__file__))
TEST_DIR = os.path.join(BASE_DIR,'tests')

if __name__ == '__main__':
    # from . import template
    # from . import metadata
    from . import manager

    if not os.path.exists(TEST_DIR):
        os.mkdir(TEST_DIR)

    print('CATT Available Templates')
    template_manager = manager.TemplateFolderManager()
    available_templates_list = template_manager.list_available_templates()
    print(available_templates_list)

    print('CATT Get a Template')
    template = template_manager.get_template('stencil')
    print(template)

    print('CATT Get Template Info')
    info = template_manager.get_template_info('stencil')
    print(info)


    # print('Cellular Automata Template Metadata')
    # cafile = metadata.CAFile.create_file(dir_path=TEST_DIR)
    # print('* cafile metadata')
    # pprint.pprint(cafile.data)

    # print('Cellular Automata Template')
    # ca_template = template.CATemplate(cafile)

    # print('* template raw text')
    # print(ca_template)

    # print('* rendered template')
    # rendered_file_path = ca_template.render_to_file(dir_path=TEST_DIR)
    # print('The code was rendered in:', rendered_file_path)

    if os.path.exists(TEST_DIR):
        shutil.rmtree(TEST_DIR)

