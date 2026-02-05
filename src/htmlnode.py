class HTMLNode():

    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props
    
    def to_html(self):
        raise NotImplementedError
    
    def props_to_html(self):
        if self.props == None:
            return ""
        else:
            result_string = ""
            for k in self.props:
                result_string += f' {k}="{self.props[k]}"'
            return result_string
    
    def __repr__(self):
        return f'Tag: {self.tag} | Value: {self.value} | Children: {self.children} | Props: {self.props}'
