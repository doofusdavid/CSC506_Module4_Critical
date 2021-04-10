from Node import Node


class Queue:
    def __init__(self):
        self.list = []

    def enqueue(self, new_item):
        # Create a new node to hold the item
        new_node = Node(new_item)

        # Insert as list tail (end of queue)
        self.list.append(new_node)

    def dequeue(self):
        # Return the popped item
        return self.list.pop(0).data

    def __str__(self):
        string = ""
        for node in self.list:
            string = string + str(node.data) + "\n"
            node = node.next
        return string
