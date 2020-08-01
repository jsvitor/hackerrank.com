import unittest

from operators import operators


class OperatorsTest(unittest.TestCase):
    def test_if_is_3_and_2_work(self):
        self.assertEqual(operators(3, 2), '5\n1\n6')

    def test_if_it_is_out_of_range(self):
        self.assertEqual(operators(-1, 100000000000), None)
