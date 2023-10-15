#!/usr/bin/python3
from models import storage
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.place import Place
from models.city import City
from models.amenity import Amenity
from models.review import Review

all_objs = storage.all()
print("-- Reloaded objects --")
for obj_id in all_objs.keys():
    obj = all_objs[obj_id]
    print(obj)

print("-- Create a new object --")
my_model = BaseModel()
my_model.name = "My_First_Model"
my_model.my_number = 89
my_model.save()
print(my_model)

print("-- Create a new object user --")

user = User()
user.first_name = "Minii"
user.last_name = "Homlnad"
user.save()

print("-- Create a new object State --")
stat = State()
stat.name = 'sakia elhemra'
stat.save()
print("-- Create a new object Place --")
plac = Place()
plac.name = "Gym"
plac.save()
print("-- Create a new object City --")
cit = City()
cit.name = "Rabat"
cit.save()
print("-- Create a new object Amenity --")
ame = Amenity()
ame.name = "nothing"
ame.save()
print("-- Create a new object Review --")
rev = Review()
rev.text = "5 Star rating"
rev.save()