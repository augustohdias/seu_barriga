def read_md_template(path, template_name, params={}):
    template_str = open(f'{path}/messages/{template_name}.md', 'r').read()
    for param in params:
        template_str = template_str.replace(f'<{param}>', params[param])
    return template_str