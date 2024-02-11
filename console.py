#!/usr/bin/python3
"""
Module for console
"""

import cmd


class HBNBCommand(cmd.Cmd):
    """
    HBNBCommand console class
    """
    prompt = '(hbnb) '

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


if __name__ == '__main__':
    HBNBCommand().cmdloop()
