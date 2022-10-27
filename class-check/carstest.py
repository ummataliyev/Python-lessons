import unittest
from cars import Car

class CarTest(unittest.TestCase):
    """
    For checking class "Car"
    """
    def setUp(self):
        make = "BMW",
        model = "x7",
        year = 2022,
        self.price = 150000
        self.km = 10000
        self.car1 = Car (make, model, year)
        self.car2 = Car (make, model, year, price = self.price)
    
    def tesr_create(self):
        self.assertIsNotNone(self.car1.make)
        self.assertIsNotNone(self.car1.model)
        self.assertIsNotNone(self.car1.year)
        self.assertIsNone(self.car1.price)
        self.assertEqual(0, self.car1.get_km())
        self.assertEqual(self.price, self.car2.price)

    def test_set_price(self):
        new_price = 170000
        self.car2.set_price(new_price)
        self.assertEqual(new_price, self.car2.price)

    def test_add_km(self):
        self.car1.add_km(self.km)
        self.assertEqual(self.km, self.car1.get_km)
        new_km = -50000
        try:
            self.car1.add_km(new_km)
        except ValueError as error:
            self.assertEqual(type(error), ValueError)

unittest.main()
