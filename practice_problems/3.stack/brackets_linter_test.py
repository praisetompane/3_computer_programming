from brackets_linter import BracketsLinter

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

if __name__ == "__main__":
    main()