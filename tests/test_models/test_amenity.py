#!/usr/bin/python3
""" unitest for ameniity"""
import os
import models
import unittest
from datetime import datetime
from time import sleep
from models.amenity import Amenity


class TestAmenity(unittest.TestCase):
    """Test fo amenity"""

    def test_init(self):
        # Test if an Amenity instance can be initialized.
        amenity = Amenity()
        self.assertIsInstance(amenity, Amenity)

    def test_default_attributes(self):
        # Test if Amenity attributes have the expected default values
        amenity = Amenity()
        self.assertEqual(amenity.name, "")

    def test_set_attributes(self):
        # Test setting and checking an Amenity attribute
        amenity = Amenity()
        amenity.name = "hotel"
        self.assertEqual(amenity.name, "hotel")

    def test_to_dict(self):
        # Test the conversion of an Amenity instance to a dictionary
        amenity = Amenity()
        amenity.name = "hodi"
        amenity_dict = amenity.to_dict()
        self.assertIsInstance(amenity_dict, dict)
        self.assertIn("__class__", amenity_dict)
        self.assertEqual(amenity_dict["__class__"], "Amenity")
        self.assertIn("created_at", amenity_dict)
        self.assertIn("updated_at", amenity_dict)
        self.assertIn("name", amenity_dict)

    def test_str_representation(self):
        # Test the string representation of an Amenity instance
        amenity = Amenity()
        amenity.name = "taxi"
        str_repr = str(amenity)
        self.assertIn("Amenity", str_repr)
        self.assertIn("'name': 'taxi'", str_repr)


if __name__ == '__main__':
    unittest.main()
