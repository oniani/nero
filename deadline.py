class Deadline:
    def __init__(self, tasks_file):
        self.file = open(tasks_file, 'r+')
        self.tasks = self.file.readlines()

    def __getitem__(self, idx):
        for i in range(len(self.tasks)):
            if i == idx:
                return self.tasks[i]

    def __len__(self):
        return len(self.tasks)

    def __iter__(self):
        for i in range(len(self.tasks)):
            yield self.tasks[i]
    
    def __str__(self):
        res = ""
        for i in range(len(self.tasks)):
            res += str(i+1) + '. ' + self.tasks[i]
        return res

    def add_task(self, new_task=""):
        new_task += '\n'
        temp = self.tasks

        self.clear()
        self.file.write(new_task)
        self.tasks.append(new_task)

        for task in temp:
            self.file.write(task)
            self.tasks.append(task)

    def remove_task(self, idx):
        if idx > len(self.tasks):
            print("Your task index cannot be greater than the number of tasks")
            return
        elif idx < 1:
            print("Your task index cannot be less than 1")
            return

        temp = self.tasks[:idx-1] + self.tasks[idx:]

        self.clear()

        for task in temp:
            self.file.write(task)
            self.tasks.append(task)

    def update_task(self, idx, updated_task):
        updated_task += '\n'
        temp = self.tasks

        self.clear()

        for i in range(len(temp)):
            if i+1 == idx:
                self.file.write(updated_task)
                self.tasks.append(updated_task)
            else:
                self.file.write(temp[i])
                self.tasks.append(temp[i])


    def info(self):
        print("Deadline by David Oniani")
        print("Licensed under MIT")
        print("Copyright (c) 2018 David Oniani")
        print("Type 'help' for more information")
    
    def help(self):
        print("Deadline is the terminal app which helps you orginize your daily tasks")
        print("--------------------------------------------------------------------")
        print("Type 'show' to show all the tasks")
        print("You can add task by typing 'add' after which you can enter the new task on the prompted line")
        print("You can remove task by typing 'rem n' where n is the number of the task")
        print("Type 'stop' to stop running the program")


    def clear(self):
        self.file.truncate(0) # Remove everything from a file
        self.file.seek(0) # Set the pointer to the beginning so that the file is read from up to down (not necessary)
        self.tasks = list()

    def close(self):
        self.file.close()

def main():
    deadline = Deadline("tasks.txt")
    deadline.info()
    run = True

    print()

    while run:
        cmd = input()

        if cmd == "help":
            print()
            deadline.help()
            print()

        elif cmd == "show":
            print()
            print("--------------------------------------------")
            print(deadline)

        elif cmd == "add":
            new_task = input("Write your new task: ")
            deadline.add_task(new_task)
            print()
            print(deadline)
        
        elif cmd == "rm":
            remove_line = input("Enter the number of the task you want to remove: ")
            deadline.remove_task(int(remove_line))
            print()
            print(deadline)
        
        elif cmd == "stop":
            deadline.close()
            run = False
    
    print("\nThe program has stopped running")
    
    return True

if __name__ == "__main__":
    main()