# Copyright SYS113 2019. gpl v3.0 license , see readme file.

from error import error
from platform import system as os_type
from platform import release as os_release
from pathlib import Path
from os.path import isfile

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
	YELLOW = '\033[33m'
	BLUE = '\033[94m'
	GREEN = '\033[92m'
	RED = '\033[91m'

if os_release() == '7':
	class c:
		YELLOW = ''
		BLUE = ''
		GREEN = ''
		RED = ''
else:
	class c:
		YELLOW = '\033[33m'
		BLUE = '\033[94m'
		GREEN = '\033[92m'
		RED = '\033[91m'

def if_else():
	if language == 'EN':
		print(c.RED + 'error' + c.GREEN+' : ' + c.BLUE + 'code '+c.YELLOW+'0' + c.GREEN+' | '+c.BLUE+'please see '+c.RED+'CGT-Files/EN-ErrorList.png'+c.BLUE+' .'+c.GREEN+'.'+c.RED+'.')
	if language == 'FA':
		print(c.RED+'khata'+c.GREEN+' : ' + c.BLUE + 'code '+c.YELLOW+'0' + c.GREEN+' | '+c.BLUE+'lotfan bbinid '+c.RED+'CGT-Files/FA-ErrorList.png'+c.BLUE+' .'+c.GREEN+'.'+c.RED+'.')
	error(0)
