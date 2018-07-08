from deadline.engine import Core
from deadline.interactions import Information, InteractiveHelp, Function

def main():
    file= 'data/tasks.txt'
    tasks = Core(file)
    Information.info()
    
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
        
        elif cmd == 'lst':
            Function.wn_clear()
            print(tasks)

        elif cmd == 'add':
            title = input("Write your task title: ")
            deadline = input("Write your task deadline: ")
            tasks.add_task(title, deadline)
            Function.wn_clear()
            print(tasks)
        
        elif cmd == 'rem':
            idx = int(input("Enter the index of the task you want to remove: "))
            InteractiveHelp.rem_helper(tasks, idx)
            tasks.remove_task(idx)
            Function.wn_clear()
            print(tasks)
        
        elif cmd == 'clear':
            Function.wn_clear()

        elif cmd == 'stop':
            run = False
        
        tasks.close()
    
    print("The application has stopped running")
    
    return True

if __name__ == "__main__":
    main()
