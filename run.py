from deadline.engine import Task
from deadline.interactions import Information, InteractiveHelp, Function

def main():
    file = 'data/tasks.txt'
    task = Task(file)
    Information().info()

    run = True
    
    while run:
        cmd = input()
        task.open(file)

        if cmd == 'help':
            Function().wn_clear()
            InteractiveHelp().help()
        
        elif cmd == 'license':
            Function().wn_clear()
            Information().license('LICENSE')
        
        elif cmd == 'lst':
            Function().wn_clear()
            print(task)

        elif cmd == 'add':
            title = input("Write your task title: ")
            deadline = input("Write your task deadline: ")
            task.add_task(title, deadline)
            Function().wn_clear()
            print(task)
        
        elif cmd == 'rem':
            task_idx = int(input("Enter the index of the task you want to remove: "))
            # InteractiveHelp().remove_helper(task, task_idx)
            task.remove_task(task_idx)
            Function().wn_clear()
            print(task)
        
        elif cmd == 'clear':
            Function().wn_clear()

        elif cmd == 'stop':
            run = False
        
        else:
            InteractiveHelp().give_hint_by_cmd(cmd);
        
        task.close()
    
    print("The application has stopped running")
    
    return True

if __name__ == "__main__":
    main()
