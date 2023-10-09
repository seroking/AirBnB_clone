#!/usr/bin/python3
"""Parent class"""
import uuid
from datetime import datetime


class BaseModel:
    """The base class"""

    id = str(uuid.uuid4())
    created_at = datetime.now()
    updated_at = created_at

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
my_model.name = "My First Model"
my_model.my_number = 89
print(my_model)
my_model.save()
print(my_model)
my_model_json = my_model.to_dict()
print(my_model_json)
print("JSON of my_model:")
for key in my_model_json.keys():
    print("\t{}: ({}) - {}".format(key, type(my_model_json[key]), my_model_json[key]))
