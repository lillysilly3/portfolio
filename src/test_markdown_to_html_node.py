import unittest
from markdown_blocks import markdown_to_html_node

class TestMarkdownToHtmlNode(unittest.TestCase):
    def test_paragraphs(self):
        md = """
This is **bolded** paragraph
text in a p
tag here

This is another paragraph with _italic_ text and `code` here

"""
        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
        "<div><p>This is <b>bolded</b> paragraph text in a p tag here</p><p>This is another paragraph with <i>italic</i> text and <code>code</code> here</p></div>",
        )

    def test_codeblock(self):
        md = """
```
This is text that _should_ remain
the **same** even with inline stuff
```
"""
        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><pre><code>This is text that _should_ remain\nthe **same** even with inline stuff\n</code></pre></div>",
        )

    def test_heading(self):
        md = """
# This is a heading
"""
        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(html, "<div><h1>This is a heading</h1></div>")

    def test_heading_levels(self):
        md = "### Level 3 Heading"
        node = markdown_to_html_node(md)
        self.assertEqual(node.to_html(), "<div><h3>Level 3 Heading</h3></div>")

    def test_ulist(self):
        md = """
- item one
- item two
- item three
"""
        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(html, "<div><ul><li>item one</li><li>item two</li><li>item three</li></ul></div>")

    def test_olist(self):
        md = """
1. item one
2. item two
3. item three
"""
        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(html, "<div><ol><li>item one</li><li>item two</li><li>item three</li></ol></div>")

    def test_quote(self):
        md = """
> This is a first quote
> This is a second quote
"""
        node = markdown_to_html_node(md)
        self.assertEqual(node.to_html(), "<div><blockquote>This is a first quote This is a second quote</blockquote></div>")

    def test_multiple_block_types(self):
        md = """
# Heading

> This is a quote

1. item one
2. item two

```
some code
```
"""
        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertIn("<h1>Heading</h1>", html)
        self.assertIn("<blockquote>This is a quote</blockquote>", html)
        self.assertIn("<ol><li>item one</li><li>item two</li></ol>", html)
        self.assertIn("<pre><code>", html)