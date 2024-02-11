!/usr/bin/python
"""
Module for console
"""

import cmd
class HBNBCommand(cmd.Cmd):
    prompt = "(hbnb)"

    def do_quit(self, args):
        """exit the program"""
        return True
    def help_quit(self, args):
        """documented line to help understand quit command"""
        print("Quit command to exit the program")
    def do_EOF(self, args):
        """exit the program"""
        print("")
        return True

if __name__ == '__main__':
    HBNBCommand().cmdloop()
