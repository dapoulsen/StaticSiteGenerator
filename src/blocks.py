from enum import Enum
from htmlnode import HTMLNode

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
    for block in blocks:
        block_type = block_to_block_type(block)
        html_node = block_to_HTMLNode(block, block_type)


def block_to_HTMLNode(block, blocktype):
    match blocktype:
        case BlockType.HEADING:
            tag = ""
            value = ""
            if block.startswith('# '):
                tag = "h1"
                value = block.strip(block[2:])
            elif block.startswith('## '):
                tag = "h2"
                value = block.strip(block[3:])
            elif block.startswith('### '):
                tag = "h3"
                value = block.strip(block[4:])
            elif block.startswith('#### '):
                tag = "h4"
                value = block.strip(block[5:])
            elif block.startswith('##### '):
                tag = "h5"
                value = block.strip(block[6:])
            elif block.startswith('###### '):
                tag = "h6"
                value = block.strip(block[7:])
            return HTMLNode(tag, value)
        case BlockType.PARAGRAPH:
            value = block.replace("\n", " ")
            return HTMLNode("p", value)
        case BlockType.CODE:
            value = block.strip('```')
            return HTMLNode("code", value)
        case BlockType.QUOTE:
            value = block.strip('>')
            return HTMLNode("blockquote", value)
        case BlockType.UNORDERED_LIST:
            value = block.strip('- ')
            return HTMLNode("ul", value)
        case BlockType.ORDERED_LIST:
            value = block.strip('.')
            return HTMLNode("ol", value)