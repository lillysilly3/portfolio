# Paulina's Portfolio

Personal portfolio website showcasing my projects build in Python.

**Live site:** https://lillysilly3.github.io/portfolio/

## Projects Featured

- **Pokedex CLI** - Go command-line app using PokeAPI
- **Journal App** - Python desktop app with mood tracking
- **Asteroids Game** - Classic arcade game with Pygame
- **Static Site Generator** - Python SSG that powers this site

## How the SSG Works

![SSG sceme](/images/ssg.png)

1. `static/` → copied to `docs/` (CSS, images)
2. `content/*.md` → converted to HTML using `template.html` → saved to `docs/`
3. `docs/` → served by GitHub Pages

## Supported Markdown Features

**Block elements:** Headings, paragraphs, code blocks, block quotes, ordered and unordered lists

**Inline elements:** Bold (`**`), italic (`_`), inline code, links, and images

## Project Structure

- `src/` - Static site generator Python code
- `content/` - Markdown source files
- `static/` - CSS and images
- `docs/` - Generated site (served by GitHub Pages)
- `template.html` - HTML wrapper template

## What I Learned

- **Static Site Generation** - How to convert Markdown to HTML and build a complete site from source files
- **Python** - Regex parsing, recursive file processing, HTML node generation
- **Markdown Parsing** - Handling inline elements (bold, italic, links, images) and block elements (headings, lists, code blocks)
- **CSS** - Responsive styling, flexbox layouts, hover effects
- **Git & GitHub Pages** - Version control and deploying static sites
- **Problem Solving** - Adding features like linked image support to handle `[![alt](img)](link)` syntax

## Build

```bash
./build.sh
```

## Acknowledgments

This project was built as part of the [Boot.dev](https://boot.dev) curriculum.