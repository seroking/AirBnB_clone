#!/usr/bin/python3
"""Parent class"""
import uuid
from datetime import datetime


class BaseModel:
    """The base class"""

    def __init__(self, *args, **kwargs):

        """ instantiates objects of the class BaseModel """

        time_format = "%Y-%m-%dT%H:%M:%S.%f"

        if kwargs:
            for key, value in kwargs.items():
                if key == 'updated_at':
                    self.updated_at = datetime.strptime(value, time_format)
                elif key == 'created_at':
                    self.created_at = datetime.strptime(value, time_format)
                elif key != "__class__":
                    setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()

    def __str__(self):
        """
        should print: [<class name>] (<self.id>) <self.__dict__>

        """
        string = "[{class_name}] ({self_id}) <{self_dict}>".format(
                    class_name=self.__class__.__name__,
                    self_id=self.id,
                    self_dict=self.__dict__)
        return string

    def save(self):
        self.updated_at = datetime.now()

    def to_dict(self):
        obj_dic = {
            **self.__dict__, "__clas__": str(__class__.__name__),
            "created_at": self.created_at.isoformat(),
            "updated_at": self.updated_at.isoformat()
        }
        return obj_dic


my_model = BaseModel()
my_model.name = "My_First_Model"
my_model.my_number = 89
print(my_model.id)
print(my_model)
print(type(my_model.created_at))
print("--")
my_model_json = my_model.to_dict()
print(my_model_json)
print("JSON of my_model:")
for key in my_model_json.keys():
    print("\t{}: ({}) - {}".format(key, type(my_model_json[key]), my_model_json[key]))

print("--")
my_new_model = BaseModel(**my_model_json)
print(my_new_model.id)
print(my_new_model)
print(type(my_new_model.created_at))

print("--")
print(my_model is my_new_model)
