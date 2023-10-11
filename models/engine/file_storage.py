#!/usr/bin/python3
"""file storage class"""

import json
from models.base_model import BaseModel


class FileStorage:
    """filestorage class"""
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """returns the dictionary __objects"""
        return (FileStorage.__objects)
    
    def new(self, obj):
        """sets in __objects the obj with key <obj class name>.id"""
        FileStorage.__objects[str(obj.__class__.__name__ + "." + str(obj.id))] = obj

    def save(self):

        obj_dic = {}
        for key, obj in FileStorage.__objects.items():
            obj_dic[key] = obj.to_dict()
        with open(FileStorage.__file_path, 'w', encoding="utf-8") as obj_saves:
            json.dump(obj_dic, obj_saves, indent=4)

    def reload(self):
        try:
            with open(FileStorage.__file_path, 'r', encoding="utf-8") as obj_saves:
                data = json.load(obj_saves)
                objects = {}
                for key, value in data.items():
                    obj = eval(data[key]["__class__"])(**value)
                    objects[key] = obj
            FileStorage.__objects = objects
        except FileNotFoundError:
            return
