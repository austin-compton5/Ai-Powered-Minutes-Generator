from jinja2 import Environment, FileSystemLoader


def render_html(templates_dir, template, meeting_dict):
    
    env = Environment(loader=FileSystemLoader(templates_dir))
    template = env.get_template(template)

    rendered_html = template.render(meeting=meeting_dict)
    
    return rendered_html