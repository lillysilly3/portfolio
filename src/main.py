import shutil
import os
import sys

from textnode import TextNode, TextType
from copystatic import copy_files_recursive
from gencontent import generate_pages_recursive

def main():
    basepath = "/"
    if len(sys.argv) > 1:
        basepath = sys.argv[1]
    
    node = TextNode("This is some anchor text", TextType.LINK, "https://www.boot.dev")
    print(node)

    if os.path.exists("./docs"):
        shutil.rmtree("./docs")
    copy_files_recursive("./static", "./docs")

    generate_pages_recursive("./content", "template.html", "./docs", basepath)

main()