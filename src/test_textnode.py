import unittest

from textnode import TextNode, TextType, text_node_to_html_node
from htmlnode import LeafNode


class TestTextNode(unittest.TestCase):
    # TextNode
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)

    def test_eq_with_url(self):
        node = TextNode("Click here", TextType.LINK, "https://example.com")
        node2 = TextNode("Click here", TextType.LINK, "https://example.com")
        self.assertEqual(node, node2)
 
    def test_url_defaults_to_none(self):
        node = TextNode("Hello", TextType.TEXT)
        self.assertIsNone(node.url)
 
    def test_not_equal_different_text(self):
        node = TextNode("Hello", TextType.BOLD)
        node2 = TextNode("World", TextType.BOLD)
        self.assertNotEqual(node, node2)
 
    def test_not_equal_different_text_type(self):
        node = TextNode("Hello", TextType.BOLD)
        node2 = TextNode("Hello", TextType.ITALIC)
        self.assertNotEqual(node, node2)
 
    def test_not_equal_different_url(self):
        node = TextNode("Click", TextType.LINK, "https://example.com")
        node2 = TextNode("Click", TextType.LINK, "https://other.com")
        self.assertNotEqual(node, node2)
 
    def test_not_equal_url_vs_none(self):
        node = TextNode("Click", TextType.LINK, "https://example.com")
        node2 = TextNode("Click", TextType.LINK)
        self.assertNotEqual(node, node2)

    # tests for text_node_to_html_node
    def test_text(self):
        node = TextNode("Hello", TextType.TEXT)
        html = text_node_to_html_node(node)
        self.assertEqual(html.to_html(), "Hello")

    def test_bold(self):
        node = TextNode("Hello", TextType.BOLD)
        html = text_node_to_html_node(node)
        self.assertEqual(html.to_html(), "<b>Hello</b>")

    def test_italic(self):
        node = TextNode("Hello", TextType.ITALIC)
        html = text_node_to_html_node(node)   
        self.assertEqual(html.to_html(), "<i>Hello</i>")

    def test_code(self):
        node = TextNode("print('hi')", TextType.CODE)
        html = text_node_to_html_node(node)
        self.assertEqual(html.to_html(), "<code>print('hi')</code>")

    def test_link(self):
        node = TextNode("Click here", TextType.LINK, "https://example.com")
        html = text_node_to_html_node(node)
        self.assertEqual(html.to_html(), '<a href="https://example.com">Click here</a>')

    def test_image(self):
        node = TextNode("My image", TextType.IMAGE, "https://example.com/img.png")
        html = text_node_to_html_node(node)
        self.assertIn('src="https://example.com/img.png"', html.to_html())
        self.assertIn('alt="My image"', html.to_html())

    def test_invalid_type_raises_error(self):
        node = TextNode("Hello", None)
        with self.assertRaises(Exception):
            text_node_to_html_node(node)

if __name__ == "__main__":
    unittest.main()