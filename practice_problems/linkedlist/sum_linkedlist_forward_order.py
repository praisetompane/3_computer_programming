'''
    Context:
        Given numbers represented as linkedlist
    Objective:
        Write function that: 
            adds the two numbers
            returns sum as linkedlist

    Defintions:

    Contraints:

    Assumptions:
        base 10 number system
    Example:

        input = (6 -> 1 -> 7) + (2 -> 9 -> 5)
        output = (9 -> 1 -> 2)

'''
from linkedlist.impl.linkedlist import LinkedList
from stack.impl.stack_list import Stack

def add(first_number, second_number):
    result = LinkedList()
    first_number_stack = Stack()
    second_number_stack = Stack()

    first_num_digit = first_number.head
    second_num_digit = second_number.head
    carry = 0
    number_system_base = 10

    #O(1)
    def _add(first, second, carry):
        sum = first + second + carry
        carry = sum//number_system_base
        current_digit_value = sum%number_system_base
        result.add_to_top(current_digit_value)
        return carry

    #O(N)
    while(first_num_digit is not None or second_num_digit is not None):
        print("creating stacks")
        if first_num_digit is not None and second_num_digit is not None:
            first_number_stack.push(first_num_digit.data)
            second_number_stack.push(second_num_digit.data)
            first_num_digit = first_num_digit.next
            second_num_digit = second_num_digit.next
        elif first_num_digit is not None and second_num_digit is None:
            first_number_stack.push(first_num_digit.data)
            first_num_digit = first_num_digit.next
        elif first_num_digit is None and second_num_digit is not None:
            second_number_stack.push(second_num_digit.data)
            second_num_digit = second_num_digit.next
    #O(N)
    while(not first_number_stack.is_empty() or not second_number_stack.is_empty()):
        print("adding stacks")
        if not first_number_stack.is_empty() and not second_number_stack.is_empty():
            carry = _add(first_number_stack.pop(), second_number_stack.pop(), carry)
        elif not first_number_stack.is_empty() and second_number_stack.is_empty():
            carry = _add(first_number_stack.pop(), 0, carry)
        elif first_number_stack.is_empty() and not second_number_stack.is_empty():
            carry = _add(0, second_number_stack.pop(), carry)

    if carry > 0:
        result.add_to_top(carry)

    return result


if __name__ == "__main__":
    first = input("first number: ")
    first_number = LinkedList([int(n) for n in first])
    second = input("second number: ")
    second_number = LinkedList([int(n) for n in second])

    print("adding %s and %s", (first, second))

    add(first_number, second_number).toString()