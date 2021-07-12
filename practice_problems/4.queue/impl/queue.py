class Node:
    data = None
    next = None

    def __init__(self, data):
        self.data = data


class Queue:
    first = None
    last = None
    # O(1)
    def add(self, item):
        node = Node(item)
        if(self.first is None):
            self.first = node
            self.last = self.first
        else:
            self.last.next = node
            self.last = node
    # O(1)

    def remove(self):
        if(self.first is None):
            raise Exception("Queue is empty")
        else:
            item = self.first.data
            self.first = self.first.next
            if(self.first is None):
                self.last = None
            return item
    # O(1)

    def peek(self):
        if(self.first is None):
            raise Exception("Queue is empty")
        else:
            return self.first.data
    # O(1)

    def is_empty(self):
        return self.first is None

    def __str__(self):
        current = self.first
        queue = ''
        if(self.first is None):
            return 'queue is empty'
        else:
            while(current.next is not None):
                queue += str(current.data) + "->"
                current = current.next
            queue += str(current.data)
        return queue


def main():
    print('Can create queue')
    teller_service_queue = Queue()
    print(teller_service_queue)

    print('Can add to queue')
    teller_service_queue.add(1)
    print(teller_service_queue)

    print('Can check what is next is queue')
    print(teller_service_queue.peek())

    print('Can remove next item in queue')
    print(teller_service_queue.remove())
    print(teller_service_queue)

    print('Can check if it is empty')
    print(teller_service_queue.is_empty())
 
    print("Can add more")
    teller_service_queue.add(2)
    teller_service_queue.add(3)
    print(teller_service_queue)



if __name__ == '__main__':
    main()
