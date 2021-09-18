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

def add(first_number, second_number):
    number_system_base = 10
    result = LinkedList()
    carry = 0

    first_num_digit = first_number.head
    second_num_digit = second_number.head
    
    # O(1)
    def _add(first, second, carry):
        sum = first + second + carry
        carry = sum//number_system_base
        current_digit_value = sum % number_system_base
        result.add_to_top(current_digit_value)
        return carry

    # O(N)
    while(first_num_digit is not None or second_num_digit is not None):
        if first_num_digit is not None and second_num_digit is not None:
            carry = _add(first_num_digit.data, second_num_digit.data, carry)
            first_num_digit = first_num_digit.next
            second_num_digit = second_num_digit.next
        elif first_num_digit is not None and second_num_digit is None:
            carry = _add(first_num_digit.data, 0, carry)
            first_num_digit = first_num_digit.next
        elif first_num_digit is None and second_num_digit is not None:
            carry = _add(0, second_num_digit.data, carry)
            second_num_digit = second_num_digit.next

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
