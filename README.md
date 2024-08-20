# Static-Site-Generator
# Markdown to Static HTML Site Generator

This project is a static site generator that converts markdown files into HTML pages using a specified HTML template. The generator recursively processes markdown files from a content directory and outputs HTML files into a public directory while maintaining the directory structure.

## Features

- Converts markdown files to HTML using a predefined HTML template.
- Automatically generates HTML for each markdown file found in the content directory.
- Preserves the directory structure of the content directory in the output.
- Supports common markdown features such as headings, paragraphs, lists, code blocks, and blockquotes.
- Includes a simple local server setup for previewing the generated site.

## Project Structure
project-root/
├── content/
│ ├── index.md
│ └── majesty/
│ └── index.md
├── public/ (generated files will go here)
├── src/
│ ├── main.py
│ ├── markdown_blocks.py
│ └── markdown_utils.py
├── static/
│ ├── images/
│ │ └── rivendell.png
│ └── index.css
├── template.html
└── main.sh



## Getting Started

### Prerequisites

- Python 3.x installed on your system.

### Setup and Usage

1. **Clone the repository:**
   ```bash
   git clone <repository-url>
   cd <repository-directory>
Place your markdown content:
Add markdown files to the content/ directory. Ensure each file ends with .md.
Prepare your HTML template:
Customize the template.html file in the root directory. Use {{ Title }} for the page title and {{ Content }} for the main content area.
Generate the site:
Run the main.sh script to convert markdown files to HTML and serve the site locally.

./main.sh
View the site:
Open your web browser and navigate to http://localhost:8888 to view the generated site.
How It Works
Markdown Parsing: The project uses a custom markdown parser defined in markdown_blocks.py to convert markdown into HTML nodes.
HTML Generation: The generate_pages_recursive function in main.py traverses the content/ directory, processes each markdown file, and outputs HTML files in the public/ directory.
Template Rendering: The HTML content is injected into the template.html file, replacing the {{ Title }} and {{ Content }} placeholders.
Local Server: A simple Python HTTP server is used to serve the generated HTML files for local preview.