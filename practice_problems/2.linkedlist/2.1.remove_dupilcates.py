'''
    Context:
        Given unsorted linked list
    Definitions:

    Objective:
        Remove duplicates
    Assumptions:
        Using singly linked list
    Constraints:
        None
    Example(s):
        input = [1, 2, 4, 6, 1, 6, 8, 5]
        state:[1,2,4,6,8,5]
        
    Algorithm flow:
        empty hash(nodeData -> count)
        foreach element in list
            if exists in hash
                deleteNode
                add element and count = 1
            else
                add element and count = 1
'''
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
    
def remove_duplicates(linkedlist):
    element_frequency = {}
    current_node = linkedlist.head
    while(current_node.next is not None):
        if(current_node.next.data in element_frequency):
            current_node.next = current_node.next.next
            element_frequency[current_node.data] = 1
        else: 
            element_frequency[current_node.data] = 1
            current_node = current_node.next
    
def printlist(linkedlist):
    current_node = linkedlist.head
    while(current_node.next is not None):
        print(current_node.data)
        current_node = current_node.next
    print(current_node.data)

def initialise_linkedlist(numbers, linkedlist):
    previous_node = None
    for n in numbers:
        node = Node(n)
        if linkedlist.head is None: 
            linkedlist.head = node
            previous_node = node
        else: 
            previous_node.next = node
            previous_node = node 
def main():
    linkedlist = LinkedList()
    numbers = [1, 2, 4, 6, 1, 6, 8, 5]
    initialise_linkedlist(numbers, linkedlist)
    print("before delete")
    printlist(linkedlist)
    remove_duplicates(linkedlist)
    print("after delete")
    printlist(linkedlist)

main()

'''
    Performance

        Time = 
            N number of elements 
            D number of operations for delete a node from linkedlist= Constant 
            => O(1 + N) => O(N)
        Space = 
            upto N element's count stored in hash => O(N)
'''

