from deadline.engine import Core
from deadline.interactions import Information, InteractiveHelp, Function
from deadline.colorize import red, green, blue, cyan

def main():
    tasks = Core('data/tasks.txt')
    Information.info()
    
    run = True
    
    while run:
        cmd = input()
        tasks.open('data/tasks.txt')

        if cmd == 'help':
            Function.wn_clear()
            InteractiveHelp.help()
        
        elif cmd == 'license':
            Function.wn_clear()
            Information.license('LICENSE')
        
        elif cmd == 'l':
            Function.wn_clear()
            print(tasks)

        elif cmd == 'add':
            title = input(green("Write your task title: "))
            deadline = input(blue("Write your task deadline: "))
            tasks.add_task(title, deadline)
            Function.wn_clear()
            print(tasks)
        
        elif cmd == 'rm':
            idx = input(red("Enter the index of the task you want to remove: "))
            
            while not idx.isdigit():
                print(red("The task index is a positive integer"))
                idx = input(red("Please, re-enter your task index: "))
            
            idx = int(idx)
            InteractiveHelp.rm_helper(tasks, idx)
            tasks.remove_task(idx)
            Function.wn_clear()
            print(tasks)
        
        elif cmd == 'clear':
            Function.wn_clear()

        elif cmd == 'history':
            Information.history('data/history.txt')

        elif cmd == 'stop':
            run = False

        Function.historize(cmd, 'data/history.txt')
        tasks.close()
    
    print(cyan("The application has stopped running"))

    Function.clear_session_history(cmd, 'data/history.txt')

    return True

if __name__ == "__main__":
    main()
