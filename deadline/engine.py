'''
This is the app's primary engine
'''
import csv

class Core:
    '''
    Class contains the core functionalities of the app
    '''
    def __init__(self, filename):
        csv.register_dialect('nero', delimiter=',', lineterminator='\n', quotechar='"')
        self.filename = filename

        self.file = open(self.filename, 'r')
        self.task_reader = csv.reader(self.file, 'nero')

        self.titles = [task[0] for task in self.task_reader]
        self.file.seek(0)
        self.deadlines = [task[1] for task in self.task_reader]

        self.file.close()

    def __len__(self):
        return len(self.titles)

    def __getitem__(self, idx):
        if idx > len(self.titles) - 1:
            raise IndexError("Index is out of bounds")
        elif idx < 0:
            raise IndexError("Index cannot be less than 0")

        return self.titles[idx]

    def __iter__(self):
        for i in range(len(self.titles)):
            yield self.titles[i]

    def __str__(self):
        max_ttl_len = len(max(self.titles, key=len))
        max_ddl_len = len(max(self.deadlines, key=len))

        res = "Title" + ' ' * (max_ttl_len - len("Title") + 20) + "Deadline"
        res += '\n' + '='*(max_ttl_len + max_ddl_len + 20) + '\n'

        for idx, task in enumerate(zip(self.titles, self.deadlines)):
            res += str(idx+1) + '.'
            res += ''.join(word.ljust(max_ttl_len + 20) for word in task)
            res += '\n'

        return res

    def get_titles(self):
        '''Returns the list of all the task titles'''
        return self.titles

    def get_deadlines(self):
        '''Returns the list of all the task deadlines'''
        return self.deadlines

    def add_task(self, title, deadline):
        '''Adds new task'''
        file = open(self.filename, 'a')
        task_writer = csv.writer(file, 'nero')

        task_writer.writerow([title, deadline])
        self.titles.append(title)
        self.deadlines.append(deadline)

        file.close()

    def remove_task(self, idx):
        '''Removes task by the index'''
        file = open(self.filename, 'w')
        task_writer = csv.writer(file, 'nero')

        if idx > 1:
            self.titles = self.titles[:idx-1] + self.titles[idx:]
            self.deadlines = self.deadlines[:idx-1] + self.deadlines[idx:]
        else:
            self.titles = self.titles[1:]
            self.deadlines = self.deadlines[1:]

        task_writer.writerows(zip(self.titles, self.deadlines))

        file.close()

    def open(self, file):
        '''Opens the file'''
        self.file = open(file, 'r+')

    def close(self):
        '''Closes the file'''
        self.file.close()
