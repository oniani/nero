"""
Nero

Author: David Oniani
Licensed under GNU General Public License v3.0
"""


import os
from nero import engine
from nero import interactions


def main():
    """The main function - all the magic happens here."""
    file_1 = os.path.join(os.path.dirname(__file__), "data", "tasks.csv")
    file_2 = os.path.join(os.path.dirname(__file__), "data", "reserve.csv")

    tasks = engine.Core(file_1)

    interactions.Function.wn_clear()
    interactions.Information.info()

    print("\n", tasks, end="")

    history = []
    run = True

    while run:
        cmd = input()

        if cmd == "help":
            interactions.Function.wn_clear()
            interactions.InteractiveHelp.help()

        elif cmd == "license":
            interactions.Function.wn_clear()
            interactions.Information.license("LICENSE")

        elif cmd == "ls":
            interactions.Function.wn_clear()
            print(tasks, end="")

        elif cmd == "ls --ttl":
            interactions.Function.wn_clear()
            for item in tasks.get_titles():
                print(item)

        elif cmd == "ls --ddl":
            interactions.Function.wn_clear()
            for item in tasks.get_deadlines():
                print(item)

        elif cmd == "add":
            title = input("Write your task title: ")
            deadline = input("Write your task deadline: ")
            tasks.add_task(title, deadline)
            interactions.Function.wn_clear()
            print(tasks, end="")

        elif cmd == "rm":
            idx = input("Enter the index of the task you want to remove: ")

            while not idx.isdigit() or int(idx) < 0 or int(idx) >= len(tasks):
                print(
                    "Task index is a positive integer between 1 and \
                                                    the number of tasks!"
                )
                idx = input("Please, re-enter your task index: ")

            idx = int(idx)
            tasks.remove_task(idx)
            interactions.Function.wn_clear()
            print(tasks, end="")

        elif cmd == "clear":
            interactions.Function.wn_clear()

        elif cmd == "h":
            interactions.Function.wn_clear()
            for item in history:
                print(item)

        elif cmd == "q":
            run = False
            interactions.Function.rewrite(file_1, file_2)
            print(
                "The application has stopped running."
                " Your changes have been saved."
            )

        elif cmd == "q!":
            run = False
            interactions.Function.undo(file_1, file_2)
            print(
                "The application has stopped running."
                " Your changes have NOT been saved."
            )

        elif cmd == "FULL CLEAR":
            confirm = input(
                "This command will remove all of your tasks,"
                " are you sure? Y/n\n"
            )
            if confirm == "Y":
                interactions.Function.full_clear(file_1)
                interactions.Function.full_clear(file_2)
                print(
                    "All the tasks have been deleted,"
                    "there is no going back now..."
                )
                run = False
            else:
                print("Ugh... You have almost wiped your tasks clean.")

        elif cmd == "":
            pass

        else:
            interactions.InteractiveHelp.give_hint_by_cmd(cmd)

        history.append(cmd)

    history.clear()

    return True


if __name__ == "__main__":
    main()
