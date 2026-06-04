# Static Site Generator

A custom static site generator built in Python that powers this portfolio website.

## How It Works

static/       → copied to docs/ (CSS, images)
content/*.md  → converted to HTML → docs/
template.html → wraps the HTML content
docs/         → served by GitHub Pages

![SSG sceme](/images/ssg.png)

## Supported Markdown Features

**Block elements:** Headings, paragraphs, code blocks, block quotes, ordered and unordered lists

**Inline elements:** Bold, italic, inline code, links, images and linked images

## Tech Stack

- Python
- Custom Markdown parser
- HTML node generation
- Recursive file processing

## Features

- Converts Markdown to HTML
- Copies static assets (CSS, images)
- Uses template for consistent styling
- Generates full site with one command


[Full project on GitHub](https://github.com/lillysilly3/portfolio)

[← Back to Portfolio](/)
