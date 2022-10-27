import unittest
from pi import getArea, getPerimetr

class CircleTest(unittest.TestCase):
    def test_area(self):
        self.assertAlmostEqual(getArea(5), 78.53975)

    def test_perimetr(self):
        self.assertAlmostEqual(getPerimetr(2), 12.56636)\

unittest.main()