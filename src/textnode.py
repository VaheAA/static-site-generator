from enum import Enum

from htmlnode import LeafNode

class TextType(Enum):
    TEXT_PLAIN = "plain"
    TEXT_BOLD = "bold"
    TEXT_ITALIC = "italic"
    TEXT_CODE = "code"
    TEXT_LINK = 'link'
    TEXT_IMAGE = 'image'


class TextNode:
    def __init__(self, text, text_type, url=None):
        self.text = text
        self.text_type = text_type
        self.url = url

    def __eq__(self, other):
        return self.text == other.text and self.text_type == other.text_type and self.url == other.url

    def __repr__(self):
           return f"TextNode({self.text}, {self.text_type.value}, {self.url})"


def text_node_to_html_node(self):

    if self.text_type == TextType.TEXT_PLAIN:
        return LeafNode(None, self.text)
    elif self.text_type == TextType.TEXT_BOLD:
        return LeafNode("b", self.text)
    elif self.text_type == TextType.TEXT_ITALIC:
        return LeafNode("i", self.text)
    elif self.text_type == TextType.TEXT_CODE:
        return LeafNode("code", self.text)
    elif self.text_node_to_html_node == TextType.TEXT_LINK:
        return LeafNode("a", self.text, {"href": self.url})
    elif self.text_type == TextType.TEXT_IMAGE:
        return LeafNode("img", "", {"src": self.url, "alt": self.text})
