import unittest
from highnumb import maximum

class NumTest(unittest.TestCase):
    def test_high_num(self):
        number = maximum(4, 5, 6)
        self.assertEqual(number, 6)

unittest.main()