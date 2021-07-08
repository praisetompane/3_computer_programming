from impl.stack import Stack

'''
    general use case: symmetry test
    Performance:
        N = length of document
        Time = O(N)
        Space = O(N)
'''

class BracketsLinter():
    document = None
    opening_parathesis = None
    opening_curly = '{'
    opening_round = '('
    opening_square = '['
    def __init__(self):
        self.opening_parathesis = Stack()

    def lint(self, document):
        for char in document:
            if(char == self.opening_round or char == self.opening_curly or char == self.opening_square):
                self.opening_parathesis.push(char)
            if(char == '}' and self.opening_parathesis.peek() == self.opening_curly):
                self.opening_parathesis.pop()
            if(char == ']' and self.opening_parathesis.peek() == self.opening_square):
                self.opening_parathesis.pop()
            if(char == ')' and self.opening_parathesis.peek() == self.opening_round):
                self.opening_parathesis.pop()

        return self.opening_parathesis.is_empty() 


def main():
    c_linter = BracketsLinter()
    valid_code = '''
                    public void add(int index, int element){
                        if(numberOfElements < _size)
                            array[index] = element;
                        else {
                            resize();
                            array[index] = element;
                        }
                        numberOfElements++;
                    }
                '''
    print("valid code")
    print(c_linter.lint(valid_code))

    invalid_code = '''
                public void add[int index, int element){
                    if(numberOfElements < _size)
                        array[index] = element;
                    else {
                        resize();
                        array(index] = element;
                    }
                    numberOfElements++;
                }
            '''
    print("invalid code")
    print(c_linter.lint(invalid_code))


main()
