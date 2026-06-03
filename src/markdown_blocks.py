import re

from enum import Enum
from htmlnode import ParentNode, LeafNode
from inline_markdown import text_to_textnodes
from textnode import text_node_to_html_node, TextType, TextNode

def markdown_to_blocks(markdown):
    modified_blocks = []
    blocks = markdown.split("\n\n")
    for block in blocks:
        if block != "":
            modified_blocks.append(block.strip())

    return modified_blocks

class BlockType(Enum):
    PARAGRAPH = "paragraph"
    HEADING = "heading"
    CODE = "code"
    QUOTE = "quote"
    UNOREDERED_LIST = "unordered_list"
    ORDERED_LIST = "ordered_list"

def block_to_block_type(block):
    if re.match(r"^#{1,6} ", block):
        return BlockType.HEADING
    
    if block.startswith("```\n") and block.endswith("```"):
        return BlockType.CODE
    
    if all(line.startswith(">") for line in block.split("\n")):
        return BlockType.QUOTE
    
    if all(line.startswith("- ") for line in block.split("\n")):
        return BlockType.UNOREDERED_LIST
    
    lines = block.split("\n")
    if all(line.startswith(f"{i + 1}. ") for i, line in enumerate(lines)):
        return BlockType.ORDERED_LIST
    
    return BlockType.PARAGRAPH
        
    
def markdown_to_html_node(markdown):
    blocks = markdown_to_blocks(markdown)
    children = []
    for block in blocks:
        html_node = block_to_html_node(block)
        children.append(html_node)
    return ParentNode("div", children)

def text_to_children(text):
    textNodes = text_to_textnodes(text)
    children = []
    for node in textNodes:
        html_node = text_node_to_html_node(node)
        children.append(html_node)
    return children

def paragraph_to_html_node(block):
    lines = block.split("\n")
    paragraph = " ".join(lines)
    children = text_to_children(paragraph)
    return ParentNode("p", children)

def heading_to_html_node(block):
    n = block.lstrip("#")
    level = len(block) - len(n)
    clean = n[1:]
    children = text_to_children(clean)
    return ParentNode(f"h{level}", children)

def quote_to_html_node(block):
    lines = []
    for line in block.split("\n"):
        lines.append(line.lstrip("> "))
    children = text_to_children(" ".join(lines))
    return ParentNode("blockquote", children)

def code_to_html_node(block):
    text = block[4:-3]
    node = TextNode(text, TextType.TEXT)
    child = text_node_to_html_node(node)
    return ParentNode("pre", [ParentNode("code", [child])])

def ulist_to_html_node(block):
    items = []
    for line in block.split("\n"):
        children = text_to_children(line.lstrip("- "))
        items.append(ParentNode("li", children))
    return ParentNode("ul", items)

def olist_to_html_node(block):
    items = []
    for line in block.split("\n"):
        children = text_to_children(line.split(". ", 1)[1])
        items.append(ParentNode("li", children))
    return ParentNode("ol", items)


def block_to_html_node(block):
    block_type = block_to_block_type(block)
    if block_type == BlockType.PARAGRAPH:
        return paragraph_to_html_node(block)
    if block_type == BlockType.HEADING:
        return heading_to_html_node(block)
    if block_type == BlockType.QUOTE:
        return quote_to_html_node(block)
    if block_type == BlockType.CODE:
        return code_to_html_node(block)
    if block_type == BlockType.UNOREDERED_LIST:
        return ulist_to_html_node(block)
    if block_type == BlockType.ORDERED_LIST:
        return olist_to_html_node(block)
    
    