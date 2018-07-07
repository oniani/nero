import os

class Terminal:
    def clear(self):
        if os.name == 'nt':
            os.system('cls')
        else:
            os.system('clear')
