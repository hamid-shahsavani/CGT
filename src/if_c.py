# Copyright SYS113 2019. gpl v3.0 license , see readme file.

from features import features
from clear import clear
from time import sleep
from pathlib import Path
from os.path import isfile
from platform import system as os_type

home = str(Path.home())

if os_type().upper() == 'WINDOWS':
    if isfile(home+'\\.CGT\\files\\LANGUAGE'):
        language = open(home + '\\.CGT\\files\\LANGUAGE', 'r').read()
elif os_type().upper() == 'LINUX':
    if isfile(home+'/.CGT/files/LANGUAGE'):
        language = open(home + '/.CGT/files/LANGUAGE', 'r').read()
else:
    pass

class c:
    BLUE = '\033[94m'
    GREEN = '\033[92m'
    RED = '\033[91m'

def if_c():
    if language == 'EN':
        print(c.BLUE+'clear '+c.RED+'screen'+c.BLUE+' .'+c.GREEN+'.'+c.RED+'.')
        sleep(2)
        clear()
        features()
    elif language == 'FA':
        print(c.RED+'tamiz'+c.BLUE+' kardan'+c.RED+' safhe '+c.BLUE+' .'+c.GREEN+'.'+c.RED+'.')
        sleep(2)
        clear()
        features()