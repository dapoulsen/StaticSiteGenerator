import re
from textnode import TextType, TextNode

def split_nodes_delimiter(old_nodes, delimiter, text_type):
    result_list = []
    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            result_list.append(node)
            continue

        new_nodes = []
        text_split = node.text.split(delimiter)

        if len(text_split) % 2 == 0:
           raise Exception("Missing closing delimiter")
        
        for i in range(len(text_split)):
            if text_split[i] == "":
                continue
            if i % 2 == 0:
                new_nodes.append(TextNode(text_split[i], TextType.TEXT))
            else:
                new_nodes.append(TextNode(text_split[i], text_type))
    
        result_list.extend(new_nodes)

    return result_list

def extract_markdown_images(text):
    pattern = r"!\[([^\[\]]*)\]\(([^\(\)]*)\)"
    return re.findall(pattern, text)

def extract_markdown_links(text):
    pattern = r"(?<!!)\[([^\[\]]*)\]\(([^\(\)]*)\)"
    return re.findall(pattern, text)