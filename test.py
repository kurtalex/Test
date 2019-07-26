import unittest
from selenium import webdriver
from my_sum import summary
from fractions import Fraction


class TestSum(unittest.TestCase):
    def test_list_int(self):
        """
        Test that it can sum a list of integers
        :return:
        """
        data = [1, 2, 3]
        result = summary(data)
        self.assertEqual(result, 6)

    def test_list_fraction(self):
        """
        Test that it can a list of fractions
        :return:
        """
        data = [Fraction(1, 4), Fraction(1, 4), Fraction(2, 5)]
        result = summary(data)
        self.assertEqual(result, 1)

    def return_driver(self):
        pass


if __name__ == "__main__":
    unittest.main()
