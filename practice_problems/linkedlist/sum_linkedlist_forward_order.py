'''
    Context:
        Given two numbers represented as a
            each represented as a linkedlist

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

class SumLinkedListForwardOrder:

    def add(self, first_number, second_number):
        number_system_base = 10
        result = LinkedList()
        carry = 0
        _first_number = LinkedList(first_number)
        _second_number = LinkedList(second_number)

        if _first_number.is_empty() is None:
            return second_number.toInt()
        elif _second_number.is_empty() is None:
            return first_number.toInt()

        first_num_digit = _first_number.head
        second_num_digit = _second_number.head

        # O(1)
        def _add(first, second, carry):
            sum = first + second + carry
            carry = sum//number_system_base
            current_digit_value = sum % number_system_base
            result.add(current_digit_value)
            return carry

        # O(N)
        while(first_num_digit is not None or second_num_digit is not None):
            if first_num_digit is not None and second_num_digit is not None :
                carry = _add(first_num_digit.data, second_num_digit.data, carry)
                first_num_digit = first_num_digit.next
                second_num_digit = second_num_digit.next

            elif first_num_digit is not None and second_num_digit is None:
                carry = _add(first_num_digit.data, 0, carry)
                first_num_digit = first_num_digit.next
                second_num_digit = 0
            elif first_num_digit is None and second_num_digit is not None:
                carry = _add(0, second_num_digit.data, carry)
                second_num_digit = second_num_digit.next
                first_num_digit = 0

        if carry > 0:
            result.add(carry)

        return result


if __name__ == "__main__":
    first_number = input("first number: ")
    second_number = input("second number: ")
    adder = SumLinkedListForwardOrder()
    print("adding %s and %s", (first_number, second_number))

    first_numberList = [int(n) for n in first_number]
    second_numberList = [int(n) for n in second_number]

    adder.add(first_numberList, second_numberList).toString()
