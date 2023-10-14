#!/usr/bin/python3
""" Defines unittests for models/state.py """
import unittest
from models.state import State


class TestState(unittest.TestCase):
    """ Test Class state"""

    def test_init(self):
        # Test if a State instance can be initialized.
        state = State()
        self.assertIsInstance(state, State)

    def test_default_attributes(self):
        # Test if State attributes have the expected default values.
        state = State()
        self.assertEqual(state.name, "")

    def test_set_attributes(self):
        # Test setting and checking State attributes.
        state = State()
        state.name = "California"
        self.assertEqual(state.name, "California")

    def test_to_dict(self):
        # Test the conversion of a State instance to a dictionary.
        state = State()
        state_dict = state.to_dict()
        self.assertIsInstance(state_dict, dict)
        self.assertIn("__class__", state_dict)
        self.assertEqual(state_dict["__class__"], "State")
        self.assertIn("created_at", state_dict)
        self.assertIn("updated_at", state_dict)

    def test_str_representation(self):
        # Test the string representation of a State instance.
        state = State()
        state.name = "California"
        str_repr = str(state)
        self.assertIn("State", str_repr)
        self.assertIn("'name': 'California'", str_repr)


if __name__ == '__main__':
    unittest.main()
