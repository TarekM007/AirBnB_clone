#!/usr/bin/python3
"""
Module for console
"""

import cmd
import re
import ast
from models import storage
from models.base_model import BaseModel
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review


def split_func(e_args):
    """
    a function that splits curly braces for the update method
    """
    curly_braces = re.search(r"\{(.)\*?}", e_args)

    if curly_braces:
        id_comma = (e_args[:curly_braces.span()[0]]).split()
        id = [i.strip(",") for i in id_comma][0]

        str_data = curly_braces.group(1)
        try:
            args_dict = ast.literal_eval("{" + str_data + "}")
        except Exception:
            print("**  invalid dictionary format **")
            return
        return id, args_dict
    else:
        command = e_args.split(",")
        if command:
            try:
                id = command[0]
            except Exception:
                return "", ""
            try:
                attr_name = command[1]
            except Exception:
                return id, ""
            try:
                attr_value = command[2]
            except Exception:
                return id, attr_name
            return f"{id}", f"{attr_name} {attr_value}"


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
                    obj_id, arg_dict = split_func(e_args)
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
        """
        Update an instance by adding or updating an attribute.
        """
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
            elif len(command) < 3:
                print("** attribute name missing **")
            elif len(command) < 4:
                print("** value missing **")
            else:
                obj = objects[key]
                curly_braces = re.search(r"\{?(.)*\}", args)

                if curly_braces:
                    try:
                        str_data = curly_braces.group(1)

                        args_dict = ast.literal_eval("{" + str_data + "}")

                        attr_names = list(args_dict.keys())
                        attr_values = list(args_dict.values())
                        try:
                            attr_name_1 = attr_names[0]
                            attr_value_1 = attr_values[0]
                            setattr(obj, attr_name_1, attr_value_1)
                        except Exception:
                            pass
                        try:
                            attr_name_2 = attr_names[1]
                            attr_value_2 = attr_values[1]
                            setattr(obj, attr_name_2, attr_value_2)
                        except Exception:
                            pass
                    except Exception:
                        pass
                else:

                    attr_name = command[2]
                    attr_value = command[3]

                    try:
                        attr_value = eval(attr_value)
                    except Exception:
                        pass
                    setattr(obj, attr_name, attr_value)

                obj.save()



if __name__ == '__main__':
    HBNBCommand().cmdloop()
