# Copyright SYS113 2019. gpl v3.0 license , see readme file.

from os import system
from platform import system as os_type

def screensize():
	if os_type().upper() == 'WINDOWS':
		system('mode con: cols=103 lines=50')
	elif os_type().upper() == 'LINUX':
		system('resize -s 50 103 > /dev/null')
	else:
		pass