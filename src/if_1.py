# Copyright SYS113 2019. gpl v3.0 license , see readme file.

try:
	from os import startfile	
except:
	pass
from pathlib import Path
from os import chdir , system , stat , remove
from os.path import isfile , isdir , exists  , splitext , basename , realpath
from error import error
from time import sleep
from shutil import rmtree , move
from platform import system as os_type

def xinput(s, *args, **kwargs):
    print(s, end='')
    return input('')

class c:
  MAGENTA = '\033[35m'
  YELLOW = '\033[33m'
  CYAN = '\033[36m'
  BLUE = '\033[94m'
  DARKCYAN = '\033[96m'
  GREEN = '\033[92m'
  RED = '\033[91m'
  GRAY = '\033[90m'
  BOLD = '\033[1m'
  WHITE = '\033[37m'
  END = '\033[0m'

home = (str(Path.home()))

if os_type().upper() == 'WINDOWS':
	if isfile(home+'\\.CGT\\files\\LANGUAGE'):
		language = open(home + '\\.CGT\\files\\LANGUAGE', 'r').read()
elif os_type().upper() == 'LINUX':
	if isfile(home+'/.CGT/files/LANGUAGE'):
		language = open(home + '/.CGT/files/LANGUAGE', 'r').read()
else:
	pass

