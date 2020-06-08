# Copyright SYS113 2019. gpl v3.0 license , see readme file.

from os import system
from platform import system as os_type
def clear():
    if os_type().upper() == 'WINDOWS':
        system('cls')
    elif os_type().upper() == 'LINUX':
        system('clear')
    else:
    	pass