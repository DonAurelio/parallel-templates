# -*- encoding: utf-8 -*-

import sys
from pprint import pprint

# To include the pragcc module in the python path
sys.path[0:0] = ['.', '..']

from catt.core import metadata
from . import data

def template_obj_creation():
    template = metadata.Template(data.RAW_COMPLEX_TEMPLATE,'stencil')
    print('Template Name: ',template.pattern_name)    
    pprint(template.source)

    return template


def cafile_obj_creation():
    cafile = metadata.Cafile(data.RAW_CAFILE)
    print('Cafile Source')
    pprint(cafile.source)
    print('Cafile data')
    pprint(cafile.data)

    return cafile


def template_renderization():
    template = template_obj_creation()
    cafile =  cafile_obj_creation()

    rendered = template.render(cafile)

    print('Template Renderization')
    print(rendered)

if __name__ == '__main__':

    template_obj_creation()
    cafile_obj_creation()
    template_renderization()



    
