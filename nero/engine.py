"""
Engine module

David Oniani
Licensed under MIT
"""


import csv


class Core:
    """This class contains the core functionalities of the app."""
    def __init__(self, filename: str) -> None:
        """Initializer magic method."""
        csv.register_dialect('nero', delimiter=',', lineterminator='\n')
        self._filename = filename

        file = open(self._filename, 'r')
        self._task_reader = csv.reader(file, 'nero')

        self._titles = [task[0] for task in self._task_reader]
        file.seek(0)
        self._deadlines = [task[1] for task in self._task_reader]

        file.close()

    def __len__(self) -> int:
        """Return the length of the list for titles."""
        return len(self._titles)

    def __getitem__(self, idx) -> int:
        """Return the item with the given index from the list for titles."""
        if idx > len(self._titles) - 1:
            raise IndexError("Index is out of bounds")
        elif idx < 0:
            raise IndexError("Index cannot be less than 0")

        return self._titles[idx]

    def __iter__(self) -> None:
        """The default '__iter__' iterates over the list for titles."""
        for i in range(len(self._titles)):
            yield self._titles[i]

    def __str__(self) -> str:
        """The string representation for the class."""
        try:
            max_ttl_len = len(max(self._titles, key=len))
            max_ddl_len = len(max(self._deadlines, key=len))
        except Exception:
            max_ttl_len = max_ddl_len = 0

        res = "N   Title" + \
            ' ' * (max_ttl_len - len("Title") + 13) + "Deadline"

        if len(self) != 0:
            res += '\n' + '=' * (max_ttl_len + max_ddl_len + 17) + '\n'
        else:
            res += '\n' + '=' * 25 + '\n'

        for idx, task in enumerate(zip(self._titles[1:], self._deadlines[1:])):
            res += str(idx) + '.' + ''.rjust(3 - len(str(idx)))
            res += ''.join(word.ljust(max_ttl_len + 13) for word in task)
            res += '\n'

        return res

    def get_titles(self) -> list:
        """Return the list of task titles."""
        return self._titles

    def get_deadlines(self) -> list:
        """Return the list of task deadlines."""
        return self._deadlines

    def add_task(self, title, deadline) -> None:
        """Add a new task."""
        file = open(self._filename, 'a')
        task_writer = csv.writer(file, 'nero')

        task_writer.writerow([title, deadline])
        self._titles.append(title)
        self._deadlines.append(deadline)

        file.close()

    def remove_task(self, idx) -> None:
        """Remove a task by the index."""
        file = open(self._filename, 'w')
        task_writer = csv.writer(file, 'nero')

        del self._titles[idx+1]
        del self._deadlines[idx+1]

        task_writer.writerows(zip(self._titles, self._deadlines))

        file.close()
