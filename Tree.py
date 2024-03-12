class Node:
    def __init__(self, value, parent):
        self.value = value
        self.parent = parent
        self.children = []

    def __str__(self):
        output = ""
        output += self.value + " with parent " + self.parent
        output += " with children: \n"
        for child in self.children:
            output += child.value
            output += "   "
        return output


class Tree:
    root = Node("root", "None")
    nodes = list()
    nodes.append(root)

    def insert(self, node):
        for child in self.nodes:
            if child.value == node.parent:
                child.children.append(node)
                self.nodes.append(node)
                return


tree = Tree()
tree.insert(Node("a", "root"))
tree.insert(Node("b", "root"))
tree.insert(Node("c", "root"))
tree.insert(Node("d", "a"))
tree.insert(Node("e", "a"))
tree.insert(Node("f", "b"))
tree.insert(Node("g", "c"))
print(tree.nodes[4])
