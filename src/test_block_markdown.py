import unittest

from markdown_blocks import BlockType, block_to_block_type

class TestBlockToBlockType(unittest.TestCase):
    def test_heading_one(self):
        self.assertEqual(block_to_block_type("# Hello"), BlockType.HEADING)

    def test_heading_six(self):
        self.assertEqual(block_to_block_type("###### Hello"), BlockType.HEADING)

    def test_heading_no_space(self):
        self.assertEqual(block_to_block_type("#Hello"), BlockType.PARAGRAPH)

    def test_code(self):
        self.assertEqual(block_to_block_type("```\ncode here```"), BlockType.CODE)

    def test_code_no_endswith(self):
        self.assertEqual(block_to_block_type("```\ncode here"), BlockType.PARAGRAPH)

    def test_quote(self):
        self.assertEqual(block_to_block_type(">line one\n>line two"), BlockType.QUOTE)

    def test_quote_with_space(self):
        self.assertEqual(block_to_block_type("> line one\n> line two"), BlockType. QUOTE)

    def test_quote_missing_gt(self):
        self.assertEqual(block_to_block_type(">line one\nline two"), BlockType.PARAGRAPH)

    def test_unordered_list(self):
        self.assertEqual(block_to_block_type("- item one\n- item two"), BlockType.UNOREDERED_LIST)

    def test_unordered_list_missing_space(self):
        self.assertEqual(block_to_block_type("-item one\n-item two"), BlockType.PARAGRAPH)

    def test_ordered_list(self):
        self.assertEqual(block_to_block_type("1. item one\n2. item two\n3. item three"), BlockType.ORDERED_LIST)

    def test_ordered_list_wrong_increment(self):
        self.assertEqual(block_to_block_type("1. item one\n3. item two"), BlockType.PARAGRAPH)

    def test_ordered_lkist_worng_start(self):
        self.assertEqual(block_to_block_type("2. item one\n3. item two"), BlockType.PARAGRAPH)

    def test_paragraph(self):
        self.assertEqual(block_to_block_type("Hello world"), BlockType.PARAGRAPH)

    
    if __name__ == "__main__":
        unittest.main()
