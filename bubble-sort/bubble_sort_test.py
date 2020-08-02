import unittest

from bubble_sort import make_bubble_sort


class BubbleSortTest(unittest.TestCase):
    def test_if_it_sort_10_to_5_list(self):
        self.assertEqual(make_bubble_sort(
            [4, 3, 2, 1]), [1, 2, 3, 4])
