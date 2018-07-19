'''
Importing main modules
'''
import os
from deadline.engine import Core
from deadline.interactions import Information, InteractiveHelp, Function
from deadline.colorize import red, green, blue, cyan

def main():
    file = os.path.join('.', 'data', 'tasks.csv')
    tasks = Core(file)
    Information.info()
    
    history = []
    run = True
    
    while run:
        cmd = input()
        tasks.open(file)

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
                print(red("Task index is a positive integer which is more than 1 and less than the number of tasks!"))
                idx = input(red("Please, re-enter your task index: "))

            idx = int(idx)
            tasks.remove_task(idx)
            Function.wn_clear()
            print(tasks, end='')
        
        elif cmd == 'clear':
            Function.wn_clear()

        elif cmd == 'h':
            Function.wn_clear()
            for i in range(len(history)):
                if i != len(history) - 1:
                    print(history[i], end=', ')
                else:
                    print(history[i])

        elif cmd == 'stop':
            run = False
            print(cyan("The application has stopped running"))

        else:
            InteractiveHelp.give_hint_by_cmd(cmd)

        history.append(cmd)
        tasks.close()
    
    history.clear()

    return True

if __name__ == "__main__":
    main()
