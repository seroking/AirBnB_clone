#!/usr/bin/python3
""" Console 0.0.1 """


import cmd


class HBNBCommand(cmd.Cmd):
    """ cmd class """

    prompt = "(hbnb) "

    def do_quit(self, arg):
        """ Quit command to exist the program """
        return True

    def do_EOF(self):
        """ EOF command to exist the program"""
        return True

    def emptyline(self):
        """ skip empty line"""
        pass


if __name__ == '__main__':
    HBNBCommand().cmdloop()
