from impl.stack import Stack

class BracketsLinter():
    document = None
    opening_parathesis = None
    def __init__(self):
        self.opening_parathesis = Stack()

    def lint(self, document):
        document_length = len(document)
        for char in range(document_length):
            if(char == '(' or char == '{' or char == '['): self.opening_parathesis.push(char)
            elif(char == ')' or char == '}' or char == ']'): self.opening_parathesis.pop()

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
    assert(c_linter.lint(valid_code))

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
    assert(c_linter.lint(invalid_code))
main()