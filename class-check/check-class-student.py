import unittest
from studpers import Person, Student

class PersonTest(unittest.TestCase):
    """
    Checking
    """
    def setUp(self):
        name = 'Umidjon'
        surname = 'Ummataliyev'
        self.birth_y = 2000
        self.passport = 'AB7070707'
        self.person1 = Person (name, surname, birth_y = self.birth_y, passport = self.passport)
        self.person2 = Person (name, surname, birth_y = self.birth_y, passport = self.passport)

    def test_set_person(self):
        self.assertIsNotNone(self.person1.name)
        self.assertIsNotNone(self.person1.surname)
        self.assertIsNotNone(self.person1.birth_y)
        self.assertIsNotNone(self.person1.passport)
        self.assertEqual(self.passport, self.person2.passport)

    def test_passport(self):
        new_passport = 'AC7070707'
        self.person2.set_passport(new_passport)
        self.assertEqual(new_passport, self.person2.passport)

unittest.main()