from deadline.deadline import Deadline
from deadline.interaction import Interactions, InteractiveHelp
from deadline.terminal import Functions

def main():
    file = 'data/tasks.txt'
    deadline = Deadline(file)
    Interactions().info()

    run = True
    
    while run:
        cmd = input()
        deadline.open(file)

        if cmd == 'help':
            Functions().wn_clear()
            InteractiveHelp().help()
        
        elif cmd == 'license':
            Functions().wn_clear()
            Interactions().license('../LICENSE')
        
        elif cmd == 'show':
            Functions().wn_clear()
            print(deadline)

        elif cmd == 'add':
            new_task = input("Write your new task: ")
            deadline.add_task(new_task)
            Functions().wn_clear()
            print(deadline)
        
        elif cmd == 'rm':
            remove_line = input("Enter the index of the task you want to remove: ")
            deadline.remove_task(int(remove_line))
            Functions().wn_clear()
            print(deadline)
        
        elif cmd == 'clear':
            Functions().wn_clear()

        elif cmd == 'stop':
            run = False
        
        deadline.close()
    
    print("\nThe application has stopped running")
    
    return True

if __name__ == "__main__":
    main()
