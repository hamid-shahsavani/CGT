# Copyright SYS113 2019. gpl v3.0 license , see readme file.

from time import sleep
from sys import exit
from pathlib import Path
from platform import system as os_type
from platform import release as os_release
from os.path import isfile

home = (str(Path.home()))

if os_type().upper() == 'WINDOWS':
    if isfile(home+'\\.CGT\\files\\LANGUAGE'):
        language = open(home + '\\.CGT\\files\\LANGUAGE', 'r').read()
elif os_type().upper() == 'LINUX':
    if isfile(home+'/.CGT/files/LANGUAGE'):
        language = open(home + '/.CGT/files/LANGUAGE', 'r').read()
else:
  pass

if os_release() == '7':
	class c:
		BLUE = ''
		GREEN = ''
		RED = ''
else:
	class c:
		BLUE = '\033[94m'
		GREEN = '\033[92m'
		RED = '\033[91m'

def if_e():
  if language == 'FA':
    print(c.RED+'khoroj'+c.BLUE+' az '+c.GREEN+'CGT'+c.BLUE+' .'+c.GREEN+'.'+c.RED+'.')
  else:
    print(c.RED+'exit'+c.BLUE+' from '+c.GREEN+'CGT'+c.BLUE+' .'+c.GREEN+'.'+c.RED+'.')
  sleep(2)
  exit()
