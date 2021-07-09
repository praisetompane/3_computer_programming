from impl.stack import Stack
'''
    general use case = reverse order
    Performance:
        N = length of item list
        Time = O(2 * N) = O(N)
        Space = O(2 * N) = O(N)
'''


def reverse_order(item_list):
    reverse_order = Stack()
    reversed = None
    for item in item_list:
        reverse_order.push(item)
    if(type(item_list) == str):
        reversed = ''
        while(reverse_order.is_empty() is False):
            reversed += reverse_order.pop()
    else:
        reversed = []
        while(reverse_order.is_empty() is False):
            reversed.append(reverse_order.pop())

    return reversed



