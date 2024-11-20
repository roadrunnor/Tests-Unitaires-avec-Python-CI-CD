import unittest
from math_operations import addition, soustraction, multiplication, division

class TestMathOperations(unittest.TestCase):
    # Test pour l'addition
    def test_addition(self):
        self.assertEqual(addition(2, 3), 5)
        self.assertEqual(addition(-1, 1), 0)
        self.assertEqual(addition(0, 0), 0)

    # Test pour la soustraction
    def test_soustraction(self):
        self.assertEqual(soustraction(5, 3), 2)
        self.assertEqual(soustraction(0, 5), -5)
        self.assertEqual(soustraction(-1, -1), 0)

    # Test pour la multiplication
    def test_multiplication(self):
        self.assertEqual(multiplication(2, 3), 6)
        self.assertEqual(multiplication(-1, 5), -5)
        self.assertEqual(multiplication(0, 10), 0)

    # Test pour la division
    def test_division(self):
        self.assertEqual(division(10, 2), 5)
        self.assertEqual(division(-10, 2), -5)
        self.assertEqual(division(0, 1), 0)

        # Test pour la division par zéro
        with self.assertRaises(ValueError):
            division(10, 0)

if __name__ == "__main__":
    unittest.main()
