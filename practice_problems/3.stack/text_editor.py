from impl.stack import Stack

'''
    general use case = undo operations
    Performance:
        N = length of item list
        Space = O(2 * N) = O(N)
        write:
            Time = O(1)
        undo:
            Time= O(1)
        redo:
            Time= O(1)
        display:
            Time= O(1)
'''


class TextEditor:
    undo_stack = None
    redo_stack = None
    document = None

    def __init__(self, document):
        self.undo_stack = Stack()
        self.redo_stack = Stack()
        self.document = document

    def write(self, text):
        self.undo_stack.push(text)
        self.document += text
        self.display()

    def undo(self):
        self.redo_stack.push(self.undo_stack.peek())
        last_word = self.undo_stack.pop()
        self.document = self.document[:-len(last_word)]
        self.display()

    def redo(self):
        self.document += self.redo_stack.pop()
        self.display()

    def display(self):
        print(self.document)
