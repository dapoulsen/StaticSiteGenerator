import os
import shutil

from blocks import markdown_to_html_node

def copy_content_to_directory(source, destination):
    if os.path.exists(destination):
        print(f"Deleting extisting directory: {destination}")
        shutil.rmtree(destination)
    
    os.mkdir(destination)

    for item in os.listdir(source):
        src_path = os.path.join(source, item)
        dst_path = os.path.join(destination, item)

        if os.path.isfile(src_path):
            shutil.copy(src_path, dst_path)
            print(f"Copied file:{src_path} -> {dst_path}")
        else:
            copy_content_to_directory(src_path, dst_path)

def extract_title(markdown):
    header = ''
    lines = markdown.split('\n')
    for line in lines:
        if line.startswith('# '):
            header = line[2:].strip()
            break
    if header == '':
        raise Exception('There is no title in markdown text')
    return header

def generate_page(from_path, template_path, dest_path):
    print(f"Generating page from {from_path} to {dest_path} using {template_path}")
    
    with open(from_path, "r") as f:
        from_file = f.read()
    
    with open(template_path, "r") as f:
        template_file = f.read()
    
    html_node = markdown_to_html_node(from_file)
    html_string = html_node.to_html()

    title = extract_title(from_file)

    final_html = template_file.replace("{{ Title }}", title).replace("{{ Content }}", html_string)

    dir = os.path.dirname(dest_path)
    if dir != "":
        os.makedirs(dir, exist_ok=True)
    with open(dest_path, "w") as f:
        f.write(final_html)
