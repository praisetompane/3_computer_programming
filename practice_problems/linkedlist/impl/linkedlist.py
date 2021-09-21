class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self, numbers=[]):
        self.head = None
        self.initialise_from_array(numbers)

    '''
        O(N)
    '''

    def toString(self):
        if(self.head is None):
            return
        number = ''
        current_node = self.head
        while(current_node is not None):
            number += str(current_node.data)
            current_node = current_node.next
        return number

    '''
        O(N)
    '''

    def toInt(self): 
        if self.head is None: return 0
        else: return int(self.toString())
    '''
        O(N)
    '''

    def add_to_end(self, data):
        new_number = Node(data)
        if self.head is None:
            self.head = new_number
        else:
            current_node = self.head
            while(current_node.next is not None):
                current_node = current_node.next
            current_node.next = new_number

    '''
        O(N)
    '''

    def initialise_from_array(self, numbers):
        for n in numbers:
            self.add(n)

    '''
        O(1)
    '''

    '''
        This actully builds a Stack
            Given 592
            Creates 295
                2 will be head of LinkedList
                The last value added, will be the first one processed
                LIFO => Last In First Out

        Insight: Transformation of any ordered data
                   into a Singly linked list, produces
                        a Stack representation of that data.
                 Because you can only add to the top and remove from the top.
                    Precisrly what a Stack is (Last In(at the top), First Out(from the top))
    '''

    def add(self, data):
        new_number = Node(data)
        if self.head is None:
            self.head = new_number
        else:
            new_number.next = self.head
            self.head = new_number

