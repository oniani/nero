import os

class Functions:
    def wn_clear(self):
        if os.name == 'nt':
            os.system('cls')
        else:
            os.system('clear')
    
    # Finish up the type check for the input
    # If user enters 'int' and 'string' is required, python quits...
    # Either exceptions or while loop...
    def type_check(self, n):
        while type(n) != 'int':
            prompt = input("The p")
