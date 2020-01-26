from parameterized import parameterized, parameterized_class
from src.day1 import FuelCalculator

import unittest

class Day1Tests(unittest.TestCase):

    @parameterized.expand([
        (12, 2),
        (14, 2),
        (1969, 654),
        (100756, 33583)
    ])
    def test_calculate(self, mass, expected):
        self.assertEqual(expected, FuelCalculator.calculate(mass))

    @parameterized.expand([
        (12, 2),
        (1969, 966),
        (100756, 50346)
    ])
    def test_calculate_with_additional_fuel(self, mass, expected):
        self.assertEqual(expected, FuelCalculator.calculate_with_additional_fuel(mass))