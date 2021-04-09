from LinkedList import LinkedList
from Node import Node


class Stack:
    def __init__(self):
        self.list = LinkedList()

    def push(self, new_item):
        # Create a new node to hold the item
        new_node = Node(new_item)

        # Insert the node as the list head (top of stack)
        self.list.prepend(new_node)

    def pop(self):
        # Copy data from list's head node (stack's top node)
        if self.list.head == None:
            return None
        popped_item = self.list.head.data

        # Remove list head
        self.list.remove_after(None)

        # Return the popped item
        return popped_item

    def __str__(self):
        string = ""
        node = self.list.head
        while node != None:
            string = string + str(node.data) + "\n"
            node = node.next
        return string