def windows():
	if language == 'EN':
		print(c.END+c.BLUE+'drag'+c.RED+' & '+c.BLUE +'drop'+c.GREEN+' .img.lz4 '+c.RED+'file type'+c.BLUE+' and press'+c.RED+' enter ' + c.BLUE +'key'+ c.RED+' .'+c.GREEN+'.'+c.BLUE+'.')
		img_lz4_file = xinput(c.MAGENTA+'> '+c.YELLOW)
		if ' ' in img_lz4_file:
			print(c.END + c.RED + 'error' + c.GREEN+' : ' + c.BLUE + 'code '+c.YELLOW+'2' + c.GREEN+' | '+c.BLUE+'please see '+c.RED+'CGT-Files/ErrorList.png'+c.BLUE+' .'+c.GREEN+'.'+c.RED+'.')
			error(2)
		else:
			img_file = img_lz4_file.replace('.lz4', '')
			img_lz4_file = img_lz4_file.replace("\"", "")
			img_lz4_file = img_lz4_file.replace("\'", "")
			file_name, file_extension = splitext(img_lz4_file)
			img_unpack = img_lz4_file.replace('.lz4', '')
			if exists(img_lz4_file) == True:
				if file_extension == '.lz4':
					if isdir(home + "\\Desktop\\CGT-Files\\1\\"):
						try:
						  sleep(1)
						  print(c.END+c.RED+'directory'+c.YELLOW+' 1 '+c.BLUE + 'already exists'+c.GREEN+' ; '+c.RED + 'overwrite ' + c.BLUE + '.' + c.GREEN + '.' + c.RED + '.')
						  rmtree(home + "\\Desktop\\CGT-Files\\1\\")
						except:
						  sleep(1)
						  print(c.END + c.RED + 'error' + c.GREEN+' : ' + c.BLUE + 'code '+c.YELLOW+'7' + c.GREEN+' | '+c.BLUE+'please see '+c.RED+'CGT-Files/ErrorList.png'+c.BLUE+' .'+c.GREEN+'.'+c.RED+'.')
						  error(7)
						  return
					else:
						print(c.RED+'making'+c.BLUE+' directory '+c.YELLOW+'1'+c.RED+' .'+c.GREEN+'.'+c.BLUE+'.')
					system('mkdir '+home + "\\Desktop\\CGT-Files\\1\\")
					sleep(1)
					print(c.END+c.BLUE + 'conevert '+c.RED + basename(img_lz4_file) + c.BLUE + ' to ' +c.RED + basename(img_file) + c.BLUE + ' .' + c.GREEN + '.' + c.RED + '.')
					system(home+'\\.CGT\\programs\\lz4.exe -d ' + img_lz4_file)
					img_lz4_size = stat(img_unpack)
					if img_lz4_size.st_size != 0:
					  sleep(1)
					  print(c.BLUE+'move '+c.RED+basename(img_file)+c.BLUE+' to '+c.RED+'CGT-Files/1/')
					  move(img_unpack, home+"\\Desktop\\CGT-Files\\1\\")
					  readme_convert_lz4_to_img = '--- convert ' + \
						  basename(img_lz4_file)+' to ' + \
						  basename(img_file)+' by CGT ---'
					  readme_convert = open(home + '\\Desktop\\CGT-Files\\1\\CGT.txt', 'w')
					  readme_convert.write(readme_convert_lz4_to_img)
					  readme_convert.close()
					  sleep(1)
					  print(c.END+c.RED + basename(img_lz4_file) + c.BLUE + ' converted to ' + c.RED + basename(img_file) + c.GREEN + ' : ' + c.YELLOW + "CGT-Files/1/")
					  chdir(home)
					  startfile(realpath(home+'\\Desktop\\CGT-Files\\1\\'))
					  startfile(home+'\\Desktop\\CGT-Files\\1\\CGT.txt')
					elif img_lz4_size.st_size == 0:
					  sleep(1)
					  print(c.END + c.RED + 'error' + c.GREEN+' : ' + c.BLUE + 'code '+c.YELLOW+'4' + c.GREEN+' | '+c.BLUE+'please see '+c.RED+'CGT-Files/ErrorList.png'+c.BLUE+' .'+c.GREEN+'.'+c.RED+'.')
					  error(4)
					  sleep(1)
					  print(c.BLUE+'remove'+c.RED+' logs '+c.BLUE+'and'+c.RED+' break '+c.BLUE+'.'+c.GREEN+'.'+c.RED+'.')
					  chdir(home)
					  rmtree(home + "\\Desktop\\CGT-Files\\1\\")
					  remove(img_unpack)
				elif file_extension != '.lz4':
					print(c.END + c.RED + 'error' + c.GREEN+' : ' + c.BLUE + 'code '+c.YELLOW+'3' + c.GREEN+' | '+c.BLUE+'please see '+c.RED+'CGT-Files/ErrorList.png'+c.BLUE+' .'+c.GREEN+'.'+c.RED+'.')
					error(3)
			elif exists(img_lz4_file) == False:
				print(c.END + c.RED + 'error' + c.GREEN+' : ' + c.BLUE + 'code '+c.YELLOW+'1' + c.GREEN+' | '+c.BLUE+'please see '+c.RED+'CGT-Files/ErrorList.png'+c.BLUE+' .'+c.GREEN+'.'+c.RED+'.')
				error(1)
	if language == 'FA':
		print(c.END+c.GREEN+'drag'+c.RED+' & '+c.GREEN +'drop'+c.BLUE+' konid '+c.RED+'file az no\'e '+c.GREEN+'.img.lz4'+c.BLUE+' va '+c.RED+'klid enter' + c.BLUE+' ra '+c.RED+'befesharid' + c.BLUE+' .'+c.GREEN+'.'+c.RED+'.')
		img_lz4_file = xinput(c.MAGENTA+'> '+c.YELLOW)
		if ' ' in img_lz4_file:
			print(c.RED+'khata'+c.GREEN+' : ' + c.BLUE + 'code '+c.YELLOW+'2' + c.GREEN+' | '+c.BLUE+'lotfan bbinid '+c.RED+'CGT-Files/FA-ErrorList.png'+c.BLUE+' .'+c.GREEN+'.'+c.RED+'.')
			error(2)
		else:
			img_file = img_lz4_file.replace('.lz4', '')
			img_lz4_file = img_lz4_file.replace("\"", "")
			img_lz4_file = img_lz4_file.replace("\'", "")
			file_name, file_extension = splitext(img_lz4_file)
			img_unpack = img_lz4_file.replace('.lz4', '')
			if exists(img_lz4_file) == True:
				if file_extension == '.lz4':
					if isdir(home + "\\Desktop\\CGT-Files\\1\\"):
						try:
						  rmtree(home + "\\Desktop\\CGT-Files\\1\\")
						  sleep(1)
						  print(c.END+c.RED+'directory'+c.YELLOW+' 1 '+c.BLUE + 'already exists'+c.GREEN+' ; '+c.RED + 'overwrite ' + c.BLUE + '.' + c.GREEN + '.' + c.RED + '.')
						except:
						  sleep(1)
						  print(c.RED+'khata'+c.GREEN+' : ' + c.BLUE + 'code '+c.YELLOW+'7' + c.GREEN+' | '+c.BLUE+'lotfan bbinid '+c.RED+'CGT-Files/FA-ErrorList.png'+c.BLUE+' .'+c.GREEN+'.'+c.RED+'.')
						  error(7)
						  return
					else:
						print(c.RED+'sakht'+c.BLUE+' poshe '+c.YELLOW+'1'+c.RED+' .'+c.GREEN+'.'+c.BLUE+'.')
					system('mkdir '+home + "\\Desktop\\CGT-Files\\1\\")
					sleep(1)
					print(c.END+c.BLUE + 'tabdil '+c.RED + basename(img_lz4_file) + c.BLUE + ' beh ' +c.RED + basename(img_file) + c.BLUE + ' .' + c.GREEN + '.' + c.RED + '.')
					system(home+'\\.CGT\\programs\\lz4.exe -d ' + img_lz4_file)
					img_lz4_size = stat(img_unpack)
					if img_lz4_size.st_size != 0:
					  sleep(1)
					  print(c.BLUE+'enteghal '+c.RED+basename(img_file)+c.BLUE+' beh '+c.RED+'CGT-Files/1/')
					  move(img_unpack, home+"\\Desktop\\CGT-Files\\1\\")
					  readme_convert_lz4_to_img = '--- tabdil shod ' + \
						  basename(img_lz4_file)+' beh ' + \
						  basename(img_file)+' tavasote CGT ---'
					  readme_convert = open(home + '\\Desktop\\CGT-Files\\1\\CGT.txt', 'w')
					  readme_convert.write(readme_convert_lz4_to_img)
					  readme_convert.close()
					  sleep(1)
					  print(c.END+c.RED + basename(img_lz4_file) + c.BLUE + ' tabdil shod beh ' + c.RED + basename(img_file) + c.GREEN + ' : ' + c.YELLOW + "CGT-Files/1/")
					  chdir(home)
					  startfile(realpath(home+'\\Desktop\\CGT-Files\\1\\'))
					  startfile(home+'\\Desktop\\CGT-Files\\1\\CGT.txt')
					if img_lz4_size.st_size == 0:
					  sleep(1)
					  print(c.RED+'khata'+c.GREEN+' : ' + c.BLUE + 'code '+c.YELLOW+'4' + c.GREEN+' | '+c.BLUE+'lotfan bbinid '+c.RED+'CGT-Files/FA-ErrorList.png'+c.BLUE+' .'+c.GREEN+'.'+c.RED+'.')
					  error(4)
					  sleep(1)
					  print(c.BLUE+'hazf'+c.RED+' log ha '+c.BLUE+'va'+c.RED+' khoroj '+c.BLUE+'.'+c.GREEN+'.'+c.RED+'.')
					  chdir(home)
					  rmtree(home + "\\Desktop\\CGT-Files\\1\\")
					  remove(img_unpack)
				elif file_extension != '.lz4':
					print(c.RED+'khata'+c.GREEN+' : ' + c.BLUE + 'code '+c.YELLOW+'3' + c.GREEN+' | '+c.BLUE+'lotfan bbinid '+c.RED+'CGT-Files/FA-ErrorList.png'+c.BLUE+' .'+c.GREEN+'.'+c.RED+'.')
					error(3)
			elif exists(img_lz4_file) == False:
				print(c.RED+'khata'+c.GREEN+' : ' + c.BLUE + 'code '+c.YELLOW+'1' + c.GREEN+' | '+c.BLUE+'lotfan bbinid '+c.RED+'CGT-Files/FA-ErrorList.png'+c.BLUE+' .'+c.GREEN+'.'+c.RED+'.')
				error(1)
def if_1():
	if os_type().upper() == 'WINDOWS':
		windows()
	elif os_type().upper() == 'LINUX':
		linux()
	else:
		pass