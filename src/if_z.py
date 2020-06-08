# Copyright SYS113 2019. gpl v3.0 license , see readme file.

from pathlib import Path
from time import sleep , strftime
from os import system , execv , chdir 
from platform import system as os_type
from os.path import isfile , isdir
from error import error
from shutil import move
from sys import executable , exit , argv
from shutil import rmtree

home = (str(Path.home()))

if os_type().upper() == 'WINDOWS':
	if isfile(home+'\\.CGT\\files\\LANGUAGE'):
		_lang = open(home + '\\.CGT\\files\\LANGUAGE', 'r').read()
elif os_type().upper() == 'LINUX':
	if isfile(home+'/.CGT/files/LANGUAGE'):
		_lang = open(home + '/.CGT/files/LANGUAGE', 'r').read()
else:
	pass

class c:
	BLUE = '\033[94m'
	GREEN = '\033[92m'
	RED = '\033[91m'
	YELLOW = '\033[33m'
	END = '\033[0m'

def if_z():
	chdir(open(home+'\\.CGT\\files\\DIR','r').read())
	current_time = strftime("%H-%M-%S")
	if _lang == 'EN':
		if(isdir(home+'\\Desktop\\CGT-Files\\1')) or (isdir(home+'\\Desktop\\CGT-Files\\2')) or (isdir(home+'\\Desktop\\CGT-Files\\3')) or (isdir(home+'\\Desktop\\CGT-Files\\4')) or (isdir(home+'\\Desktop\\CGT-Files\\5')):
			if not isdir(home+'\\Desktop\\CGT-Backup\\'):
				print(c.BLUE+'creating'+c.RED+' CGT-Backup '+c.BLUE+'directory'+c.BLUE+' .'+c.GREEN+'.'+c.RED+'.')
				system('mkdir '+ home+'\\Desktop\\CGT-Backup\\')
			try:
				move(home+'\\Desktop\\CGT-Files',home+'\\Desktop\\CGT-Backup\\CGT-Backup-'+current_time)
			except:
				sleep(1)
				print(c.RED + 'error' + c.GREEN+' : ' + c.BLUE + 'code '+c.YELLOW+'24' + c.GREEN+' | '+c.BLUE+'please see '+c.RED+'CGT-Files/EN-ErrorList.png'+c.BLUE+' .'+c.GREEN+'.'+c.RED+'.')
				error(24)
				return
			sleep(1)
			print(c.RED+'CGT-Files '+c.BLUE+'directory'+c.RED+' renamed '+c.BLUE+'to'+c.RED+' CGT-Backup-'+current_time+c.BLUE+' .'+c.GREEN+'.'+c.RED+'.')
			sleep(1)
			print(c.RED+'CGT-Backup-'+current_time+c.BLUE+' directory '+c.RED+'moved'+c.BLUE+' to '+c.RED+'CGT-Backup'+c.BLUE+' .'+c.GREEN+'.'+c.RED+'.')
		else:
			sleep(1)
			print(c.RED+'remove'+c.GREEN+' & '+c.RED+'create again'+c.GREEN+' CGT-Files '+c.BLUE+'directroy '+c.RED+'.'+c.GREEN+'.'+c.BLUE+'.')
			try:
				rmtree(home+'\\Desktop\\CGT-Files')
			except:
				sleep(1)
				print(c.RED + 'error' + c.GREEN+' : ' + c.BLUE + 'code '+c.YELLOW+'24' + c.GREEN+' | '+c.BLUE+'please see '+c.RED+'CGT-Files/EN-ErrorList.png'+c.BLUE+' .'+c.GREEN+'.'+c.RED+'.')
				error(24)
				return	
		Lang = open(home + '\\.CGT\\files\\LANGUAGE', 'w')
		Lang.write('FA')
		Lang.close()
		sleep(1)
		print(c.BLUE+'language'+c.RED+' changed'+c.BLUE+' to '+c.RED+'persian'+c.BLUE+' .'+c.GREEN+'.'+c.RED+'.')
		sleep(1)
		print(c.BLUE+'restart '+c.RED+'.'+c.GREEN+'.'+c.BLUE+'.'+c.END)
		sleep(2)
		chdir(open(home+'\\.CGT\\files\\DIR','r').read())
		execv(executable, ['python'] + argv)
	elif _lang == 'FA':
		if(isdir(home+'\\Desktop\\CGT-Files\\1')) or (isdir(home+'\\Desktop\\CGT-Files\\2')) or (isdir(home+'\\Desktop\\CGT-Files\\3')) or (isdir(home+'\\Desktop\\CGT-Files\\4')) or (isdir(home+'\\Desktop\\CGT-Files\\5')):
			if not isdir(home+'\\Desktop\\CGT-Backup\\'):
				print(c.RED+'ijad'+c.BLUE+' poshe'+c.RED+' CGT-Backup '+c.BLUE+' .'+c.GREEN+'.'+c.RED+'.')
				system('mkdir '+ home+'\\Desktop\\CGT-Backup\\')
			try:
				move(home+'\\Desktop\\CGT-Files',home+'\\Desktop\\CGT-Backup\\CGT-Backup-'+current_time)
			except:
				sleep(1)
				print(c.RED+'khata'+c.GREEN+' : ' + c.BLUE + 'code '+c.YELLOW+'24' + c.GREEN+' | '+c.BLUE+'lotfan bbinid '+c.RED+'CGT-Files/FA-ErrorList.png'+c.BLUE+' .'+c.GREEN+'.'+c.RED+'.')
				error(24)
				return
			sleep(1)
			print(c.RED+'name'+c.BLUE+' poshe '+c.RED+'CGT-Files'+c.BLUE+' taghir kard be '+c.RED+'CGT-Backup-'+current_time+c.BLUE+' .'+c.GREEN+'.'+c.RED+'.')
			sleep(1)
			print(c.RED+'enteghal'+c.BLUE+' poshe '+c.RED+'CGT-Backup-'+current_time+c.BLUE+' be '+c.RED+'CGT-Backup'+c.BLUE+' .'+c.GREEN+'.'+c.RED+'.')
		else:
			print(c.RED+'hazf'+c.GREEN+' & '+c.RED+'sakht dobare'+c.BLUE+' poshe '+c.RED+'CGT-Files'+c.BLUE+' .'+c.GREEN+'.'+c.RED+'.')
			try:
				rmtree(home+'\\Desktop\\CGT-Files')
			except:
				sleep(1)
				print(c.RED+'khata'+c.GREEN+' : ' + c.BLUE + 'code '+c.YELLOW+'24' + c.GREEN+' | '+c.BLUE+'lotfan bbinid '+c.RED+'CGT-Files/FA-ErrorList.png'+c.BLUE+' .'+c.GREEN+'.'+c.RED+'.')
				error(24)
				return		
		Lang = open(home + '\\.CGT\\files\\LANGUAGE', 'w')
		Lang.write('EN')
		Lang.close()
		sleep(1)
		print(c.BLUE+'zaban'+c.RED+' taghir kard'+c.BLUE+' be '+c.RED+'english'+c.BLUE+' .'+c.GREEN+'.'+c.RED+'.')
		sleep(1)
		print(c.BLUE+'shoro\'e'+c.RED+' dobare '+c.BLUE+'.'+c.GREEN+'.'+c.RED+'.'+c.END)
		sleep(2)
		chdir(open(home+'\\.CGT\\files\\DIR','r').read())
		execv(executable, ['python'] + argv)
