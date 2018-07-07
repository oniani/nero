class Interactions:
    def info(self):
        print("Deadline by David Oniani")
        print("Licensed under MIT")
        print("Copyright (c) 2018 David Oniani")
        print("Type 'help' or 'license' for more information")
    
    def license(self, file):
        self.file = open(file, 'r')
        for line in self.file.readlines():
            print(line, end='')

class InteractiveHelp:
    def help(self):
        print("'show' - display all the tasks")
        print("'add' - add task")
        print("'rem' - remove task by its index")
        print("'stop' - stop running the application and save my edits")
    
    def give_hint_by_cmd(self, cmd):
        if cmd == 'r' or cmd == 'mr' or cmd == 'm' or cmd == 'rmm' or cmd == 'rrm':
            print("Did you mean 'rm' ?")
    
        elif cmd == 'ad' or cmd == 'addd' or cmd == 'da' or cmd == 'd' or cmd == 'dd':
            print("Did you mean 'cmd' ?")
        
        elif cmd == 'ad' or cmd == 'addd' or cmd == 'da' or cmd == 'd' or cmd == 'dd':
            print("Did you mean 'cmd' ?")
        
        elif cmd == 'sto' or cmd == 'stopp' or cmd == 'stoop' or cmd == 'stp' or cmd == 'st':
            print("Did you mean 'stop' ?")
        
        elif cmd == 'cle' or cmd == 'clearr' or cmd == 'cllar' or cmd == 'cller' or cmd == 'lear':
            print("Did you mean 'clear' ?")
        
        else:
            print("Sorry, I have nothing to offer for this request...")
            print("... but blood, boil, tears, and sweat.")
            print("Fortunately, there is a 'help' command which is a full manual for the app!")
