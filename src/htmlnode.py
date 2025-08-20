class HTMLNode:
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_self(self):
        raise NotImplementedError("Not implemented yet")

    def props_to_html(self):
        if self.props is None:
            return ""

        output = ""

        for prop in self.props:
            output += f' {prop}="{self.props[prop]}"'

        return output

    def __repr__(self):
        return f"HTMLNode({self.tag}, {self.value}, children: {self.children}, {self.props})"

class LeafNode(HTMLNode):
    def __init__(self, tag, value, props=None):
        super().__init__(tag, value, None, props)

    def to_html(self):
        if self.value is None:
            raise ValueError("All leaf nodes must have a value")

        if self.tag is None:
            return f"{self.value}"

        props = self.props_to_html()

        return f"<{self.tag}{props}>{self.value}</{self.tag}>"

class ParentNode(HTMLNode):
    def __init__(self, tag, children, props=None):
        super().__init__(tag, None, children, props)

    def to_html(self):
        if self.tag is None:
            raise ValueError("Tag is required.")

        if self.children is None:
            raise ValueError("Children are required")

        props = self.props_to_html()
        output = ""

        for child in self.children:
            output += child.to_html()

        return  f"<{self.tag}{props}>{output}</{self.tag}>"
