from Node import Node


class Stack:
    def __init__(self):
        self.list = []

    def push(self, new_item):
        # Create a new node to hold the item
        new_node = Node(new_item)

        # Insert the node as the list head (top of stack)
        self.list.append(new_node)

    def pop(self):
        # Copy data from list's head node (stack's top node)
        return self.list.pop().data

    def __str__(self):
        string = ""
        for node in self.list:
            string = string + str(node.data) + "\n"
            node = node.next
        return string
