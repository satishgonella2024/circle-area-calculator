Here is the Python code for the unit tests to verify the area calculation function:

import unittest

def calculate_area(length, width):
    if length <= 0 or width <= 0:
        return 0
    return length * width

class TestAreaCalculation(unittest.TestCase):
    def test_positive_dimensions(self):
        self.assertEqual(calculate_area(5, 3), 15)
        self.assertEqual(calculate_area(10, 4), 40)

    def test_zero_dimensions(self):
        self.assertEqual(calculate_area(0, 5), 0)
        self.assertEqual(calculate_area(3, 0), 0)

    def test_negative_dimensions(self):
        self.assertEqual(calculate_area(-2, 4), 0)
        self.assertEqual(calculate_area(5, -1), 0)

if __name__ == '__main__':
    unittest.main()