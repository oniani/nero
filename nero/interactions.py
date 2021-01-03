"""
Interactions module

David Oniani
License: MIT
"""


import os
import shutil


class Information:
    """Class to provide various information."""

    @classmethod
    def info(cls) -> None:
        """Method for 'info' command."""
        print("Nero by David Oniani")
        print("Licensed under MIT License")
        print("Copyright (c) 2018 David Oniani")
        print("Type 'help' or 'license' for more information")

    @classmethod
    def license(cls, filename: str) -> None:
        """Method for 'license' command."""
        filename = open(filename, "r")
        for line in filename.readlines():
            print(line, end="")


class InteractiveHelp:
    """Class to provide help and hints to the user."""

    @classmethod
    def help(cls) -> None:
        """Method for the 'help' command."""
        print(
            "help" + "-->".rjust(12) + "   show the manual" "for the commands"
        )
        print("license" + "-->".rjust(9) + "   show the license of the app")
        print("ls" + "-->".rjust(14) + "   list all tasks")
        print("ls --ttl" + "-->".rjust(8) + "   list titles only")
        print("ls --ddl" + "-->".rjust(8) + "   list deadlines only")
        print("add" + "-->".rjust(13) + "   add a task")
        print("rm" + "-->".rjust(14) + "   remove a task by its index")
        print("clear" + "-->".rjust(11) + "   clear the terminal window")
        print(
            "h" + "-->".rjust(15) + "   show command history for the"
            "current session"
        )
        print("q" + "-->".rjust(15) + "   quit and" + " save my edits")
        print(
            "q!"
            + "-->".rjust(14)
            + "   quit and"
            + " DO NOT"
            + " save my edits"
        )
        print(
            "FULL CLEAR" + "-->".rjust(6) + "   erase all the tasks, "
            "this is the irreversible nuclear option"
        )

    @classmethod
    def give_hint_by_cmd(cls, cmd) -> None:
        """Method for giving hints to the user."""
        if cmd in {"l", "s", "Ls", "lS", "lss", "lls"}:
            print("Did you mean 'ls' ?")

        elif cmd in {"ad", "addd", "da", "d", "dd"}:
            print("Did you mean 'add' ?")

        elif cmd in {"rm", "r", "m", "rmm", "rem"}:
            print("Did you mean 'rm' ?")

        elif cmd in {"sto", "stopp", "stoop", "stp", "st"}:
            print("Did you mean 'stop' ?")

        elif cmd in {"cle", "clearr", "cllar", "cllear", "lear"}:
            print("Did you mean 'clear' ?")

        else:
            print("Invalid command. Type 'help' for more information.")


class Function:
    """Class for terminal functionalities."""

    @classmethod
    def wn_clear(cls) -> None:
        """Clear the window."""
        if os.name == "nt":
            os.system("cls")
        else:
            os.system("clear")

    @classmethod
    def undo(cls, filename_1: str, filename_2: str) -> None:
        """Reverts all the changes."""
        shutil.copyfile(filename_2, filename_1)

    @classmethod
    def rewrite(cls, filename_1: str, filename_2: str) -> None:
        """Rewrites (copies) the contents of one file to the other."""
        shutil.copyfile(filename_1, filename_2)

    @classmethod
    def full_clear(cls, filename: str) -> None:
        """Removes all the tasks."""
        filename = open(filename, "w")
        filename.truncate(0)
        filename.write("Title,Deadline")
        filename.close()
