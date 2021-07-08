from impl.stack import Stack
'''
    Performance:
        N = length of item list
        Time = O(2 * N) = O(N)
        Space = O(2 * N) = O(N) 
'''
def reverse_order(item_list):
    reverse_order = Stack()
    reserved = ''
    for item in item_list:
        reverse_order.push(item)
    while(reverse_order.is_empty() is False):
        reserved += (reverse_order.pop())

    return reserved


def main():
    s1 = "apple"
    print("%s reversed: %s" % (s1, reverse_order(s1)))
    s1 = ""
    print("%s reversed: %s" % (s1, reverse_order(s1)))
    s1 = "racecar"
    print("%s reversed: %s" % (s1, reverse_order(s1)))


main()
