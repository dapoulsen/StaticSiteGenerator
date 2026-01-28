from textnode import TextNode, TextType

def main():

    textNode = TextNode("This is some bold text", TextType.BOLD_TEXT)
    imageNode = TextNode("This is an image", TextType.IMAGE, "www.nicepic.com")

    print(textNode)
    print(imageNode)

if __name__ == "__main__":
    main()
    
