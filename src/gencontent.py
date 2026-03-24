import os

from markdown_blocks import markdown_to_html_node
from htmlnode import HTMLNode

def extract_title(markdown):
    lines = markdown.split("\n")
    for line in lines:
        if line.startswith("# "):
            return line[2:]
        
    raise Exception("no title found")

def generate_page(from_path, template_path, dest_path):
    print("Generating page from from_path to dest_path using template_path")
    
    with open(from_path, "r") as from_file:
       content = from_file.read()
    
    node = markdown_to_html_node(content)
    html = node.to_html()
    
    title = extract_title(content)

    with open(template_path, "r") as template_file:
        template = template_file.read()

    template = template.replace("{{ Title }}", title)
    template = template.replace("{{ Content }}", html)

    dest_dir = os.path.dirname(dest_path)
    if dest_dir != "":
        os.makedirs(dest_dir, exist_ok=True)
    with open(dest_path, "w") as dest_file:
        dest_file.write(template)

    

    
