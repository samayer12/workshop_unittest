import unittest
from src.regexDecoder import decode


class DecoderTest(unittest.TestCase):
    def test_identify_simple_variables(self):
        # Arrange
        input = 'ZAxuZAuA'
        expected = ['ZAxuZ', 'AuA']

        # Act, Assert
        self.assertEqual(expected, decode(input))

    def test_identify_escaped_variables(self):
        # Arrange, Act, Assert
        self.assertEqual(['ZAp0ZuZ', 'AuX0AZA'], decode('ZAp0ZuZAuX0AZA'))

    def test_identify_mixed_variables(self):
        # Arrange
        input = 'XydWBAdc0XazVywFEABYdXxzv32wz0dxwgjw2zvyATZBYvyc0' \
                'A0ADA1vibhidkjgfkfax1fx13XTTdYWwvCZvX1bahawhch2eC' \
                'zFwzxa0CzXzWEVwXFVZCa0jegid2kv30b1e2CFFyUcbbbaAXb' \
                'C12zgwh1ckidwhx1bvVzyFXUDyxFWxxbAEDWUcV1wfb0a1v1v' \
                '1v1v2k30bZdzAEAYzUbwUCExBZfi3w3hcawckyevDWdxxTyFa' \
                'AvAFxw0DEFFXD2xfxacigwfck3z0giYDZWFVDyTExTaZEzXcC' \
                'WCYj13dx0zgxkcAwDXFVTzZEBAbxgk10axwgkwAaxxCFZyVUw' \
                'bby0AazZaZA1yyz0212wc2'
        expected = ['XydWBAdc0XazVywFEABYdX', 'ATZBYvyc0A0ADA', 'XTTdYWwvCZvX',
                    'CzFwzxa0CzXzWEVwXFVZC', 'CFFyUcbbbaAXbC', 'VzyFXUDyxFWxxbAEDWUcV',
                    'ZdzAEAYzUbwUCExBZ', 'DWdxxTyFaAvAFxw0DEFFXD', 'YDZWFVDyTExTaZEzXcCWCY',
                    'AwDXFVTzZEBA', 'AaxxCFZyVUwbby0AazZaZA']

        self.assertEqual(expected, decode(input))


if __name__ == '__main__':
    unittest.main()
