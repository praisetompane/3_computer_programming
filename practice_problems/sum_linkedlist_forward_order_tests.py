import unittest

from linkedlist.impl.linkedlist import LinkedList
from linkedlist.sum_linkedlist_forward_order import SumLinkedListForwardOrder


class SumLinkedListForwardOrder(unittest.TestCase):
    adder = SumLinkedListForwardOrder()
    def test_add_equal_length(self):
        result = self.adder.add([1,2,8], [9,8,3])
        self.assertEqual(1111, result, '128 + 983 = 1111')
'''
    def test_add_equal_length_with_carry(self):
        result = self.adder.add([7,1,6], [5,9,3])
        self.assertEqual(1012, result.toInt(), '617 + 395 = 1012')

    def test_add_different_length(self):
        result = self.adder.add([7,1], [5,9,2])
        self.assertEqual(312, result.toInt(), '17 + 295 = 312')

    def test_add_single_with_carry(self):
        result = self.adder.add([7], [5])
        self.assertEqual(12, result.toInt(), '7 + 5 = 12')

    def test_add_single_with_no_carry(self):
        result = self.adder.add([7], [1])
        self.assertEqual(8, result.toInt(), '7 + 1 = 8')
        
    def test_add_empty(self):
        result = self.adder.add([], [])
        self.assertEqual(0, result.toInt(), 'empty + empty = empty 0')
        '''
if __name__ == "__main__":
    unittest.main()
