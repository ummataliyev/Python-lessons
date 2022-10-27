import unittest
from name import get_full_name

class NameTest(unittest.TestCase):
    def test_full_name(self):
        name = get_full_name('umidjon', 'ummataliyev')
        self.assertEqual(name, 'Umidjon Ummataliyev')
    
    def fathers_name(self):
        name = get_full_name('umidjon', 'ummtaliyev', 'bakhramovich')
        self.assertEqual(name, 'Umidjo Ummataliyev Bakhramovich')

unittest.main()