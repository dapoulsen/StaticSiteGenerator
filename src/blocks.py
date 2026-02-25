from enum import Enum
from htmlnode import HTMLNode
from textnode import TextNode, text_node_to_html_node, TextType
from delimiter import text_to_textnodes
from parentnode import ParentNode
from leafnode import LeafNode

class BlockType(Enum):
    PARAGRAPH = "paragraph"
    HEADING = "heading"
    CODE = "code"
    QUOTE = "quote"
    UNORDERED_LIST = "unordered_list"
    ORDERED_LIST = "ordered_list"

def markdown_to_blocks(markdown):
    result_blocks = []
    blocks = markdown.split("\n\n")
    for block in blocks:
        stripped_block = block.strip()
        if len(block) != 0:
            result_blocks.append(stripped_block)
    return result_blocks

def block_to_block_type(block):
    lines = block.split("\n")
    if block.startswith(('# ', '## ', '### ', '#### ', '##### ', '###### ')):
        return BlockType.HEADING
    if lines[0].startswith('```') and lines[-1].startswith('```') and len(lines) > 1:
        return BlockType.CODE
    if block.startswith(('>', '> ')):
        for line in lines:
            if not line.startswith('>'):
                return BlockType.PARAGRAPH
        return BlockType.QUOTE
    if block.startswith('- '):
        for line in lines:
            if not line.startswith('- '):
                return BlockType.PARAGRAPH
        return BlockType.UNORDERED_LIST
    if block.startswith('1. '):
        i = 1
        for line in lines:
            if not line.startswith(f'{i}. '):
                return BlockType.PARAGRAPH
            i += 1
        return BlockType.ORDERED_LIST
    return BlockType.PARAGRAPH

def markdown_to_html_node(markdown):
    blocks = markdown_to_blocks(markdown)
    children = []
    for block in blocks:
        block_type = block_to_block_type(block)
        html_node = block_to_HTMLNode(block, block_type)
        children.append(html_node)
    
    grandparent_node = ParentNode("div", children)
    return grandparent_node


def block_to_HTMLNode(block, blocktype):
    match blocktype:
        case BlockType.HEADING:
            tag = ""
            value = ""
            if block.startswith('# '):
                tag = "h1"
                value = block[2:]
            elif block.startswith('## '):
                tag = "h2"
                value = block[3:]
            elif block.startswith('### '):
                tag = "h3"
                value = block[4:]
            elif block.startswith('#### '):
                tag = "h4"
                value = block[5:]
            elif block.startswith('##### '):
                tag = "h5"
                value = block[6:]
            elif block.startswith('###### '):
                tag = "h6"
                value = block[7:]
            children = text_to_children(value)
            return ParentNode(tag, children)
        case BlockType.PARAGRAPH:
            value = block.replace("\n", " ")
            children = text_to_children(value)
            return ParentNode("p", children)
        case BlockType.CODE:
            value = block[4:-3]
            node = TextNode(value, TextType.TEXT)
            return ParentNode("pre", [ParentNode("code", [text_node_to_html_node(node)])])
        case BlockType.QUOTE:
            lines = block.split('\n')
            values = [line.lstrip('>').strip() for line in lines]
            joined_lines = " ".join(values)
            children = text_to_children(joined_lines)
            return ParentNode("blockquote", children)
        case BlockType.UNORDERED_LIST:
            values = block.split('\n')
            stripped_lines = [line[2:] for line in values]
            children = list_to_children(stripped_lines)
            return ParentNode("ul", children)
        case BlockType.ORDERED_LIST:
            values = block.split('\n')
            stripped_lines = [line.split(maxsplit=1)[1] for line in values]
            children = list_to_children(stripped_lines)
            return ParentNode("ol", children)
        
def text_to_children(text):
    text_nodes = text_to_textnodes(text)
    html_nodes = []
    for text_node in text_nodes:
        html_nodes.append(text_node_to_html_node(text_node))
    return html_nodes

def list_to_children(text_list):
    children = []
    for line in text_list:
        node = ParentNode("li", text_to_children(line))
        children.append(node)
    return children
