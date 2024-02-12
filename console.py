#!/usr/bin/python3
"""
Module for console
"""

import cmd
from models import storage
from models.base_model import BaseModel
from models.user import User


class HBNBCommand(cmd.Cmd):
    """
    HBNBCommand console class
    """
    prompt = '(hbnb) '
    valid_class = ["BaseModel", "User"]

    def emptyline(self):
        """
        Do nothing when an empty line is entered.
        """
        pass

    def do_quit(self, args):
        """Quit command to exit the program"""
        return True

    def do_EOF(self, args):
        """exit the program"""
        print()
        return True

    def do_create(self, args):
        """Create a new instance of BaseModel"""
        command = args.split()

        if len(command) == 0:
            print("** class name missing **")
        elif command[0] not in self.valid_class:
            print("** class doesn't exist **")
        else:
            new_instance = eval(f"{commands[0]}()")
            storage.save()
            print(new_instance.id)

    def do_show(self, args):
        """Show the string representation of an instance."""
        command = args.split()

        if len(command) == 0:
            print("** class name missing **")
        elif command[0] not in self.valid_class:
            print("** class doesn't exist **")
        elif len(command) < 2:
            print("** instance id missing **")
        else:
            objects = storage.all()

            key = "{}.{}".format(command[0], command[1])
            if key not in objects:
                print("** no instance found **")
            else:
                print(objects[key])

    def do_destroy(self, args):
        """Delete an instance based on the class name and id."""
        command = args.split()

        if len(command) == 0:
            print("** class name missing **")
        elif command[0] not in self.valid_class:
            print("** class doesn't exist **")
        elif len(command) < 2:
            print("** instance id missing **")
        else:
            objects = storage.all()
            key = "{}.{}".format(command[0], command[1])
            if key not in objects:
                print("** no instance found **")
            else:
                del objects[key]
                storage.save()

    def do_all(self, args):
        """Print the string representation of all instances"""
        objects = storage.all()

        command = args.split()

        if len(command) == 0:
            for key, value in objects.items():
                print(str(value))
        elif command[0] not in self.valid_class:
            print("** class doesn't exist **")
        else:
            for key, value in objects.items():
                if key.split('.')[0] == command[0]:
                    print(str(value))

    def do_update(self, args):
        """Update a class instance of a given id by adding or updating
        a given attribute key/value pair or dictionary.
        """
        command = args.split()
        if len(command) < 1:
            print("** class name missing **")
            return
        elif command[0] not in self.valid_class:
            print("** class doesn't exist **")
            return
        elif len(command) < 2:
            print("** instance id missing **")
            return
        else:
            new_str = f"{command[0]}.{command[1]}"
            if new_str not in storage.all().keys():
                print("** no instance found **")
            elif len(command) < 3:
                print("** attribute name missing **")
                return
            elif len(command) < 4:
                print("** value missing **")
                return
            else:
                setattr(storage.all()[new_str], command[2], command[3])
                storage.save()


if __name__ == '__main__':
    HBNBCommand().cmdloop()
