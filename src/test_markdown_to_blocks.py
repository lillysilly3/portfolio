import unittest

from markdown_blocks import markdown_to_blocks

class TestMarkdownToBlocks(unittest.TestCase):
    def test_markdown_to_blocks(self):
        md = """
This is **bolded** paragraph

This is another paragraph with _italic_ text and `code` here
This is the same paragraph on a new line

- This is a list
- with items
"""
        blocks = markdown_to_blocks(md)
        self.assertEqual(
            blocks,
            [
                "This is **bolded** paragraph",
                "This is another paragraph with _italic_ text and `code` here\nThis is the same paragraph on a new line",
                "- This is a list\n- with items",
            ],
        )

    def test_excessive_newlines_blocks(self):
        md = """
This is paragraph




This is another paragraph



This is last paragraph
"""
        blocks = markdown_to_blocks(md)
        self.assertEqual(
            blocks,
            [
                "This is paragraph",
                "This is another paragraph",
                "This is last paragraph",    
            ]
        )

    def test_whitespace_blocks(self):
        md = "   This is a paragraph   "
        blocks = markdown_to_blocks(md)
        self.assertEqual(blocks,["This is a paragraph"])

    def test_blank_line_blocks(self):
        md = ""
        blocks = markdown_to_blocks(md)
        self.assertEqual(
            blocks,
            []
        )