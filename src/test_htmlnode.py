import unittest

from htmlnode import HTMLNode

class TestHTMLNode(unittest.TestCase):
    def test_print(self):
        htmlnode = HTMLNode("p", 'Hello there')
        print(htmlnode)
    
    def test_props_to_html(self):
        node = HTMLNode("a", "IMG", None, {"href": "www.image.com", "target": "_blank",})
        correct = ' href="www.image.com" target="_blank"'
        result = node.props_to_html()
        self.assertEqual(correct, result)
    
    def test_props_to_html_no_props(self):
        node = HTMLNode("a", "IMG")
        result = node.props_to_html()
        self.assertEqual("", result)
    

if __name__ == "__main__":
    unittest.main()