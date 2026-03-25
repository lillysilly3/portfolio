import shutil
import os

from textnode import TextNode, TextType
from copystatic import copy_files_recursive
from gencontent import generate_page

def main():
    node = TextNode("This is some anchor text", TextType.LINK, "https://www.boot.dev")
    print(node)

    if os.path.exists("./public"):
        shutil.rmtree("./public")
    copy_files_recursive("./static", "./public")

    generate_page("content/index.md", "template.html", "public/index.html")

    for root, dirs, files in os.walk("./content"):
        for file in files:
            if file.endswith(".md"):
                from_path = os.path.join(root, file)
                dest_path = from_path.replace("./content", "./public").replace(".md", ".html")
                generate_page(from_path, "template.html", dest_path)

main()
