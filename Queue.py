from LinkedList import LinkedList
from Node import Node


class Queue:
    def __init__(self):
        self.list = LinkedList()

    def enqueue(self, new_item):
        # Create a new node to hold the item
        new_node = Node(new_item)

        # Insert as list tail (end of queue)
        self.list.append(new_node)

    def dequeue(self):
        # Copy data from list's head node (queue's top node)
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
