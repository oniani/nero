# SINCE THE FILE IS OPEN ALL THE TIME, FUNCTIONS DO NOT WORK IN COMBINATION...
# EITHER DEAL WITH THE FILE BEING OPEN ALL THE TIME BY USING 'open with' OR REWRITE THE CODE!!!

class Rocket:
    def __init__(self, tasks_file):
        self.file = open(tasks_file, 'r+')
        self.tasks = self.file.readlines()

    def add_task(self, new_task=""):
        new_task += '\n'
        temp = self.tasks

        self.clear()
        self.file.write(new_task)
        self.tasks.append(new_task)

        for task in temp:
            self.file.write(task)

    def remove_task(self, idx):
        if idx > len(self.tasks):
            print("Your task index cannot be greater than the number of tasks")
            return
        elif idx < 1:
            print("Your task index cannot be less than 1")
            return

        self.clear()

        self.tasks = self.tasks[:idx-1] + self.tasks[idx:]

        for i in range(len(self.tasks)):
            self.file.write(self.tasks[i])

    def update_task(self, idx, updated_task):
        updated_task += '\n'
        temp = self.tasks
        self.clear()

        for i in range(len(temp)):
            if i+1 == idx:
                self.file.write(updated_task)
            else:
                self.file.write(temp[i])

    def clear(self):
        self.file.truncate(0) # Remove everything from a file
        self.file.seek(0) # Set the pointer to the beginning so that the file is read from up to down (not necessary)
        self.tasks = list()
    
    def close(self):
        self.file.close()

tasks = Rocket("tasks.txt")
# tasks.remove_task(1)
# tasks.add_task("Hello, world!")
tasks.update_task(1, "Do NOT do dishes!")
# tasks.close()
# tasks.remove_task(1)