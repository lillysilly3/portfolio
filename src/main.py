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

main()
