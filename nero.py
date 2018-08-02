"""Importing main modules"""
import os
from nero.engine import Core
from nero.interactions import Information, InteractiveHelp, Function


def main():
    """The main function; all the magic happens here"""
    file_1 = os.path.join(os.path.dirname(__file__), 'data', 'tasks.csv')
    file_2 = os.path.join(os.path.dirname(__file__), 'data', 'reserve.csv')

    tasks = Core(file_1)
    Information.info()

    history = []
    run = True

    while run:
        cmd = input()

        if cmd == 'help':
            Function.wn_clear()
            InteractiveHelp.help()

        elif cmd == 'license':
            Function.wn_clear()
            Information.license('LICENSE')

        elif cmd == 'ls':
            Function.wn_clear()
            print(tasks, end='')

        elif cmd == 'ls --ttl':
            Function.wn_clear()
            for item in tasks.get_titles():
                print(item)

        elif cmd == 'ls --ddl':
            Function.wn_clear()
            for item in tasks.get_deadlines():
                print(item, end='')

        elif cmd == 'add':
            title = input("Write your task title: ")
            deadline = input("Write your task deadline: ")
            tasks.add_task(title, deadline)
            Function.wn_clear()
            print(tasks, end='')

        elif cmd == 'rm':
            idx = input("Enter the index of the task you want to remove: ")

            while not idx.isdigit() or int(idx) < 1 or int(idx) >= len(tasks):
                print("Task index is a positive integer between 1 and the number of tasks!")
                idx = input("Please, re-enter your task index: ")

            idx = int(idx)
            tasks.remove_task(idx)
            Function.wn_clear()
            print(tasks, end='')

        elif cmd == 'clear':
            Function.wn_clear()

        elif cmd == 'h':
            Function.wn_clear()
            for item in history:
                print(item)

        elif cmd == 'q':
            run = False
            print("The application has stopped running. Your changes have been saved.")

        elif cmd == '!q':
            run = False
            Function.undo(file_2, file_1)
            print("The application has stopped running. Your changes have NOT been saved.")

        elif cmd == 'FULL CLEAR':
            confirm = input("This command will remove all of your tasks, are you sure? Y/n\n")
            if confirm == 'Y':
                Function.full_clear(file_1)
                print("All the tasks have been deleted, there is no going back now...")
                run = False
            else:
                print("Ugh... You almost wiped your tasks clean")

        elif cmd == '':
            pass

        else:
            InteractiveHelp.give_hint_by_cmd(cmd)

        history.append(cmd)

    history.clear()

    return True

if __name__ == "__main__":
    main()
