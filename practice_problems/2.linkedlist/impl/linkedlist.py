class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def printlist(self):
        current_node = self.head
        while(current_node.next is not None):
            print(current_node.data)
            current_node = current_node.next
        print(current_node.data)

    def add(self, data):
        print('addding %d to number digits' % (data))
        new_number = Node(data)
        if self.head is None: self.head = new_number
        else:
            current_node = self.head
            while(current_node.next is not None):
                current_node = current_node.next
            current_node.next = new_number
        
    def initialise_from_array(self, numbers):
        previous_node = None
        for n in numbers:
            node = Node(n)
            if self.head is None: 
                self.head = node
                previous_node = node
            else: 
                previous_node.next = node
                previous_node = node 