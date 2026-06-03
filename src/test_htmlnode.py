import unittest

from htmlnode import HTMLNode


class TestHTMLNode(unittest.TestCase):
    def test_props_to_html_single(self):
        node = HTMLNode("a", "Click here", None, {"href": "https://example.com"})
        self.assertEqual(node.props_to_html(), ' href="https://example.com"')

    def test_props_to_html_multiple(self):
        node = HTMLNode("a", "Click here", None, {
            "href": "https://example.com",
            "target": "_blank"
        })
        self.assertIn('href="https://example.com"', node.props_to_html())
        self.assertIn('target="_blank"', node.props_to_html())

    def test_props_to_html_empty(self):
        node = HTMLNode("p", "Hello", None, {})
        self.assertEqual(node.props_to_html(), "")

    def test_props_to_html_none(self):
        node = HTMLNode("p", "Hello")
        self.assertEqual(node.props_to_html(), "")

    def test_props_to_html_starts_with_space(self):
        node = HTMLNode("img", None, None, {"src": "image.png"})
        self.assertTrue(node.props_to_html().startswith(" "))

    def test_repr(self):
        node = HTMLNode("p", "Hello", None, {"class": "text"})
        self.assertIn("p", repr(node))
        self.assertIn("Hello", repr(node))


if __name__ == "__main__":
    unittest.main()