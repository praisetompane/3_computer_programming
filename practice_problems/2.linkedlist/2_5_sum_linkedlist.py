'''
    Context:
        Given:
            Two numbers
                each represented as linkedlist
            The digits in reserver order
                such that
                    the 1's digit is at the head
    
    Objective:
        Write function that:
            adds the tow numbers
            returns the sum as a linkedlist

    Definitions:
    
    Constraints:

    Assumptions:

    Example:
        input = (7 -> 1 -> 6) + (5 -> 9 -> 2)
        output = 2 -> 1 -> 9 = 912

    Flow:
        Option 1:

            While (both lists have nodes) at current digit place
                add each node's value to the current place [default to zero if no value in either list]
                    handle digit place overflows:
                        carry over extra place value
                        set remainder to output's place value
                move to each number's next node

            Performance:    
                FirstNumberLength = FNL
                SecondNumberLength = SNL

                Time = ± O(FNL + SNL)
                    process each element in each number
                Spance = ± O(FNL + SNL)
                    The longest between FNL and SNL
            
            Paper run:
                state:
                    input = (7 -> 1 -> 6) + (5 -> 9 -> 2)
                    next_place_carry_over_value = 1
                    output = 2 -> 1 => 9
                    first_number_current_node = 6
                    second_number_current_node = 2

                    number_system_base = 10
                    next_digit_place_carry = 0 #1
                    for d1, d2 in first_number, second_number
                        if d1 and d2 defined: 
                            add them + next_digit_place_carry*next_digit_place
                            if sum >= number_system_base
                                set digit to sum/number_system_base
                                set carry to sum%number_system_base
                            else
                                set digit to sum
                        if d1 defined but no d2
                            set digit to d1 + carry
                        if d2 defined but no d1
                            set digit to d2 + carry
                    
                    21

'''
from impl.linkedlist import LinkedList, Node

def add(first_number, second_number):
    number_system_base = 10
    carry = 0 
    result = LinkedList()

    d1 = first_number.head
    d2 = second_number.head

    while(d1 is not None or d2 is not None):
        if d1 is not None and d2 is not None: 
            sum = d1.data + d2.data + carry
            next_digit = sum%number_system_base
            result.add(next_digit) 
            carry = sum//number_system_base
        elif d1 is not None and d2 is None: result.add(d1.data + carry) 
        else: result.add(d2.data + carry)
        d1 = d1.next
        d2 = d2.next
    return result

def main():
    first = LinkedList()
    first.initialise_from_array([7,1,6])
    print('operand 1')
    first.printlist()
    second = LinkedList()
    second.initialise_from_array([5,9,2])
    print('operand 2')
    second.printlist()
    result = add(first, second)
    print('result')
    result.printlist()

main()


