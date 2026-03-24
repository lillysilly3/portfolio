import unittest

from inline_markdown import text_to_textnodes
from textnode import TextNode, TextType

class TestTextToTextNodes(unittest.TestCase):
    def test_all_markdown_types(self):
        new_nodes = text_to_textnodes("This is **text** with an _italic_ word and a `code block` and an ![obi wan image](https://i.imgur.com/fJRm4Vk.jpeg) and a [link](https://boot.dev)")
        self.assertListEqual(
            [
                TextNode("This is ", TextType.TEXT),
                TextNode("text", TextType.BOLD),
                TextNode(" with an ", TextType.TEXT),
                TextNode("italic", TextType.ITALIC),
                TextNode(" word and a ", TextType.TEXT),
                TextNode("code block", TextType.CODE),
                TextNode(" and an ", TextType.TEXT),
                TextNode("obi wan image", TextType.IMAGE, "https://i.imgur.com/fJRm4Vk.jpeg"),
                TextNode(" and a ", TextType.TEXT),
                TextNode("link", TextType.LINK, "https://boot.dev"),
            ],
            new_nodes,
        )

    def test_no_markdown(self):
        new_nodes = text_to_textnodes("This is a text with no markdown")
        self.assertListEqual([TextNode("This is a text with no markdown", TextType.TEXT)],
                              new_nodes)
        
    def test_image_markdown_only(self):
        new_nodes = text_to_textnodes("This is a text with only an ![obi wan image](https://i.imgur.com/fJRm4Vk.jpeg)")
        self.assertListEqual(
            [
                TextNode("This is a text with only an ", TextType.TEXT),
                TextNode("obi wan image", TextType.IMAGE, "https://i.imgur.com/fJRm4Vk.jpeg"),
            ],
            new_nodes,
        )

    def test_link_markdown_only(self):
        new_nodes = text_to_textnodes("This is a text with only a [link](https://boot.dev)")
        self.assertListEqual(
            [
                TextNode("This is a text with only a ", TextType.TEXT),
                TextNode("link", TextType.LINK, "https://boot.dev"),
            ],
            new_nodes,
        )

    def test_delimiter_markdown(self):
        new_nodes = text_to_textnodes("This is **text** with an _italic_ word and a `code block`")
        self.assertListEqual(
            [
                TextNode("This is ", TextType.TEXT),
                TextNode("text", TextType.BOLD),
                TextNode(" with an ", TextType.TEXT),
                TextNode("italic", TextType.ITALIC),
                TextNode(" word and a ", TextType.TEXT),
                TextNode("code block", TextType.CODE),
            ],
            new_nodes,
        )

if __name__ == "__main__":
    unittest.main()