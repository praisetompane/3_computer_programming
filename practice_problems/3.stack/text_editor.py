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
        
    def write(self, letter):
        self.undo_stack.push(letter)
        self.document += letter
        self.display()

    def ctrl_z(self):
        self.undo_stack.pop()
        self.redo_stack.push(self.document[-1])
        self.document = self.document[:-1]
        self.display()

    def ctrl_shift_z(self):
        self.document += self.redo_stack.pop()
        self.display()

    def display(self):
        print(self.document)

def main():
    print("Praise typing his body of knowldge")
    word_processor = TextEditor("")
    print("My blank slate")
    word_processor.display()
    word_processor.write("I")
    word_processor.write(" ")
    word_processor.write("k")
    word_processor.write("m")
    word_processor.ctrl_z()
    word_processor.write("n")
    word_processor.write("o")
    word_processor.write("w")
    print("Try undo and redo")
    word_processor.ctrl_z()
    word_processor.ctrl_shift_z()
main()