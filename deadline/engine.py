'''
This is the app's primary engine
'''
import csv

class Core:
    '''
    Class contains the core functionalities of the app
    '''
    def __init__(self, file):
        self.file = open(file)
        self.tasks = csv.reader(self.file, delimiter='|')
        self.titles = [task[0] for task in self.tasks]
        self.file.seek(0)
        self.deadlines = [task[1] for task in self.tasks]

    def __len__(self):
        return len(self.titles)

    def __getitem__(self, idx):
        if idx > len(self.titles) - 1:
            raise IndexError("Index is out of bounds")

        for i in range(len(self.titles)):
            if i == idx:
                return self.titles[i]

    def __iter__(self):
        for i in range(len(self.titles)):
            yield self.titles[i]

    def __str__(self):
        max_ttl_len = len(max(self.titles, key=len))
        max_ddl_len = len(max(self.deadlines, key=len))

        res = "Title" + ' ' * (max_ttl_len - len("Title") + 20) + "Deadline"
        res += '\n' + '='*(max_ttl_len + max_ddl_len + 20) + '\n'

        for idx, task in enumerate(zip(self.titles, self.deadlines)):
            res += str(idx+1) + '.' + "".join(word.ljust(max_ttl_len + 20) for word in task) + '\n'

        return res

    def get_titles(self):
        '''Returns the list of all the task titles'''
        return self.titles

    def get_deadlines(self):
        '''Returns the list of all the task deadlines'''
        return self.deadlines

    def add_task(self, new_title, new_deadline):
        '''Adds new task'''
        temp_titles = self.titles
        temp_deadlines = self.deadlines

        self.clear()
        self.file.write(new_title + '|' + new_deadline + '\n')
        self.titles.append(new_title)
        self.deadlines.append(new_deadline + '\n')

        for title, deadline in zip(temp_titles, temp_deadlines):
            self.file.write(title + '|' + deadline)
            self.titles.append(title)
            self.deadlines.append(deadline)

    def remove_task(self, idx):
        '''Removes task by the index'''
        if idx > 1:
            temp_titles = self.titles[:idx-1] + self.titles[idx:]
            temp_deadlines = self.deadlines[:idx-1] + self.deadlines[idx:]
        else:
            temp_titles = self.titles[1:]
            temp_deadlines = self.deadlines[1:]

        self.clear()

        for title, deadline in zip(temp_titles, temp_deadlines):
            self.file.write(title + '|' + deadline)
            self.titles.append(title)
            self.deadlines.append(deadline)

    def open(self, file):
        '''Opens the file'''
        self.file = open(file, 'r+')

    def clear(self):
        '''Clears all the data from the file as well as from the variables'''
        self.file.truncate(0)
        self.file.seek(0)
        self.tasks = []
        self.titles = []
        self.deadlines = []

    def close(self):
        '''Closes the file'''
        self.file.close()
