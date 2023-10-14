#!/usr/bin/python3
"""Parent class"""
import models
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
            models.storage.new(self)

    def __str__(self):
        """
        should print: [<class name>] (<self.id>) <self.__dict__>
        """
        string = "[{class_name}] ({self_id}) {self_dict}".format(
                    class_name=self.__class__.__name__,
                    self_id=self.id,
                    self_dict=self.__dict__)
        return string

    def save(self):
        """
         updates the public instance attribute
         and save using storage
        """
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """
        returns a dictionary containing all keys/values of __dict__
        """
        obj_dic = {
            **self.__dict__, "__class__": str(self.__class__.__name__),
            "created_at": self.created_at.isoformat(),
            "updated_at": self.updated_at.isoformat()
        }
        return obj_dic
