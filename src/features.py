# Copyright SYS113 2019. gpl v3.0 license , see readme file.

from line import line
from clear import clear
from platform import system as os_type
from platform import release as os_release
from os.path import isfile , isdir
from pathlib import Path
from requests import get
from tzlocal import get_localzone
from shutil import move
from re import sub

version = '0.1.1'

home = str(Path.home())

if os_type().upper() == 'WINDOWS':
	Lang = home+'\\.CGT\\files\\LANGUAGE'
	if isfile(home+'\\.CGT\\files\\LANGUAGE'):
		language = open(home + '\\.CGT\\files\\LANGUAGE', 'r').read()
		version = open(home + '\\.CGT\\files\\VERSION', 'r').read()
elif os_type().upper() == 'LINUX':
	Lang = home+'/.CGT/files/LANGUAGE'
	if isfile(home+'/.CGT/files/LANGUAGE'):
		language = open(home + '/.CGT/files/LANGUAGE', 'r').read()
		version = open(home + '/.CGT/files/VERSION', 'r').read()
else:
	pass
	
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
		
def features():
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
	if isfile(Lang):
		if language == 'EN':
			clear()
			print(line())
			print('\t\t\t              ' + c.RED + ':' + c.GREEN + ':' + c.BLUE + ': ' +c.RED+ version + c.GREEN + ' - ' + c.BLUE + 'C' + c.GREEN + 'G' + c.RED + 'T' + c.GREEN + ' - '+ c.RED + language + c.BLUE +' :' + c.GREEN + ':' + c.RED + ':')
			print(line())
			print(c.END +c.RED + '           c' + c.BLUE + '.' + c.YELLOW + 'clear screen'+'          '+c.RED+'z'+c.BLUE+'.'+c.YELLOW+'change language to'+c.GREEN+' : '+c.RED+'persian'+'            '+c.RED + 'e' + c.BLUE + '.' + c.YELLOW + 'exit from CGT')
			print(line())
			print(c.END + c.RED + ' 1' + c.BLUE + '.' + c.YELLOW + 'convert' + c.GREEN + ' .img.lz4 ' + c.YELLOW + 'to' + c.GREEN + ' .img')
			print(c.END + c.RED + ' 2' + c.BLUE + '.' + c.YELLOW + 'unpack '+c.GREEN+'boot'+c.RED+'/'+c.GREEN+'recovery')
			print(c.END + c.RED + ' 3' + c.BLUE + '.' + c.YELLOW + 'repack '+c.GREEN+'boot'+c.RED+'/'+c.GREEN+'recovery')
			print(c.END + c.RED + ' 4' + c.BLUE + '.' + c.YELLOW + 'bypass screen lock'+c.RED+' - '+c.YELLOW+'samsung'+c.RED+' - '+c.YELLOW+'method one '+c.GREEN+'['+c.RED+'need to boot'+c.GREEN+']')
			print(c.END + c.RED + ' 5' + c.BLUE + '.' + c.YELLOW + 'generate imei')
		elif language == 'FA':
			clear()
			print(line())
			print('\t\t\t              ' + c.RED + ':' + c.GREEN + ':' + c.BLUE + ': ' +c.RED+ version + c.GREEN + ' - ' + c.BLUE + 'C' + c.GREEN + 'G' + c.RED + 'T' + c.GREEN + ' - '+ c.RED + language + c.BLUE +' :' + c.GREEN + ':' + c.RED + ':')
			print(line())
			print(c.END +c.RED + '           e' + c.BLUE + '.' + c.YELLOW + 'khoroj az CGT'+'          '+c.RED+'z'+c.BLUE+'.'+c.YELLOW+'taghir zaban be'+c.GREEN+' : '+c.RED+'english'+'          '+c.RED + 'c' + c.BLUE + '.' + c.YELLOW + 'tamiz kardan safhe')
			print(line())
			print(c.END + c.RED + ' 1' + c.BLUE + '.' + c.YELLOW + 'tabdil' + c.GREEN + ' .img.lz4 ' + c.YELLOW + 'be' + c.GREEN + ' .img')
			print(c.END + c.RED + ' 2' + c.BLUE + '.' + c.YELLOW + 'estekhraj '+c.GREEN+'boot'+c.RED+'/'+c.GREEN+'recovery')
			print(c.END + c.RED + ' 3' + c.BLUE + '.' + c.YELLOW + 'feshorde kardan dobare '+c.GREEN+'boot'+c.RED+'/'+c.GREEN+'recovery')
			print(c.END + c.RED + ' 4' + c.BLUE + '.' + c.YELLOW + 'dor zadan ghofle safhe'+c.RED+' - '+c.YELLOW+'samsung '+c.RED+' - '+c.YELLOW+'ravesh aval '+c.GREEN+'['+c.RED+'niaz be boot'+c.GREEN+']')
			print(c.END + c.RED + ' 5' + c.BLUE + '.' + c.YELLOW + 'tolid imei')
	else:
		if _language == 'TEHRAN':
			clear()
			print(line())
			print('\t\t\t              ' + c.RED + ':' + c.GREEN + ':' + c.BLUE + ': ' +c.RED+ version + c.GREEN + ' - ' + c.BLUE + 'C' + c.GREEN + 'G' + c.RED + 'T' + c.GREEN + ' - '+ c.RED + 'FA' + c.BLUE +' :' + c.GREEN + ':' + c.RED + ':')
			print(line())
			print(c.END +c.RED + '           e' + c.BLUE + '.' + c.YELLOW + 'khoroj az CGT'+'          '+c.RED+'z'+c.BLUE+'.'+c.YELLOW+'taghir zaban be'+c.GREEN+' : '+c.RED+'english'+'          '+c.RED + 'c' + c.BLUE + '.' + c.YELLOW + 'tamiz kardan safhe')
			print(line())
			print(c.END + c.RED + ' 1' + c.BLUE + '.' + c.YELLOW + 'tabdil' + c.GREEN + ' .img.lz4 ' + c.YELLOW + 'be' + c.GREEN + ' .img')
			print(c.END + c.RED + ' 2' + c.BLUE + '.' + c.YELLOW + 'estekhraj '+c.GREEN+'boot'+c.RED+'/'+c.GREEN+'recovery')
			print(c.END + c.RED + ' 3' + c.BLUE + '.' + c.YELLOW + 'feshorde kardan dobare '+c.GREEN+'boot'+c.RED+'/'+c.GREEN+'recovery')
			print(c.END + c.RED + ' 4' + c.BLUE + '.' + c.YELLOW + 'dor zadan ghofle safhe'+c.RED+' - '+c.YELLOW+'samsung '+c.RED+' - '+c.YELLOW+'ravesh aval '+c.GREEN+'['+c.RED+'niaz be boot'+c.GREEN+']')
			print(c.END + c.RED + ' 5' + c.BLUE + '.' + c.YELLOW + 'tolid imei')
		elif _language != 'TEHRAN':
			clear()
			print(line())
			print('\t\t\t              ' + c.RED + ':' + c.GREEN + ':' + c.BLUE + ': ' +c.RED+version+ c.GREEN + ' - ' + c.BLUE + 'C' + c.GREEN + 'G' + c.RED + 'T' + c.GREEN + ' - '+ c.RED + 'EN' + c.BLUE +' :' + c.GREEN + ':' + c.RED + ':')
			print(line())
			print(c.END +c.RED + '           c' + c.BLUE + '.' + c.YELLOW + 'clear screen'+'          '+c.RED+'z'+c.BLUE+'.'+c.YELLOW+'change language to'+c.GREEN+' : '+c.RED+'persian'+'            '+c.RED + 'e' + c.BLUE + '.' + c.YELLOW + 'exit from CGT')
			print(line())
			print(c.END + c.RED + ' 1' + c.BLUE + '.' + c.YELLOW + 'convert' + c.GREEN + ' .img.lz4 ' + c.YELLOW + 'to' + c.GREEN + ' .img')
			print(c.END + c.RED + ' 2' + c.BLUE + '.' + c.YELLOW + 'unpack '+c.GREEN+'boot'+c.RED+'/'+c.GREEN+'recovery')
			print(c.END + c.RED + ' 3' + c.BLUE + '.' + c.YELLOW + 'repack '+c.GREEN+'boot'+c.RED+'/'+c.GREEN+'recovery')
			print(c.END + c.RED + ' 4' + c.BLUE + '.' + c.YELLOW + 'bypass screen lock'+c.RED+' - '+c.YELLOW+'samsung'+c.RED+' - '+c.YELLOW+'method one '+c.GREEN+'['+c.RED+'need to boot'+c.GREEN+']')
			print(c.END + c.RED + ' 5' + c.BLUE + '.' + c.YELLOW + 'generate imei')
