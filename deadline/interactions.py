import os
from deadline.colorize import red

class Information:
    def info():
        print("Deadline by David Oniani")
        print("Licensed under MIT")
        print("Copyright (c) 2018 David Oniani")
        print("Type 'help' or 'license' for more information.")
    
    def license(file):
        file = open(file, 'r')
        for line in file.readlines():
            print(line, end='')
    
    def history(file):
        file = open(file, 'r')
        for line in file.readlines():
            print(line, end='')

class InteractiveHelp:
    def help():
        print("'ls' - list all tasks")
        print("'ls --ttl' - list titles only")
        print("'add' - list deadlines only")
        print("'rm' - remove task by its index")
        print("'h' - show command history for the current session")
        print("'clear' - clear the terminal window")
        print("'stop' - stop running the app and save my edits")

    def give_hint_by_cmd(cmd):
        if cmd == 'l' or cmd == 's' or cmd == 'Ls' or cmd == 'lS' or cmd == 'lss' or cmd == 'lls':
            print("Did you mean 'ls' ?")

        elif cmd == 'ad' or cmd == 'addd' or cmd == 'da' or cmd == 'd' or cmd == 'dd':
            print("Did you mean 'add' ?")

        elif cmd == 'rm' or cmd == 'r' or cmd == 'm' or cmd == 'rmm' or cmd == 'rem':
            print("Did you mean 'rm' ?")
        
        elif cmd == 'sto' or cmd == 'stopp' or cmd == 'stoop' or cmd == 'stp' or cmd == 'st':
            print("Did you mean 'stop' ?")
        
        elif cmd == 'cle' or cmd == 'clearr' or cmd == 'cllar' or cmd == 'cllear' or cmd == 'lear':
            print("Did you mean 'clear' ?")
        
        else:
            print(red("Sorry, this is an invalid command. Type 'help' for more information"))

class Function:
    def wn_clear():
        if os.name == 'nt':
            os.system('cls')
        else:
            os.system('clear')
