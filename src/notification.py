# Copyright SYS113 2019. gpl v3.0 license , see readme file.

from platform import system as os_type
from platform import release as os_release
from os.path import isfile , isdir
from pathlib import Path
from requests import get
from line import line
from tzlocal import get_localzone
from shutil import move
from re import sub
from loading import loading

_language = str(get_localzone())

home = (str(Path.home()))

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

def windows():
	if not isdir(home+'\\.CGT'):
		if not isfile(home+'\\CITY'):
			city= open(home+'\\CITY','w')
			city.write(sub(r'.*/', '', str(get_localzone())).upper())
			city.close()
	if isdir(home+'\\.CGT'):
		if not isfile(home+'\\.CGT\\files\\CITY'):
			move(home+'\\CITY',home+'\\.CGT\\files\\CITY')
	try:
		_language = open(home+'\\CITY','r').read()
	except:
		_language = open(home+'\\.CGT\\files\\CITY','r').read()
	CGT_VERSION = '0.1.2'
	if isfile(home + '\\.CGT\\files\\VERSION'):
		language = open(home + '\\.CGT\\files\\LANGUAGE', 'r').read()
		if language == 'EN':
			try:
				curent_version = open(home + '\\.CGT\\files\\VERSION','r').read()
				latest_version = get('https://raw.githubusercontent.com/sys113/CGT-dependencies/master/VERSION').text
				if latest_version > curent_version:
					if latest_version > CGT_VERSION:
						print(c.BLUE+'version '+c.RED+latest_version+c.BLUE+' released'+c.GREEN+' : '+c.RED+'https://github.com/SYS113/CGT/releases')
						print(line())
				else:
					pass
			except:
				pass
		if language == 'FA':
			try:
				curent_version = open(home + '\\.CGT\\files\\VERSION','r').read()
				latest_version = get('https://raw.githubusercontent.com/sys113/CGT-dependencies/master/VERSION').text
				if latest_version > curent_version:
					if latest_version > CGT_VERSION:
						print(c.BLUE+'noskhe '+c.RED+latest_version+c.BLUE+' montasher shod'+c.GREEN+' : '+c.RED+'https://github.com/SYS113/CGT/releases')
						print(line())
				else:
					pass
			except:
				pass

def notification():
	if os_type().upper() == 'WINDOWS':
		a = loading(function=windows)
	elif os_type().upper() == 'LINUX':
		linux()
	else:
		pass
