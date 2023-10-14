#!/usr/bin/python3
""" Console 0.0.1 """


import cmd
from shlex import split
from models.base_model import BaseModel
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User
from models import storage
from models.city import City


class HBNBCommand(cmd.Cmd):
    """ cmd class """

    prompt = "(hbnb) "

    cls = {"BaseModel", "User"}

    def do_quit(self, arg):
        """ Quit command to exist the program """
        return True

    def do_EOF(self):
        """ EOF command to exist the program"""
        return True

    def emptyline(self):
        """ skip empty line"""
        pass

    def do_create(self, arg):
        """ create a new instance of the class BaseModel """
        if arg == "":
            print("** class doesn't exist **")
        else:
            try:
                new_instance = eval(arg)()
                new_instance.save()
                print(new_instance.id)
            except NameError:
                print("** class name missing **")

    def do_show(self, arg):
        """ show the string representaion of an instance based on ID """
        args = arg.split()
        if not args:
            print("** class name missing **")
        else:
            cls_name = args[0]
            if len(args) == 0:
                print("** class name missing **")
            elif cls_name not in HBNBCommand.cls:
                print("** class doesn't exist **")
            elif len(args) < 2:
                print("** instance id missing **")
            else:
                key_obj = "{}.{}".format(cls_name, args[1])
                all_objs = storage.all()
                if key_obj in all_objs:
                    print(all_objs[key_obj])
                else:
                    print("** no instance found **")

    def do_destroy(self, arg):
        """ destroy an instance """
        args = arg.split()
        if not arg:
            print("** class name missing **")
        else:
            cls_name = args[0]
            if len(args) == 0:
                print("** class name missing **")
            elif cls_name not in HBNBCommand.cls:
                print("** class doesn't exist **")
            elif len(args) < 2:
                print("** instance id missing **")
            else:
                key_object = "{}.{}".format(cls_name, args[1])
                all_objects = storage.all()
                if key_object in all_objects:
                    del all_objects[key_object]

    def do_all(self, arg):
        """Prints all string representation of all instances."""
        args = arg.split()
        all_objects = storage.all()
        if not args:
            print([str(obj) for obj in all_objects.values()])
        else:
            try:
                cls_name = args[0]
                if cls_name not in HBNBCommand.cls:
                    print("** class doesn't exist **")
                else:
                    if hasattr(eval(cls_name), "all"):
                        obj_cls = [str(obj) for obj in eval(cls_name).all()]
                        print(obj_cls)
                    else:
                        objs_cls = [
                            str(obj)
                            for key, obj in all_objects.items()
                            if key.startswith(cls_name + ".")
                        ]
                        print(objs_cls)
            except IndexError:
                print("** class name missing **")

    def do_update(self, arg):
        """
        Updates an instance based on the
        class name and id by adding or updating attribute
        """
        args = arg.split()
        if len(args) >= 4:
            key = "{}.{}".format(args[0], args[1])
            if key in storage.all():
                obj = storage.all()[key]
                setattr(obj, args[2], eval(args[3]))
                obj.save()
            else:
                print("** no instance found **")
        elif len(args) == 0:
            print("** class name missing **")
        elif args[0] not in HBNBCommand.cls:
            print("** class doesn't exist **")
        elif len(args) == 1:
            print("** instance id missing **")
        elif ("{}.{}".format(args[0], args[1])) not in storage.all():
            print("** no instance found **")
        elif len(args) == 2:
            print("** attribute name missing **")
        elif len(args) == 3:
            print("** value missing **")


if __name__ == '__main__':
    HBNBCommand().cmdloop()
