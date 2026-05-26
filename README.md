# Paulina's Portfolio

Personal portfolio website showcasing my projects.

**Live site:** https://lillysilly3.github.io/portfolio/

## Projects Featured

- **Pokedex CLI** - Go command-line app using PokeAPI
- **Journal App** - Python desktop app with mood tracking
- **Asteroids Game** - Classic arcade game with Pygame
- **Static Site Generator** - Python SSG that powers this site

## Built With

Custom static site generator (SSG) built in Python.

## How the SSG Works

┌─────────────┐
│  static/    │──── CSS, images (source)
└──────┬──────┘
       │
       ▼
┌─────────────┐     ┌──────────────┐     ┌─────────┐     ┌─────────────────┐
│  content/   │────>│   main.py    │────>│  docs/  │────>│  GitHub Pages   │
│ (.md files) │     │    (SSG)     │     │(output) │     │    (website)    │
└─────────────┘     └──────────────┘     └─────────┘     └─────────────────┘
                           ▲
                           │
                    ┌──────┴───────┐
                    │ template.html│
                    └──────────────┘

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

## Build

```bash
./build.sh

Author

Paulina