from htmlnode import HTMLNode

class ParentNode(HTMLNode):
    def __init__(self, tag, children, props=None):
        super().__init__(tag, None, children, props)
    
    def to_html(self):
        if self.tag == None:
            raise ValueError("No tag in ParentNode detected")
        if self.children == None:
            raise ValueError("No children detected")        
        children_html = ''.join(child.to_html() for child in self.children)
        return f'<{self.tag}>{children_html}</{self.tag}>'

