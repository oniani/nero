def default(text):
    return '\033\e[0;39m' + text + '\033[1;m'

def red(text):
    return '\033[1;31m' + text + '\033[1;m'

def green(text):
    return '\033[1;32m' + text + '\033[1;m'

def blue(text):
    return '\033[1;34m' + text + '\033[1;m'

def yellow(text):
    return '\033[1;33' + text + '\033[1;m'

def magenta(text):
    return '\033[1;35m' + text + '\033[1;m'

def cyan(text):
    return '\033[1;36m' + text + '\033[1;m'

def black(text):
    return '\033[1;30m' + text + '\033[1;m'

def white(text):
    return '\033[1;37m' + text + '\033[1;m'
