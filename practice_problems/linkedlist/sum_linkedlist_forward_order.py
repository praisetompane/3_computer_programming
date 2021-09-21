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

class SumLinkedListForwardOrder:

    def initialise_from_array_into_stack(self, numbers):
        num = Stack()
        for n in numbers:
            num.push(n)
        return num

    def add(self, first_number, second_number):
        number_system_base = 10
        result = LinkedList()
        carry = 0
        _first_number = self.initialise_from_array_into_stack(first_number)
        _second_number = self.initialise_from_array_into_stack(second_number)

        if _first_number.is_empty() is False or _second_number.is_empty() is False:
            return 0
        first_num_digit = _first_number.pop()
        second_num_digit = _second_number.pop()

        # O(1)
        def _add(first, second, carry):
            sum = first + second + carry
            carry = sum//number_system_base
            current_digit_value = sum % number_system_base
            result.add(current_digit_value)
            return carry

        # O(N)
        while(_first_number.is_empty() is False or _second_number.is_empty() is False):
            if _first_number.is_empty() is False and _second_number.is_empty() is False:
                carry = _add(first_num_digit,second_num_digit, carry)
                first_num_digit = _first_number.pop()
                second_num_digit = _second_number.pop()

            elif _first_number.is_empty() is False and _second_number.is_empty() is True:
                carry = _add(first_num_digit, 0, carry)
                first_num_digit = _first_number.pop()
                second_num_digit = 0
            elif _first_number.is_empty()  is True and _second_number.is_empty()  is False:
                carry = _add(0, second_num_digit, carry)
                second_num_digit = _second_number.pop()
                first_num_digit = 0

        carry = _add(first_num_digit,second_num_digit, carry)
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
