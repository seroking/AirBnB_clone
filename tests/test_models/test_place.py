#!/usr/bin/python3
"""Defines unittests for models/place.py."""

import unittest
from models.place import Place


class TestPlace(unittest.TestCase):
    """ Test the place class """
    def test_init(self):
        # Test if a Place instance can be initialized.
        place = Place()
        self.assertIsInstance(place, Place)

    def test_default_attributes(self):
        # Test if Place attributes have the expected default values.
        place = Place()
        self.assertEqual(place.city_id, "")
        self.assertEqual(place.user_id, "")
        self.assertEqual(place.name, "")
        self.assertEqual(place.description, "")
        self.assertEqual(place.number_rooms, 0)
        self.assertEqual(place.number_bathrooms, 0)
        self.assertEqual(place.max_guest, 0)
        self.assertEqual(place.price_by_night, 0)
        self.assertEqual(place.latitude, 0.0)
        self.assertEqual(place.longitude, 0.0)
        self.assertEqual(place.amenity_ids, [])

    def test_set_attributes(self):
        # Test setting and checking Place attributes.
        place = Place()
        place.city_id = "12345"
        place.user_id = "user123"
        place.name = "Cozy Apartment"
        place.description = "A comfortable place to stay"
        place.number_rooms = 2
        place.number_bathrooms = 1
        place.max_guest = 4
        place.price_by_night = 100
        place.latitude = 40.7128
        place.longitude = -74.0060
        place.amenity_ids = ["amenity1", "amenity2"]

        self.assertEqual(place.city_id, "12345")
        self.assertEqual(place.user_id, "user123")
        self.assertEqual(place.name, "Cozy Apartment")
        self.assertEqual(place.description, "A comfortable place to stay")
        self.assertEqual(place.number_rooms, 2)
        self.assertEqual(place.number_bathrooms, 1)
        self.assertEqual(place.max_guest, 4)
        self.assertEqual(place.price_by_night, 100)
        self.assertEqual(place.latitude, 40.7128)
        self.assertEqual(place.longitude, -74.0060)
        self.assertEqual(place.amenity_ids, ["amenity1", "amenity2"])

    def test_to_dict(self):
        # Test the conversion of a Place instance to a dictionary.
        place = Place()
        place_dict = place.to_dict()
        self.assertIsInstance(place_dict, dict)
        self.assertIn("__class__", place_dict)
        self.assertEqual(place_dict["__class__"], "Place")
        self.assertIn("created_at", place_dict)
        self.assertIn("updated_at", place_dict)

    def test_str_representation(self):
        # Test the string representation of a Place instance.
        place = Place()
        place.name = "Cozy Apartment"
        str_repr = str(place)
        self.assertIn("Place", str_repr)
        self.assertIn("'name': 'Cozy Apartment'", str_repr)


if __name__ == '__main__':
    unittest.main()
