"""this is a module doc"""

'''
    any python file is a module
    convention: file name in lower case
'''

#set values to expose as interface
__all__ = ['generalised_adder']

def adder(x, y):
    return x + y

def generalised_adder(*args):
    return sum(args)
'''
    in Terminal
    ./repl_run.sh
'''