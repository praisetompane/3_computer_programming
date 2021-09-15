class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self, numbers = []):
        self.head = None
        self.initialise_from_array(numbers)

    def printlist(self):
        print('')
        if(self.head is None): return
        number = ''
        current_node = self.head
        while(current_node is not None):
            number += str(current_node.data)
            current_node = current_node.next
        print(number)

    def add(self, data):
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