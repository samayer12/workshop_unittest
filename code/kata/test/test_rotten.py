import unittest
from src.rotten import rotN


class MyTestCase(unittest.TestCase):
    def test_rotate_one_lowercase(self):
        # Arrange
        input = 'a'
        expected = 'b'

        # Act, Assert
        self.assertEqual('b', rotN(input, 1))

    def test_rotate_five_uppercase(self):
        # Arrange, Act, Assert
        self.assertEqual('F', rotN('A', 5))

    def test_rotate_sentence(self):
        # Arrange
        input = 'GRAVITYisDESIREtimeISsight'
        expected = 'NYHCPAFpzKLZPYLaptlPZzpnoa'

        # Act, Assert
        self.assertEqual(expected, rotN(input, 7))

    # This test will fail. Can you make it pass?
    def test_rotate_supports_integers(self):
        # Arrange
        input = 'A1steaksauce'
        expected = 'B2tufbltbvdf'

        #Act, Assert
        self.assertEqual(expected, rotN(input, 1))

if __name__ == '__main__':
    unittest.main()
