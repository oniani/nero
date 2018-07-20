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
        if cmd == 'l' or cmd == 's' or cmd == 'Ls' or cmd == 'lS' or cmd == 'lss' or cmd == 'lls':
            print("Did you mean 'ls' ?")

        elif cmd == 'ad' or cmd == 'addd' or cmd == 'da' or cmd == 'd' or cmd == 'dd':
            print("Did you mean 'add' ?")

        elif cmd == 'rm' or cmd == 'r' or cmd == 'm' or cmd == 'rmm' or cmd == 'rem':
            print("Did you mean 'rm' ?")

        elif cmd == 'sto' or cmd == 'stopp' or cmd == 'stoop' or cmd == 'stp' or cmd == 'st':
            print("Did you mean 'stop' ?")

        elif cmd == 'cle' or cmd == 'clearr' or cmd == 'cllar' or cmd == 'cllear' or cmd == 'lear':
            print("Did you mean 'clear' ?")

        else:
            print(red("Sorry, this is an invalid command. Type 'help' for more information"))

class Function:
    """Class for terminal functionalities"""
    @classmethod
    def wn_clear(cls):
        """Clear the window"""
        if os.name == 'nt':
            os.system('cls')
        else:
            os.system('clear')
