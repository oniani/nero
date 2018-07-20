"""Terminal coloration"""

def red(text):
    """Make text red"""
    return '\033[1;31m' + text + '\033[1;m' + '\033[m'

def green(text):
    """Make text green"""
    return '\033[1;32m' + text + '\033[1;m' + '\033[m'

def blue(text):
    """Make text blue"""
    return '\033[1;34m' + text + '\033[1;m' + '\033[m'

def yellow(text):
    """Make text yellow"""
    return '\033[1;33m' + text + '\033[1;m' + '\033[m'

def magenta(text):
    """Make text magenta"""
    return '\033[1;35m' + text + '\033[1;m' + '\033[m'

def cyan(text):
    """Make text cyan"""
    return '\033[1;36m' + text + '\033[1;m' + '\033[m'

def black(text):
    """Make text black"""
    return '\033[1;30m' + text + '\033[1;m' + '\033[m'

def white(text):
    '''Make text white'''
    return '\033[1;37m' + text + '\033[1;m' + '\033[m'
