import unittest
from name_function import get_formatted_name

class NamesTestCase(unittest.TestCase):
    def test_first_last_name(self):
        formatted_name = get_formatted_name('andrei', 'sushchenko')
        self.assertEqual(formatted_name, 'Andrei Sushchenko')

unittest.main()
