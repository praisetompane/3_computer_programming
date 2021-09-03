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

'''
from impl.linkedlist import LinkedList, Node

def add(first_number, second_number):
    return

def main():
    first = LinkedList()
    first.initialise_from_array([7,1,6])
    first.printlist()
    second = LinkedList()
    second.initialise_from_array([5,9,2])
    second.printlist()
    result = add(first, second)
    result.printlist()

main()


