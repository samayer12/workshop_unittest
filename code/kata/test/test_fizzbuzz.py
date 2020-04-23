#!/usr/bin/env python3

import random
import unittest
import subprocess
import sys
import os

from src.fizzbuzz import fizzbuzz


class FizzBuzzTest(unittest.TestCase):
    test_size = 100

    def test_returns_specified_length(self):
        # Arrange, Act, Assert
        self.assertEqual(self.test_size, len(fizzbuzz(self.test_size)))

    def test_divisible_by_3_is_Fizz(self):
        # Arrange
        checked_values = [3]
        checked_values += list(random.sample(range(6, self.test_size, 3), 5))

        # Act
        result = fizzbuzz(self.test_size)

        # Assert
        for value in checked_values:
            self.assertIn('Fizz', (result[value])[:4])

    def test_divisible_by_5_is_Buzz(self):
        # Arrange
        checked_values = [5]
        checked_values += list(random.sample(range(10, self.test_size, 5), 5))

        # Act
        result = fizzbuzz(self.test_size)

        # Assert
        for value in checked_values:
            self.assertIn('Buzz', (result[value])[-4:])

    def test_divisible_by_3_and_5_is_FizzBuzz(self):
        # Arrange
        checked_values = [15]
        checked_values += list(random.sample(range(30, self.test_size, 15), 2))

        # Act
        # Assert
        self.assertEqual(['FizzBuzz'] * len(checked_values),
                         list(fizzbuzz(self.test_size)[value] for value in checked_values))


if __name__ == '__main__':
    subprocess.call('clear')
    sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))
    loader = unittest.TestLoader()
    suite = loader.discover('.')
    runner = unittest.TextTestRunner()
    runner.buffer = True
    runner.run(suite)
