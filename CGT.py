# Copyright SYS113 2019. gpl v3.0 license , see readme file.

from sys import path ; path.insert(1, 'src')
from platform import system as os_type
from platform import release as os_release
from line import line
from screensize import screensize
from download import download 
from cp import cp
from features import features
from notification import notification
from if_c import if_c 
from if_e import if_e
from if_z import if_z
from if_1 import if_1
from if_2 import if_2
from if_3 import if_3
from if_4 import if_4
from if_5 import if_5
from if_else import if_else

def xinput(s, *args, **kwargs):
	print(s, end='')
	return input('')

def _run(f):
    def wrapper(*args, **kwargs):
        if not wrapper.has_run:
            wrapper.has_run = True
            return f(*args, **kwargs)
    wrapper.has_run = False
    return wrapper

if os_release() == '7':
	class c:
		YELLOW = ''
		BLUE = ''
		GREEN = ''
		RED = ''
		CYAN = ''
		BOLD = ''
		END = ''
else:
	class c:
		YELLOW = '\033[33m'
		BLUE = '\033[94m'
		GREEN = '\033[92m'
		RED = '\033[91m'
		CYAN = '\033[36m'
		BOLD = '\033[1m'
		END = '\033[0m'

check_new_ver = _run(notification) 

def main():
	while True:
		print(line())
		# check_new_ver() # coming soon ...
		send = xinput(c.BLUE+">"+c.GREEN+">"+c.RED+"> "+c.CYAN)
		if send == 'c':
			if_c()
		elif send == 'e':
			if_e()
		elif send == 'z':
			if_z()
		elif send == '1':
			if_1()
		elif send == '2': 
			if_2()
		elif send == '3':
			if_3()
		elif send == '4':
			if_4()
		elif send == '5':
			if_5()
		else:
			if_else()

if os_type().upper() == 'WINDOWS':
	screensize()
	features()
	download()
	cp()
	main()
elif os_type().upper() == 'LINUX':
	print(c.END+c.BLUE+'support only'+c.GREEN+' windows'+c.RED+' , '+c.GREEN+'GNU/Linux'+c.BLUE+' version coming soon '+c.RED+'.'+c.GREEN+'.'+c.BLUE+'.')
	xinput('')
else:
	pass
