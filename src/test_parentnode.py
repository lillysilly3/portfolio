import unittest

from htmlnode import ParentNode, LeafNode


class TestParentNode(unittest.TestCase):
    def test_to_html_single_child(self):
        node = ParentNode("div", [LeafNode("p", "Hello")])
        self.assertEqual(node.to_html(), "<div><p>Hello</p></div>")

    def test_to_html_multiple_children(self):
        node = ParentNode("div", [
            LeafNode("p", "Hello"),
            LeafNode("p", "World"),
        ])
        self.assertEqual(node.to_html(), "<div><p>Hello</p><p>World</p></div>")

    def test_to_html_nested_parent(self):
        node = ParentNode("div", [
            ParentNode("p", [
                LeafNode("b", "Hello")
            ])
        ])
        self.assertEqual(node.to_html(), "<div><p><b>Hello</b></p></div>")

    def test_to_html_with_props(self):
        node = ParentNode("div", [LeafNode("p", "Hello")], {"class": "container"})
        self.assertIn('class="container"', node.to_html())

    def test_no_tag_raises_error(self):
        node = ParentNode(None, [LeafNode("p", "Hello")])
        with self.assertRaises(ValueError):
            node.to_html()

    def test_no_children_raises_error(self):
        node = ParentNode("div", [])
        with self.assertRaises(ValueError):
            node.to_html()

    def test_deeply_nested(self):
        node = ParentNode("div", [
            ParentNode("p", [
                ParentNode("span", [
                    LeafNode("b", "Hello")
                ])
            ])
        ])
        self.assertEqual(node.to_html(), "<div><p><span><b>Hello</b></span></p></div>")


if __name__ == "__main__":
    unittest.main()