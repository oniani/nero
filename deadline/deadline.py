class Deadline:
    def __init__(self, file):
        self.file = open(file, 'r+')
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

        '''
        Modifications has to be made to '__str__' method in order to format the output
        '''
        # res += "Task"
        # res += 2 * len(max(self.tasks, key=len)) * ' '
        # res += "Deadline\n"
        # res += 3 * len(max(self.tasks, key=len)) * '-'

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

    def open(self, file):
        self.file = open(file, 'r+')

    def clear(self):
        self.file.truncate(0) # Remove everything from a file
        self.file.seek(0) # Set the pointer to the beginning so that the file is read from up to down (not necessary)
        self.tasks = list()

    def close(self):
        self.file.close()
