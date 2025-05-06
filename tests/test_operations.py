import unittest
from calculator.operations import add, subtract, multiply, divide

class TestCalculator(unittest.TestCase):
    def test_add(self):
        self.assertEqual(add(2, 3), 5)
        self.assertEqual(add(-1, 1), 0)
        self.assertEqual(add(0, 0), 0)

    def test_subtract(self):
        # TODO: add assertions for subtract
        self.assertEqual(subtract(2, 2), 0)
        self.assertEqual(subtract(3, 3), 0)
        self.assertEqual(subtract(4, 4), 0)
        pass

    def test_multiply(self):
        self.assertEqual(multiply(2, 2), 4)
        self.assertEqual(multiply(3, 3), 9)
        self.assertEqual(multiply(4, 4), 16)
        pass

    def test_divide(self):
        # TODO: add assertions for divide
        self.assertEqual(divide(2, 2), 1)
        self.assertEqual(divide(9, 3), 3)
        self.assertEqual(divide(16, 0), "can't divide by 0")
        pass

if __name__ == '__main__':
    unittest.main()
