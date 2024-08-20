import os
import shutil
from markdown_blocks import markdown_to_html_node, extract_title

def clear_directory(directory):
    if os.path.exists(directory):
        shutil.rmtree(directory)
    os.makedirs(directory)

def copy_static(src, dest):
    if not os.path.exists(dest):
        os.makedirs(dest)
    
    for item in os.listdir(src):
        src_path = os.path.join(src, item)
        dest_path = os.path.join(dest, item)
        
        if os.path.isdir(src_path):
            # Recursively copy directory
            copy_static(src_path, dest_path)
        elif os.path.isfile(src_path):
            # Copy file
            shutil.copy(src_path, dest_path)
            print(f"Copied file: {src_path} -> {dest_path}")


def generate_pages_recursive(dir_path_content, template_path, dest_dir_path):
    for root, _, files in os.walk(dir_path_content):
        for file in files:
            if file.endswith('.md'):
                from_path = os.path.join(root, file)
                relative_path = os.path.relpath(from_path, dir_path_content)
                dest_path = os.path.join(dest_dir_path, os.path.splitext(relative_path)[0] + '.html')

                print(f"Generating page from {from_path} to {dest_path} using {template_path}")

                with open(from_path, 'r') as f:
                    markdown_content = f.read()

                with open(template_path, 'r') as f:
                    template_content = f.read()

                html_node = markdown_to_html_node(markdown_content)
                html_content = html_node.to_html()

                title = extract_title(markdown_content)

                final_html = template_content.replace("{{ Title }}", title).replace("{{ Content }}", html_content)

                os.makedirs(os.path.dirname(dest_path), exist_ok=True)
                with open(dest_path, 'w') as f:
                    f.write(final_html)

def main():
    src_dir = 'static'
    dest_dir = 'public'
    
    # Clear destination directory
    clear_directory(dest_dir)
    
    # Copy static content
    copy_static(src_dir, dest_dir)
    generate_pages_recursive('content', 'template.html', 'public')

if __name__ == "__main__":
    main()