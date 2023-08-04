from jinja2 import Environment, FileSystemLoader
import yaml

def generate_page(page_data):
    # Configure Jinja environment
    env = Environment(loader=FileSystemLoader('.'))
    template = env.get_template('dashboard_template.html')

    # Render the template with the data and write it to a file
    rendered_html = template.render(data=page_data, pages_data=pages_data)
    filename = './site/' + template_name.split('.')[0] + '.html'
    with open(filename, 'w') as file:
        file.write(rendered_html)

if __name__ == '__main__':
    # Load the YAML data
    with open('inventory.yml', 'r') as file:
        pages_data = yaml.safe_load(file)

    # Generate the navigation bar
    env = Environment(loader=FileSystemLoader('.'))
    navbar_template = env.get_template('navbar_template.html')
    rendered_navbar = navbar_template.render(pages_data=pages_data)
    with open('navbar.html', 'w') as file:
        file.write(rendered_navbar)

    # Loop through each page and generate the corresponding HTML file
    for template_name, data in pages_data.items():
        generate_page(data)