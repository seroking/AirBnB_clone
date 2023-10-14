#!/usr/bin/python3

import os
import unittest
from datetime import datetime
import models
from time import sleep
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
import json


class test_file_storage_class(unittest.TestCase):
    """test methods of FileStorage class"""

    @classmethod
    def setUp(self):
        """Run before each individual test method in the test class. """
        try:
            os.rename("file.json", "tmp")
        except IOError:
            pass

    @classmethod
    def tearDown(self):
        """Run afer each individual test method in the test class. """
        try:
            os.remove("file.json")
        except IOError:
            pass
        try:
            os.rename("tmp", "file.json")
        except IOError:
            pass
        FileStorage._FileStorage__objects = {}

    def test_all_method(self):
        # Test if all method returs a dic
        store = FileStorage()
        self.assertEqual(dict, type(store.all()))

    def test_new_method(self):
        # Test if new method add new key to __object
        store = FileStorage()
        model = BaseModel()
        store.new(model)
        self.assertIn(str('BaseModel'+'.'+str(model.id)), store.all())

    def test_save_method(self):
        # Test if save method file exist "file.json"
        model = BaseModel()
        store = FileStorage()
        store.new(model)
        store.save()
        self.assertTrue(os.path.exists("file.json"))

        # Test the data of "file.json"

        with open("file.json", 'r') as file:
            data = json.load(file)
            self.assertIn(str('BaseModel'+'.'+str(model.id)), data)

    def test_reload_method(self):
        # Test reload method
        model1 = BaseModel()
        model2 = BaseModel()
        store = FileStorage()
        store.new(model1)
        store.new(model2)
        store.save()
        relo = FileStorage()
        relo.reload()
        self.assertIn(str('BaseModel'+'.'+str(model1.id)), relo.all())
        self.assertIn(str('BaseModel'+'.'+str(model2.id)), relo.all())


if __name__ == "__main__":
    unittest.main()
