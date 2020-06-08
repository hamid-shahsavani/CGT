# Copyright SYS113 2019. gpl v3.0 license , see readme file.

from shutil import copyfile
from pathlib import Path
from os.path import isdir , isfile
from os import system , mkdir
from platform import system as os_type

home = str(Path.home())

def windows():
	if isfile(home+'\\.CGT\\files\\LANGUAGE'):
		language = open(home + '\\.CGT\\files\\LANGUAGE', 'r').read()
		if language == 'EN':
			if not isdir(home + '\\Desktop\\CGT-Files'):
				system('mkdir ' + home + '\\Desktop\\CGT-Files')
			if not isfile(home + '\\Desktop\\CGT-Files\\EN-ErrorList.png'):
				copyfile(home + '\\.CGT\\files\\EN-ErrorList.png', home + '\\Desktop\\CGT-Files\\EN-ErrorList.png')
			if not isfile(home + '\\Desktop\\CGT-Files\\EN-Readme.png'):
				copyfile(home + '\\.CGT\\files\\EN-Readme.png', home + '\\Desktop\\CGT-Files\\EN-Readme.png')
			if not isfile(home + '\\Desktop\\CGT-Files\\LICENSE'):
				copyfile(home + '\\.CGT\\files\\LICENSE', home + '\\Desktop\\CGT-Files\\LICENSE')
		elif language == 'FA':
			if not isdir(home + '\\Desktop\\CGT-Files'):
				system('mkdir ' + home + '\\Desktop\\CGT-Files')
			if not isfile(home + '\\Desktop\\CGT-Files\\FA-ErrorList.png'):
				copyfile(home + '\\.CGT\\files\\FA-ErrorList.png', home + '\\Desktop\\CGT-Files\\FA-ErrorList.png')
			if not isfile(home + '\\Desktop\\CGT-Files\\FA-Readme.png'):
				copyfile(home + '\\.CGT\\files\\FA-Readme.png', home + '\\Desktop\\CGT-Files\\FA-Readme.png')
			if not isfile(home + '\\Desktop\\CGT-Files\\LICENSE'):
				copyfile(home + '\\.CGT\\files\\LICENSE', home + '\\Desktop\\CGT-Files\\LICENSE')

def linux():
	if isfile(home+'/.CGT/files/LANGUAGE'):
		language = open(home + '/.CGT/files/LANGUAGE', 'r').read()
		if language == 'EN':
			if not isdir(home + '/Desktop/CGT-Files'):
				mkdir(home + '/Desktop/CGT-Files')
			if not isfile(home + '/Desktop/CGT-Files/EN-ErrorList.png'):
				copyfile(home + '/.CGT/files/EN-ErrorList.png', home + '/Desktop/CGT-Files/EN-ErrorList.png')
			if not isfile(home + '/Desktop/CGT-Files/EN-Readme.png'):
				copyfile(home + '/.CGT/files/EN-Readme.png', home + '/Desktop/CGT-Files/EN-Readme.png')
			if not isfile(home + '/Desktop/CGT-Files/LICENSE'):
				copyfile(home + '/.CGT/files/LICENSE', home + '/Desktop/CGT-Files/LICENSE')
			if not isfile(home + '/Desktop/CGT-Files/VERSION'):
				copyfile(home + '/.CGT/files/VERSION', home + '/Desktop/CGT-Files/VERSION')
			if not isfile(home + '/Desktop/CGT-Files/LANGUAGE'):
				copyfile(home + '/.CGT/files/LANGUAGE' , home + '/Desktop/CGT-Files/LANGUAGE')
		elif language == 'FA':
			if not isdir(home + '/Desktop/CGT-Files'):
				mkdir(home + '/Desktop/CGT-Files')
			if not isfile(home + '/Desktop/CGT-Files/FA-ErrorList.png'):
				copyfile(home + '/.CGT/files/FA-ErrorList.png', home + '/Desktop/CGT-Files/FA-ErrorList.png')
			if not isfile(home + '/Desktop/CGT-Files/EN-readme.png'):
				copyfile(home + '/.CGT/files/FA-Readme.png', home + '/Desktop/CGT-Files/FA-Readme.png')
			if not isfile(home + '/Desktop/CGT-Files/LICENSE'):
				copyfile(home + '/.CGT/files/LICENSE', home + '/Desktop/CGT-Files/LICENSE')
			if not isfile(home + '/Desktop/CGT-Files/VERSION'):
				copyfile(home + '/.CGT/files/VERSION', home + '/Desktop/CGT-Files/VERSION')
			if not isfile(home + '/Desktop/CGT-Files/LANGUAGE'):
				copyfile(home + '/.CGT/files/LANGUAGE' , home + '/Desktop/CGT-Files/LANGUAGE')

def cp():
	if os_type().upper() == 'WINDOWS':
		windows()
	elif os_type().upper() == 'LINUX':
		linux()
	else:
		pass
			  