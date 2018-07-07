class Task:
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
        max_tsk_len = len(max(self.tasks, key=len))

        res += "Task" + 3 * max_tsk_len * ' ' + "Deadline"
        res += "\n" + (3 * max_tsk_len + 12) * '-' + '\n'

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
        temp = self.tasks[:idx-1] + self.tasks[idx:]

        self.clear()

        for task in temp:
            self.file.write(task)
            self.tasks.append(task)

    def open(self, file):
        self.file = open(file, 'r+')

    def clear(self):
        self.file.truncate(0)
        self.file.seek(0)
        self.tasks = list()

    def close(self):
        self.file.close()
