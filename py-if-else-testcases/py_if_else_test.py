import unittest

from py_if_else import is_weird

# Tests adapted from `problem-specifications//canonical-data.json` @ v1.1.0


class PyIfElseTest(unittest.TestCase):
    def test_is_odd(self):
        self.assertEqual(is_weird(3), "Weird")

    def test_is_even_in_2_to_5_not_weird(self):
        self.assertEqual(is_weird(4), "Not Weird")

    def test_is_event_in_6_to_20_weird(self):
        self.assertEqual(is_weird(10), "Weird")

    def test_greater_than_20_not_weird(self):
        self.assertEqual(is_weird(24), "Not Weird")


if __name__ == "__main__":
    unittest.main()
