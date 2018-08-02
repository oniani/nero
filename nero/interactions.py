"""Importing modules"""
import os


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
        print("ls" +  "⟶".rjust(13) + "     list all tasks")
        print("ls --ttl" + "⟶".rjust(7) + "     list titles only")
        print("ls --ddl" + "⟶".rjust(7) + "     list deadlines only")
        print("add" + "⟶".rjust(12) + "     add a task")
        print("rm" + "⟶".rjust(13) + "     remove a task by its index")
        print("clear" + "⟶".rjust(10) + "     clear the terminal window")
        print("h" + "⟶".rjust(14) + "     show command history for the current session")
        print("undo" + "⟶".rjust(10) + "     undo the previous command")
        print("q" + "⟶".rjust(14) + "     quit and" + " save my edits")
        print("!q" + "⟶".rjust(13) +  "     quit and" + " DO NOT" + " save my edits")
        print("FULL CLEAR" + "⟶".rjust(5) + "     erase all the tasks, this is the irreversible nuclear option")

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
            print("Invalid command. Type 'help' for more information")


class Function:
    """Class for terminal functionalities"""
    @classmethod
    def wn_clear(cls):
        """Clear the window"""
        if os.name == 'nt':
            os.system('cls')
        else:
            os.system('clear')

    @classmethod
    def undo(cls, file_1, file_2):
        """Reverts all the changes"""
        file_1 = open(file_1, 'r')
        lines = file_1.readlines()
        file_1.close()

        file_2 = open(file_2, 'w')

        for task in lines:
            file_2.write(task)

        file_2.close()

    @classmethod
    def full_clear(cls, file):
        """Removes all the tasks"""
        file = open(file, 'w')
        file.close()
