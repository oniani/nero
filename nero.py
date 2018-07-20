"""Importing main modules"""
import os
from nero.engine import Core
from nero.interactions import Information, InteractiveHelp, Function
from nero.colorize import red, green, blue, cyan

def main():
    """The main function; all the magic happens here"""
    file = os.path.join('data', 'tasks.csv')
    tasks = Core(file)
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
            title = input(blue("Write your task title: "))
            deadline = input(blue("Write your task deadline: "))
            tasks.add_task(title, deadline)
            Function.wn_clear()
            print(tasks, end='')

        elif cmd == 'rm':
            idx = input(red("Enter the index of the task you want to remove: "))

            while not idx.isdigit() or int(idx) < 1 or int(idx) > len(tasks):
                print(red("Task index is a positive integer between 1 and the number of tasks!"))
                idx = input(red("Please, re-enter your task index: "))

            idx = int(idx)
            tasks.remove_task(idx)
            Function.wn_clear()
            print(tasks, end='')

        elif cmd == 'clear':
            Function.wn_clear()

        elif cmd == 'h':
            Function.wn_clear()
            for idx, item in enumerate(history):
                if idx != len(history)-1:
                    print(item, end=', ')
                else:
                    print(item)

        elif cmd == 'q':
            run = False
            print(cyan("The application has stopped running"))

        else:
            InteractiveHelp.give_hint_by_cmd(cmd)

        history.append(cmd)

    history.clear()

    return True

if __name__ == "__main__":
    main()
