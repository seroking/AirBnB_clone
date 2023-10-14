#!/usr/bin/python3
"""Defines unittests for models/review.py """
import unittest
from models.review import Review


class TestReview(unittest.TestCase):
    """test review """

    def test_init(self):
        # Test if a Review instance can be initialized.
        review = Review()
        self.assertIsInstance(review, Review)

    def test_default_attributes(self):
        # Test if Review attributes have the expected default values.
        review = Review()
        self.assertEqual(review.place_id, "")
        self.assertEqual(review.user_id, "")
        self.assertEqual(review.text, "")

    def test_set_attributes(self):
        # Test setting and checking Review attributes.
        review = Review()
        review.place_id = "place123"
        review.user_id = "user456"
        review.text = "Great place to stay!"

        self.assertEqual(review.place_id, "place123")
        self.assertEqual(review.user_id, "user456")
        self.assertEqual(review.text, "Great place to stay!")

    def test_to_dict(self):
        # Test the conversion of a Review instance to a dictionary.
        review = Review()
        review_dict = review.to_dict()
        self.assertIsInstance(review_dict, dict)
        self.assertIn("__class__", review_dict)
        self.assertEqual(review_dict["__class__"], "Review")
        self.assertIn("created_at", review_dict)
        self.assertIn("updated_at", review_dict)

    def test_str_representation(self):
        # Test the string representation of a Review instance.
        review = Review()
        review.text = "Great place to stay!"
        str_repr = str(review)
        self.assertIn("Review", str_repr)
        self.assertIn("'text': 'Great place to stay!'", str_repr)


if __name__ == '__main__':
    unittest.main()
