#!/usr/bin/python3
"""
Module for console
"""

import cmd
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
    HBNBCommand console class
    """
    prompt = '(hbnb) '
    valid_class = ["BaseModel", "User", "Amenity",
                     "Place", "Review", "State", "City"]

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
            new_instance = eval(f"{command[0]}()")
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

    def default(self, args):
        """Default behavior for cmd module when input is invalid"""
        arg_list = args.split('.')

        cls_num = arg_list[0]

        command = arg_list[1].split('(')

        cmd_method = command[0]

        e_args = command[1].split(')')[0]

        method_dict = {
                'all': self.do_all,
                'show': self.do_show,
                'destroy': self.do_destroy,
                'update': self.do_update,
                'count': self.do_count
                }

        if cmd_method in method_dict.keys():
            if cmd_method != "update":
                return method_dict[cmd_method]("{} {}".format(cls_num, e_args))
            else:
                if not cls_num:
                    print("** class name missing **")
                    return
                try:
                    obj_id, arg_dict = split_curly_braces(e_args)
                except Exception:
                    pass
                try:
                    call = method_dict[cmd_method]
                    return call("{} {} {}".format(cls_num, obj_id, arg_dict))
                except Exception:
                    pass
        else:
            print("*** Unknown syntax: {}".format(args))
            return False

    def do_count(self, args):
        """Counts and retrieves the number of instances of a class"""
        objects = storage.all()

        command = args.split()

        if args:
            cls_num = command[0]

        count = 0

        if command:
            if cls_num in self.valid_class:
                for obj in objects.values():
                    if obj.__class__.__name__ == cls_num:
                        count += 1
                print(count)
            else:
                print("** invalid class name **")
        else:
            print("** class name missing **")

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
