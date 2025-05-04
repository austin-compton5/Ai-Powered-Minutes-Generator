from jinja2 import Environment, FileSystemLoader


def render_html(path, meeting_dict):
    
    env = Environment(loader=FileSystemLoader(path))
    template = env.get_template("minutes_template.html")

    rendered_html = template.render(meeting=meeting_dict)
    
    return rendered_html