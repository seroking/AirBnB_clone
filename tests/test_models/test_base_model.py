#!/usr/bin/python3

import unittest
from datetime import datetime
import models
from time import sleep
from models.base_model import BaseModel


class TestBaseModel(unittest.TestCase):
    """test methods of BaseModel class"""
    def test_id_(self):
        # Test id is an str
        self.assertEqual(str, type(BaseModel().id))

    def test_two_models_unique_ids(self):
        model1 = BaseModel()
        model2 = BaseModel()
        self.assertNotEqual(model1.id, model2.id)

    def test_init(self):
        # Test the initialization of a BaseModel object
        model = BaseModel()
        self.assertIsInstance(model, BaseModel)
        self.assertTrue(hasattr(model, 'id'))
        self.assertTrue(hasattr(model, 'created_at'))
        self.assertTrue(hasattr(model, 'updated_at'))

    def test_str(self):
        # Test the __str__ method
        model = BaseModel()
        expected_str = f"[BaseModel] ({model.id}) {model.__dict__}"
        self.assertEqual(str(model), expected_str)

    def test_save(self):
        # Test the save method
        model = BaseModel()
        original_updated_at = model.updated_at
        model.save()
        self.assertNotEqual(original_updated_at, model.updated_at)

    def test_to_dict(self):
        # Test the to_dict method
        model = BaseModel()
        model_dict = model.to_dict()
        self.assertIsInstance(model_dict, dict)
        self.assertIn('id', model_dict)
        self.assertIn('created_at', model_dict)
        self.assertIn('updated_at', model_dict)
        self.assertEqual(model_dict['__class__'], 'BaseModel')
        self.assertEqual(type(model_dict["id"]), str)
        self.assertEqual(type(model_dict["created_at"]), str)
        self.assertEqual(type(model_dict["updated_at"]), str)
        self.assertEqual(type(model_dict["__class__"]), str)

        # Test to_dict with new attribute
        model = BaseModel()
        model.attr1 = "new attr"
        model.attr2 = 15
        model_dict = model.to_dict()
        self.assertIn('id', model_dict)
        self.assertIn('created_at', model_dict)
        self.assertIn('updated_at', model_dict)
        self.assertIn('attr1', model_dict)
        self.assertIn('attr2', model_dict)
        self.assertEqual(model_dict['__class__'], 'BaseModel')

    def test_init_with_arguments(self):
        # Test the __init__ method with keyword arguments
        time_format = "%Y-%m-%dT%H:%M:%S.%f"

        created_at = "2020-06-29T21:30:00.000000"
        updated_at = "2020-06-29T21:30:00.000000"
        model = BaseModel(id='123',
                          created_at=created_at, updated_at=updated_at)
        self.assertEqual(model.id, '123')
        self.assertEqual(model.created_at,
                         datetime.strptime(created_at, time_format))
        self.assertEqual(model.updated_at,
                         datetime.strptime(updated_at, time_format))


if __name__ == '__main__':
    unittest.main()
