import os

class Information:
    def info():
        print("Deadline by David Oniani")
        print("Licensed under MIT")
        print("Copyright (c) 2018 David Oniani")
        print("Type 'help' or 'license' for more information")
    
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
        print("'l' - display all the tasks")
        print("'add' - add task")
        print("'rm' - remove task by its index")
        print("'stop' - stop running the application and save my edits")
    
    def give_hint_by_cmd(cmd):
        if cmd == 'l' or cmd == 'll' or cmd == 'L' or cmd == 'Ll' or cmd == 'lL':
            print("Did you mean 'lst' ?")

        elif cmd == 'ad' or cmd == 'addd' or cmd == 'da' or cmd == 'd' or cmd == 'dd':
            print("Did you mean 'add' ?")

        elif cmd == 'rm' or cmd == 'r' or cmd == 'm' or cmd == 'rmm' or cmd == 'rem':
            print("Did you mean 'rm' ?")
        
        elif cmd == 'sto' or cmd == 'stopp' or cmd == 'stoop' or cmd == 'stp' or cmd == 'st':
            print("Did you mean 'stop' ?")
        
        elif cmd == 'cle' or cmd == 'clearr' or cmd == 'cllar' or cmd == 'cller' or cmd == 'lear':
            print("Did you mean 'clear' ?")
        
        else:
            print("Sorry, I have nothing to offer for this request...")
            print("... but blood, boil, tears, and sweat.")
            print("Fortunately, there is a 'help' command which is a full manual for the app!")
    
    def rm_helper(task, idx):
        while idx > len(task):
            print("Your task index cannot be greater than the number of tasks")
            idx = int(input("Please, re-enter your task index: "))

        while idx < 1:
            print("Your task index cannot be less than 1")
            idx = int(input("Please, re-enter your task index: "))

class Function:
    def wn_clear():
        if os.name == 'nt':
            os.system('cls')
        else:
            os.system('clear')
    
    def historize(cmd, file):
        file = open(file, 'w')
        file.write(cmd)
    
    def clear_session_history(file):
        file = open(file, 'w')
        file.truncate(0)
        file.seek(0)
