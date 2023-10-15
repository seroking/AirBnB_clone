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
                  "Review"]

    def default(self, line):
        """Catch commands if nothing else matches then."""
        self._precmd(line)

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
            print("** class name missing **")
        else:
            try:
                new_instance = eval(arg)()
                new_instance.save()
                print(new_instance.id)
            except Exception:
                print("** class doesn't exist **")

    def do_show(self, arg):
        """ show the string representaion of an instance based on ID """
        args = arg.split()
        if arg == "":
            print("** class name missing **")
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
            print("** class name missing **")
        else:
            if len(args) < 2:
                print("** instance id missing **")
            elif len(args) == 2:
                if args[0] in HBNBCommand.cls_models:
                    key = str(args[0] + '.' + args[1])
                    if key in storage.all():
                        del (storage.all()[key])
                        storage.save()
                    else:
                        print("** no instance found **")
                else:
                    print("** class doesn't exist **")

    def do_all(self, arg):
        if arg == "":
            print([str(value) for key, value in storage.all().items()])
        else:
            objs = []
            if arg in HBNBCommand.cls_models:
                for key, obj in storage.all().items():
                    if obj.__class__.__name__ == arg:
                        objs.append(str(obj))
                print(objs)
            else:
                print("** class doesn't exist **")

    def do_update(self, line):
        """Update a class instance of a given id"""
        args = line.split()
        if len(args) < 1:
            print("** class name missing **")
            return
        elif args[0] not in HBNBCommand.cls_models:
            print("** class doesn't exist **")
            return
        elif len(args) < 2:
            print("** instance id missing **")
            return
        else:
            new_str = "{}.{}".format(args[0], args[1])
            if new_str not in storage.all().keys():
                print("** no instance found **")
            elif len(args) < 3:
                print("** attribute name missing **")
                return
            elif len(args) < 4:
                print("** value missing **")
                return
            else:
                setattr(storage.all()[new_str], args[2], args[3])
                storage.save()

    def count(self, arg):
        count  = 0
        if arg in HBNBCommand.cls_models:
            for key, obj in storage.all().items():
                if obj.__class__.__name__ == arg:
                    count = count + 1
            print(count)

    def _precmd(self, line):
        words = line.split('.')
        if len(words) == 2:

            the_class = words[0]
            cmd_and_par = words[1].split('(', 1)
            command = cmd_and_par[0]

            if (command) == "all":
                return HBNBCommand.do_all(self, the_class)

            if command == "count":
                return HBNBCommand.count(self, the_class)

if __name__ == '__main__':
    HBNBCommand().cmdloop()
