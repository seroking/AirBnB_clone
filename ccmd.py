#!/usr/bin/python3
""" Defines entry point of the command interpreter."""
import cmd
import re
from shlex import split
from models import storage
from models.base_model import BaseModel
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review

class HBNBCommand(cmd.Cmd):
    """
    Implements the class HBNBCommand.

    Attributes:
        prompt (str): The command prompt.
    """
    prompt = "(hbnb) "

    cls_models = ["City",
                  "BaseModel",  
                    "User",
                    "Place",
                    "State",
                    "Amenity",
                    "Review"
                    ]

    def do_quit(self, args):
        """ Quit command to exit. """
        return True

    def do_EOF(self, arg):
        """ EOF signal to exit the program."""
        return True

    def emptyline(self):
        """ Nothing done when recieving an empty line"""
        pass

    def do_create(self, arg):
        """ create a new instance of the class BaseModel """
        if arg == "":
            print ("** class name missing **")
        else:
            try:
                new_instance = eval(arg)()
                new_instance.save()
                print (new_instance.id)
            except NameError:
                print ("** class doesn't exist **")

    def do_show(self, arg):
        """ show the string representaion of an instance based on ID """
        args = re.split(r'\s+', arg)
        if arg == "":
            print ("** class name missing **")
        else:
            if len(args) < 2:
                print("** instance id missing **")
            elif len(args) == 2:
                if args[0] in HBNBCommand.cls_models:
                    key = str(args[0] + '.' + args[1])
                    if key in storage.all():
                        print(storage.all()[key])
                    else:
                        print("** no instance found **")
                else:
                    print("** class doesn't exist **")

    def do_destroy(self, arg):
        """Destroy an object"""
        args = re.split(r'\s+', arg)
        if arg == "":
            print ("** class name missing **")
        else:
            if len(args) < 2:
                print("** instance id missing **")
            elif len(args) == 2:
                if args[0] in HBNBCommand.cls_models:
                    key = str(args[0] + '.' + args[1])
                    if key in storage.all():
                        del(storage.all()[key])
                    else:
                        print("** no instance found **")
                else:
                    print("** class doesn't exist **")

    def do_all(self, arg):
        if arg == "":
            print(storage.all())
            return
        if arg in HBNBCommand.cls_models:
            for key, obj in storage.all().items():
                    if obj.__class__.__name__ == arg:
                        print(value)
        else:
            print("** class doesn't exist **")

    def do_update(self, line):
        args = re.split(r'\s+', line)
        


if __name__ == '__main__':
    HBNBCommand().cmdloop()
