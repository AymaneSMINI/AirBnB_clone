#!/usr/bin/python3

import cmd
from .models.base_model import BaseModel
import storage
class HBNBCommand(cmd.Cmd):
    """command line"""
    prompt = '(hbnb) '

    def do_quit(self, line):
        """Quit command to exit the program"""
        return True

    def do_EOF(self, line):
        """EOF command to exit the program"""
        return True
    def emptyline(self):
        """Do nothing when an empty line is entered"""
        pass
    def do_create(self, line):
        if line is None or line == "":
            print("** class name missing **")
        elif line != "BaseModel":
            print("** class doesn't exist **")
        else:
            my_model = BaseModel()
            print(dir(my_model))



def main():
    HBNBCommand().cmdloop()

if __name__ == '__main__':
    main()

