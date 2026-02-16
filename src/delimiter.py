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

def split_nodes_image(old_nodes):
    result_list = []
    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            result_list.append(node)
            continue
        original_text = node.text
        extracted_image_text = extract_markdown_images(original_text)
        if len(extracted_image_text) == 0:
            result_list.append(node)
            continue

        for tuple in extracted_image_text:
            sections = original_text.split(f"![{tuple[0]}]({tuple[1]})", 1)
            if len(sections) != 2:
                raise ValueError("wrong markdown, image is missing closing")
            if sections[0] != "":
                result_list.append(TextNode(sections[0], TextType.TEXT))
            result_list.append(TextNode(tuple[0], TextType.IMAGE, tuple[1]))
        
            original_text = sections[1]
        
        if original_text != "":
            result_list.append(TextNode(original_text, TextType.TEXT))
    return result_list

def split_nodes_link(old_nodes):
    new_nodes = []
    for old_node in old_nodes:
        if old_node.text_type != TextType.TEXT:
            new_nodes.append(old_node)
            continue
        original_text = old_node.text
        links = extract_markdown_links(original_text)
        if len(links) == 0:
            new_nodes.append(old_node)
            continue
        for link in links:
            sections = original_text.split(f"[{link[0]}]({link[1]})", 1)
            if len(sections) != 2:
                raise ValueError("invalid markdown, link section not closed")
            if sections[0] != "":
                new_nodes.append(TextNode(sections[0], TextType.TEXT))
            new_nodes.append(TextNode(link[0], TextType.LINK, link[1]))
            original_text = sections[1]
        if original_text != "":
            new_nodes.append(TextNode(original_text, TextType.TEXT))
    return new_nodes
        
def text_to_textnodes(text):
    nodes = [TextNode(text, TextType.TEXT)]
    nodes = split_nodes_delimiter(nodes, "**", TextType.BOLD)
    nodes = split_nodes_delimiter(nodes, "_", TextType.ITALIC)
    nodes = split_nodes_delimiter(nodes, "`", TextType.CODE)
    nodes = split_nodes_image(nodes)
    nodes = split_nodes_link(nodes)
    return nodes
    