import unittest

from textnode import TextNode, TextType


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)
    
    def test_not_eq(self):
        node1 = TextNode("This is a text node", TextType.BOLD, "www.url.com")
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertNotEqual(node1, node2)
    
    def test_url_none(self):
        node1 = TextNode("This is a next node", TextType.IMAGE, None)
        node2 = TextNode("This is a next node", TextType.IMAGE)
        self.assertEqual(node1, node2)
    
    def test_dif_texttype_not_eq(self):
        node1 = TextNode("This is a text node", TextType.CODE)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertNotEqual(node1, node2)

    def test_text_not_eq(self):
       node1 = TextNode("This is a text node", TextType.BOLD)
       node2 = TextNode("This is a different text node", TextType.BOLD)
       self.assertNotEqual(node1, node2)
        


if __name__ == "__main__":
    unittest.main()
