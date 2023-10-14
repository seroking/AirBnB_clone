#!/usr/bin/python3
"""Defines unittests for models/city"""

import unittest
from models.city import City


class TestCity(unittest.TestCase):
    """ TEst for the class city """

    def test_init(self):
        # Test if a City instance can be initialized.
        city = City()
        self.assertIsInstance(city, City)

    def test_default_attributes(self):
        # Test if City attributes have the expected default values.
        city = City()
        self.assertEqual(city.state_id, "")
        self.assertEqual(city.name, "")

    def test_set_attributes(self):
        # Test setting and checking City attributes.
        city = City()
        city.state_id = "12345"
        city.name = "New York"
        self.assertEqual(city.state_id, "12345")
        self.assertEqual(city.name, "New York")

    def test_to_dict(self):
        # Test the conversion of a City instance to a dictionary.
        city = City()
        city_dict = city.to_dict()
        self.assertIsInstance(city_dict, dict)
        self.assertIn("__class__", city_dict)
        self.assertEqual(city_dict["__class__"], "City")
        self.assertIn("created_at", city_dict)
        self.assertIn("updated_at", city_dict)

    def test_str_representation(self):
        # Test the string representation of a City instance.
        city = City()
        city.state_id = "12345"
        city.name = "New York"
        str_repr = str(city)
        self.assertIn("City", str_repr)
        self.assertIn("'state_id': '12345'", str_repr)
        self.assertIn("'name': 'New York'", str_repr)


if __name__ == '__main__':
    unittest.main()
