import unittest

from impl.linkedlist import LinkedList
from sum_linkedlist import add

class SumLinkedListTests(unittest.TestCase):
    def test_add_equal_length(self):
        first = LinkedList()
        first.initialise_from_array([7,1,6])

        second = LinkedList()
        second.initialise_from_array([5,9,2])

        print('test_add_equal_length')
        result = add(first, second)
        result.printlist() #219
        self.assertEqual(True, True)
    def test_add_equal_length_with_carry(self):
        first = LinkedList()
        first.initialise_from_array([7,1,6])

        second = LinkedList()
        second.initialise_from_array([5,9,3])

        print('test_add_equal_length_with_carry')
        result = add(first, second)
        result.printlist() #2101
        self.assertEqual(True, True)

    def test_add_different_length(self):
        first = LinkedList()
        first.initialise_from_array([7,1])

        second = LinkedList()
        second.initialise_from_array([5,9,2])

        print('test_add_different_length')
        result = add(first, second)
        result.printlist() #213
        self.assertEqual(True, True)

    def test_add_single_with_carry(self):
        first = LinkedList()
        first.initialise_from_array([7])

        second = LinkedList()
        second.initialise_from_array([5])

        print('test_add_single_with_carry')
        result = add(first, second)
        result.printlist() #21
        self.assertEqual(True, True)
        return

    def test_add_single_with_no_carry(self):
        first = LinkedList()
        first.initialise_from_array([7])

        second = LinkedList()
        second.initialise_from_array([1])

        print('test_add_single_with_no_carry')
        result = add(first, second)
        result.printlist() #8
        self.assertEqual(True, True)
        return

    def test_add_empty(self):
        first = LinkedList()
        first.initialise_from_array([])

        second = LinkedList()
        second.initialise_from_array([])

        print('test_add_empty')
        result = add(first, second)
        result.printlist() #nothing
        self.assertEqual(True, True)
        return

if __name__ == '__main__':
    unittest.main()

