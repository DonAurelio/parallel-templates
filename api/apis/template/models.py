from flask_restplus import  fields


RAW_CAFILE = """
# The fields described here are mandatory to serve as a context
# to a cellular automata template.c
pattern_name: stencil
lattice: 
  rowdim: 20
  coldim: 20
  type: bool
  neighborhood:
    up: [-1,1]
    down: [1,1]
    left: [1,1]
    right: [-1,-1]
generations: 20
"""

cafile_model = {
    'name': fields.String(
        required=True,
        default='cafile.yml',
        description="name of file"
    ),
    'ftype': fields.String(
        required=True,
        default='yml',
        description="file type"
    ),
    'text': fields.String(
        required=True,
        default=RAW_CAFILE,
        description="Cellular automata specification"
    ),
}