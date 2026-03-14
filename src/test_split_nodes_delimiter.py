import unittest

from inline_markdown import split_nodes_delimiter
from textnode import TextNode, TextType

class TestSplitNodesDelimiter(unittest.TestCase):
    def test_bold_delimiter(self):
        node = TextNode("Hello **world** today", TextType.TEXT)
        result = split_nodes_delimiter([node], "**", TextType.BOLD)
        self.assertEqual(result, [
            TextNode("Hello ", TextType.TEXT),
            TextNode("world", TextType.BOLD),
            TextNode(" today", TextType.TEXT),
        ])
    
    def test_code_delimiter(self):
        node = TextNode(("Hello 'code' world"), TextType.TEXT)
        result = split_nodes_delimiter([node], "'", TextType.CODE)
        self.assertEqual(result, [
            TextNode("Hello ", TextType.TEXT),
            TextNode("code", TextType.CODE),
            TextNode(" world", TextType.TEXT),
        ])

    def  test_not_textType_text(self):
        node = TextNode(("Hello world"), TextType.BOLD)
        result = split_nodes_delimiter([node], "**", TextType.BOLD)
        self.assertEqual(result, [TextNode("Hello world", TextType.BOLD)])

    def test_invalid_markdown(self):
        node = TextNode(("Hello **world"), TextType.TEXT)
        with self.assertRaises(Exception):
            split_nodes_delimiter([node], "**", TextType.BOLD)

    def test_no_delimiter(self):
        node = TextNode(("Hello world"), TextType.TEXT)
        result = split_nodes_delimiter([node], "**", TextType.TEXT)
        self.assertEqual(result, [TextNode("Hello world", TextType.TEXT)])

    def test_italic_delimiter(self):
        node = TextNode(("Hello _world_ today"), TextType.TEXT)
        result = split_nodes_delimiter([node], "_", TextType.ITALIC)
        self.assertEqual(result, [
            TextNode("Hello ", TextType.TEXT),
            TextNode("world", TextType.ITALIC),
            TextNode(" today", TextType.TEXT),
        ])