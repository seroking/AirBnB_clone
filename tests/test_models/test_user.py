#!/usr/bin/python3
"""Defines unittests for models/user.py """

import unittest
from models.user import User


class TestUser(unittest.TestCase):
    """ test user class """

    def test_init(self):
        # Test if a User instance can be initialized.
        user = User()
        self.assertIsInstance(user, User)

    def test_default_attributes(self):
        # Test if User attributes have the expected default values.
        user = User()
        self.assertEqual(user.email, "")
        self.assertEqual(user.password, "")
        self.assertEqual(user.first_name, "")
        self.assertEqual(user.last_name, "")

    def test_set_attributes(self):
        # Test setting and checking User attributes.
        user = User()
        user.email = "user@example.com"
        user.password = "secure_password"
        user.first_name = "John"
        user.last_name = "Doe"

        self.assertEqual(user.email, "user@example.com")
        self.assertEqual(user.password, "secure_password")
        self.assertEqual(user.first_name, "John")
        self.assertEqual(user.last_name, "Doe")

    def test_to_dict(self):
        # Test the conversion of a User instance to a dictionary.
        user = User()
        user_dict = user.to_dict()
        self.assertIsInstance(user_dict, dict)
        self.assertIn("__class__", user_dict)
        self.assertEqual(user_dict["__class__"], "User")
        self.assertIn("created_at", user_dict)
        self.assertIn("updated_at", user_dict)

    def test_str_representation(self):
        # Test the string representation of a User instance.
        user = User()
        user.email = "user@example.com"
        str_repr = str(user)
        self.assertIn("User", str_repr)
        self.assertIn("'email': 'user@example.com'", str_repr)


if __name__ == '__main__':
    unittest.main()
