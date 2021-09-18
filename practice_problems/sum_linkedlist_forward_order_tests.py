import unittest

from linkedlist.impl.linkedlist import LinkedList
from linkedlist.sum_linkedlist_forward_order import add


class SumLinkedListForwardOrder(unittest.TestCase):
    def test_add_equal_length(self):
        first = LinkedList([6, 1, 7])
        second = LinkedList([2, 9, 5])
        result = add(first, second)
        result_val = result.toInt()
        self.assertEqual(912, result_val, "617 + 295 = 912")


if __name__ == "__main__":
    unittest.main()
