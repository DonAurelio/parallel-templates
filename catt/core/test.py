from . import manager


if __name__ == '__main__':
    template_manager = manager.TemplateManager()
    template_name = 'stencil'
    cafile_context = {
      "generations": 0,
      "lattice": {
        "neighborhood": {},
        "rowdim": 1000,
        "type": "int",
        "coldim": 1000
      },
      "pattern_name": "stencil"
    }

    raw_source_code = template_manager.get_rendered_template(template_name,cafile_context)

    print('Rendered Source Code.')
    print(raw_source_code)