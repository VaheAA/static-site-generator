import unittest

from textnode import TextNode, TextType, text_node_to_html_node

class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.TEXT_BOLD)
        node2 = TextNode("This is a text node", TextType.TEXT_BOLD)
        self.assertEqual(node, node2)

    def test_not_eq(self):
        node = TextNode("This is a text node", TextType.TEXT_BOLD)
        node2 = TextNode("This is a link node", TextType.TEXT_LINK, "www.google.com")
        self.assertNotEqual(node, node2)

    def test_node_eq2(self):
        node = TextNode("This is a text node", TextType.TEXT_PLAIN)
        node2 = TextNode("This is a text node2", TextType.TEXT_PLAIN)
        self.assertNotEqual(node, node2)

    def test_eq_link(self):
        node = TextNode("This is a text node", TextType.TEXT_LINK, "https://www.boot.dev")
        node2 = TextNode("This is a text node", TextType.TEXT_LINK, "https://www.boot.dev")
        self.assertEqual(node, node2)

    def test_text(self):
        node = TextNode("This is a text node", TextType.TEXT_PLAIN)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, None)
        self.assertEqual(html_node.value, "This is a text node")

if __name__ == "__main__":
    unittest.main()
