"""Importing modules"""
import os
from nero.colorize import red


class Information:
    """Class to provide various information"""
    @classmethod
    def info(cls):
        """Method for 'info' command"""
        print("Nero by David Oniani")
        print("Licensed under MIT")
        print("Copyright (c) 2018 David Oniani")
        print("Type 'help' or 'license' for more information")

    @classmethod
    def license(cls, file):
        """Method for 'license' command"""
        file = open(file, 'r')
        for line in file.readlines():
            print(line, end='')


class InteractiveHelp:
    """Class to provide help and hints to the user"""
    @classmethod
    def help(cls):
        """Method for the 'help' command"""
        print("'ls' - list all tasks")
        print("'ls --ttl' - list titles only")
        print("'ls --ddl' - list deadlines only")
        print("'add' - add a task")
        print("'rm' - remove a task by its index")
        print("'h' - show command history for the current session")
        print("'clear' - clear the terminal window")
        print("'q' - quit and save my edits")

    @classmethod
    def give_hint_by_cmd(cls, cmd):
        """Method for giving hints to the user"""
        if cmd in ['l', 's', 'Ls', 'lS', 'lss', 'lls']:
            print("Did you mean 'ls' ?")

        elif cmd in ['ad', 'addd', 'da', 'd', 'dd']:
            print("Did you mean 'add' ?")

        elif cmd in ['rm', 'r', 'm', 'rmm', 'rem']:
            print("Did you mean 'rm' ?")

        elif cmd in ['sto', 'stopp', 'stoop', 'stp', 'st']:
            print("Did you mean 'stop' ?")

        elif cmd in ['cle', 'clearr', 'cllar', 'cllear', 'lear']:
            print("Did you mean 'clear' ?")

        else:
            print(red("Invalid command. Type 'help' for more information"))


class Function:
    """Class for terminal functionalities"""
    @classmethod
    def wn_clear(cls):
        """Clear the window"""
        if os.name == 'nt':
            os.system('cls')
        else:
            os.system('clear')
