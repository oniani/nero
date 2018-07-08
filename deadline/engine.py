class Core:
    def __init__(self, file):
        self.file = open(file, 'r+')
        self.tasks = list(line.split('|') for line in self.file)
        self.titles = list(task[0] for task in (self.tasks))
        self.deadlines = list(task[1] for task in (self.tasks))

    def __getitem__(self, idx):
        for i in range(len(self.titles)):
            if i == idx:
                return self.titles[i]

    def __len__(self):
        return len(self.titles)

    def __iter__(self):
        for i in range(len(self.titles)):
            yield self.titles[i]
    
    def __str__(self):
        max_tsk_len = len(max(self.titles, key=len))
        res = "Task" + "Deadline".rjust(27 + max_tsk_len, ' ')
        res += '\n' + '='.rjust(max_tsk_len + 31, '=') + '\n'

        for i in range(len(self.titles)):
            res += str(i+1) + '. ' + (len(str(len(self.titles)))-len(str(i+1))) * ' '
            res += self.titles[i]
            res += self.deadlines[i].rjust(max_tsk_len - len(self.titles[i]) + 28, ' ')
        
        return res

    def add_task(self, title, deadline):
        deadline += '\n'

        temp_titles = self.titles
        temp_deadlines = self.deadlines

        self.clear()

        self.file.write(title + '|' + deadline)

        self.titles.append(title)
        self.deadlines.append(deadline)

        for i in range(len(temp_titles)):
            self.file.write(temp_titles[i] + '|' + temp_deadlines[i])
            self.titles.append(temp_titles[i])
            self.deadlines.append(temp_deadlines[i])

    def remove_task(self, idx):
        if idx > 1:
            temp_titles = self.titles[:idx-1] + self.titles[idx:]
            temp_deadlines = self.deadlines[:idx-1] + self.deadlines[idx:]
        else:
            temp_titles = self.titles[1:]
            temp_deadlines = self.deadlines[1:]
            
        self.clear()

        for i in range(len(temp_titles)):
            self.file.write(temp_titles[i] + '|' + temp_deadlines[i])
            self.titles.append(temp_titles[i])
            self.deadlines.append(temp_deadlines[i])

    def open(self, file):
        self.file = open(file, 'r+')

    def clear(self):
        self.file.truncate(0)
        self.file.seek(0)
        self.tasks = list()
        self.titles = list()
        self.deadlines = list()

    def close(self):
        self.file.close()
