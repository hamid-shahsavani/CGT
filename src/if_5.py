# Copyright SYS113 2019. gpl v3.0 license , see readme file.

try:
	from os import startfile	
except:
	pass
from os.path import isdir , isfile , realpath
from random import randint
from os import mkdir , system
from time import sleep
from pathlib import Path
from error import error
from shutil import rmtree
from platform import system as os_type
from platform import release as os_release

def xinput(s, *args, **kwargs):
    print(s, end='')
    return input('')

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
	  MAGENTA = ''
	  YELLOW = ''
	  CYAN = ''
	  BLUE = ''
	  DARKCYAN = ''
	  GREEN = ''
	  RED = ''
	  GRAY = ''
	  BOLD = ''
	  WHITE = ''
	  END = ''
else:
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

def windows():
	def checksum(string):
		digits = list(map(int, string))
		odd_sum = sum(digits[-1::-2])
		even_sum = sum([sum(divmod(2 * d, 10)) for d in digits[-2::-2]])
		return (odd_sum + even_sum) % 10

	def generate(string):
		cksum = checksum(string + '0')
		return (10 - cksum) % 10

	def append_luhn(string):
		return string + str(generate(string))

	def generate_imei(subject_imei):
		imei_digits = []
		for i in range(0, 14):
			try:
				digit = subject_imei[i]
			except IndexError:
				digit = randint(0, 9)
			imei_digits.append(str(digit))
		return append_luhn("".join(imei_digits))
	if language == 'FA':
		def generate_list(Imei):
			for x in range(1,int(quantity)+1):
				_generate = open(home + '\\Desktop\\CGT-Files\\5\\IMEI.txt', 'a')
				if len(str(x)) == 1:
					_generate.write('| '+str(x)+'   |        '+generate_imei(Imei)+'         |'+'\n')
				if len(str(x)) == 2:
					_generate.write('| '+str(x)+'  |        '+generate_imei(Imei)+'         |'+'\n')
				if len(str(x)) == 3:
					_generate.write('| '+str(x)+' |        '+generate_imei(Imei)+'         |'+'\n')
				if len(str(x)) == 4:
					_generate.write('| '+str(x)+'|        '+generate_imei(Imei)+'         |'+'\n')
				if len(str(x)) == 5:
					_generate.write('|'+str(x)+'|        '+generate_imei(Imei)+'         |'+'\n')
				_generate.close()

		nums = xinput(c.END+c.BLUE+'addad '+c.RED+'pishfarz'+c.BLUE+' baray '+c.RED+'mahdode '+c.GREEN+'imei'+c.RED+' : '+c.YELLOW)
		if len(nums) > 15:
			print(c.RED+'khata'+c.GREEN+' : ' + c.BLUE + 'code '+c.YELLOW+'30' + c.GREEN+' | '+c.BLUE+'lotfan bbinid '+c.RED+'CGT-Files/FA-ErrorList.png'+c.BLUE+' .'+c.GREEN+'.'+c.RED+'.')
			error(30)
			return
		if not nums.isnumeric():
			print(c.RED+'khata'+c.GREEN+' : ' + c.BLUE + 'code '+c.YELLOW+'31' + c.GREEN+' | '+c.BLUE+'lotfan bbinid '+c.RED+'CGT-Files/FA-ErrorList.png'+c.BLUE+' .'+c.GREEN+'.'+c.RED+'.')
			error(31)
			return

		quantity = xinput(c.END+c.BLUE+'che '+c.RED+'tedad'+c.GREEN+' imei'+c.RED+' : '+c.YELLOW)
		if len(quantity) > 5:
			print(c.RED+'khata'+c.GREEN+' : ' + c.BLUE + 'code '+c.YELLOW+'29' + c.GREEN+' | '+c.BLUE+'lotfan bbinid '+c.RED+'CGT-Files/FA-ErrorList.png'+c.BLUE+' .'+c.GREEN+'.'+c.RED+'.')
			error(29)
			return
		if not quantity.isnumeric():
			print(c.RED+'khata'+c.GREEN+' : ' + c.BLUE + 'code '+c.YELLOW+'31' + c.GREEN+' | '+c.BLUE+'lotfan bbinid '+c.RED+'CGT-Files/FA-ErrorList.png'+c.BLUE+' .'+c.GREEN+'.'+c.RED+'.')
			error(31)
			return

		if isdir(home + '\\Desktop\\CGT-Files\\5\\'):
			try:
				sleep(1)
				print(c.END+c.RED+'poshe'+c.YELLOW+' 5 '+c.BLUE + 'vojod darad'+c.GREEN+' ; '+c.RED + 'hazf '+c.GREEN+'&'+c.RED+' sakht dobare ' + c.BLUE + '.' + c.GREEN + '.' + c.RED + '.')
				rmtree(home + "\\Desktop\\CGT-Files\\5\\")
			except:
				sleep(1)
				print(c.RED+'khata'+c.GREEN+' : ' + c.BLUE + 'code '+c.YELLOW+'23' + c.GREEN+' | '+c.BLUE+'lotfan bbinid '+c.RED+'CGT-Files/FA-ErrorList.png'+c.BLUE+' .'+c.GREEN+'.'+c.RED+'.')
				error(23)
				return
		else:
			print(c.RED+'sakht'+c.BLUE+' poshe '+c.YELLOW+'5'+c.RED+' .'+c.GREEN+'.'+c.BLUE+'.')
		system('mkdir '+home + '\\Desktop\\CGT-Files\\5\\')
		sleep(1)
		print(c.BLUE+'sakhte'+c.GREEN+' imei '+c.BLUE+'.'+c.GREEN+'.'+c.RED+'.')
		_generate = open(home + '\\Desktop\\CGT-Files\\5\\IMEI.txt', 'w')
		_generate = open(home + '\\Desktop\\CGT-Files\\5\\IMEI.txt', 'a')
		_generate.write('.______________________________________.\n' +'| imei ha tolid shodehand tavasote CGT |'+'\n.______________________________________.\n')																		 
		_generate.close()
		generate_list(nums)
		_generate = open(home + '\\Desktop\\CGT-Files\\5\\IMEI.txt', 'a')
		_generate.write('.______________________________________.\n' +'| imei ha tolid shodehand tavasote CGT |'+'\n.______________________________________.\n')	
		_generate.close()
		sleep(1)
		print(c.BLUE+'sakhte shod'+c.GREEN+' imei '+c.BLUE+'dar' +c.GREEN+' : '+c.YELLOW+'CGT-Files/5/'+c.RED+'IMEI.txt')
		startfile(home+'\\Desktop\\CGT-Files\\5\\IMEI.TXT')
	elif language == 'EN':
		def generate_list(Imei):
			for x in range(1,int(quantity)+1):
				_generate = open(home + '\\Desktop\\CGT-Files\\5\\IMEI.txt', 'a')
				if len(str(x)) == 1:
					_generate.write('| '+str(x)+'   |  '+generate_imei(Imei)+'  |'+'\n')
				if len(str(x)) == 2:
					_generate.write('| '+str(x)+'  |  '+generate_imei(Imei)+'  |'+'\n')
				if len(str(x)) == 3:
					_generate.write('| '+str(x)+' |  '+generate_imei(Imei)+'  |'+'\n')
				if len(str(x)) == 4:
					_generate.write('| '+str(x)+'|  '+generate_imei(Imei)+'  |'+'\n')
				if len(str(x)) == 5:
					_generate.write('|'+str(x)+'|  '+generate_imei(Imei)+'  |'+'\n')
				_generate.close()
	        
		nums = xinput(c.END+c.BLUE+'default '+c.RED+'numbers'+c.BLUE+' for '+c.GREEN+'imei '+c.BLUE+'range'+c.RED+' : '+c.YELLOW)

		if len(nums) > 15:
			print(c.END + c.RED + 'error' + c.GREEN+' : ' + c.BLUE + 'code ' +c.YELLOW+'30' + c.GREEN+' | '+c.BLUE+'please see '+c.RED+'CGT-Files/EN-ErrorList.png'+c.BLUE+' .'+c.GREEN+'.'+c.RED+'.')
			error(30)
			return

		if not nums.isnumeric():
			print(c.END + c.RED + 'error' + c.GREEN+' : ' + c.BLUE + 'code ' +c.YELLOW+'31' + c.GREEN+' | '+c.BLUE+'please see '+c.RED+'CGT-Files/EN-ErrorList.png'+c.BLUE+' .'+c.GREEN+'.'+c.RED+'.')
			error(31)
			return

		quantity = xinput(c.END+c.BLUE+'how many'+c.GREEN+' imei '+c.RED+': '+c.YELLOW)
		if len(quantity) > 5:
			print(c.END + c.RED + 'error' + c.GREEN+' : ' + c.BLUE + 'code ' +c.YELLOW+'29' + c.GREEN+' | '+c.BLUE+'please see '+c.RED+'CGT-Files/EN-ErrorList.png'+c.BLUE+' .'+c.GREEN+'.'+c.RED+'.')
			error(29)
			return

		if not quantity.isnumeric():
			print(c.END + c.RED + 'error' + c.GREEN+' : ' + c.BLUE + 'code ' +c.YELLOW+'31' + c.GREEN+' | '+c.BLUE+'please see '+c.RED+'CGT-Files/EN-ErrorList.png'+c.BLUE+' .'+c.GREEN+'.'+c.RED+'.')
			error(31)
			return

		if isdir(home + '\\Desktop\\CGT-Files\\5\\'):
			try:
				sleep(1)
				print(c.END+c.RED+'directory'+c.YELLOW+' 5 '+c.BLUE + 'already exists'+c.GREEN+' ; ' +c.RED + 'overwrite ' + c.BLUE + '.' + c.GREEN + '.' + c.RED + '.')
				rmtree(home + "\\Desktop\\CGT-Files\\5\\")
			except:
				sleep(1)
				print(c.END + c.RED + 'error' + c.GREEN+' : ' + c.BLUE + 'code ' +c.YELLOW+'23' + c.GREEN+' | '+c.BLUE+'please see '+c.RED+'CGT-Files/EN-ErrorList.png'+c.BLUE+' .'+c.GREEN+'.'+c.RED+'.')
				error(23)
				return
		else:
			print(c.RED+'making'+c.BLUE+' directory '+c.YELLOW+'5'+c.RED+' .'+c.GREEN+'.'+c.BLUE+'.')
		system('mkdir '+home + '\\Desktop\\CGT-Files\\5\\')
		sleep(1)
		print(c.BLUE+'generate'+c.RED+' imei '+c.BLUE+'.'+c.GREEN+'.'+c.RED+'.')
		_generate = open(home + '\\Desktop\\CGT-Files\\5\\IMEI.txt', 'w')
		_generate = open(home + '\\Desktop\\CGT-Files\\5\\IMEI.txt', 'a')
		_generate.write('._________________________.\n' +'| imei\'s generated by CGT |'+'\n._________________________.\n') 														 
		_generate.close()
		generate_list(nums)
		_generate = open(home + '\\Desktop\\CGT-Files\\5\\IMEI.txt', 'a')
		_generate.write('._________________________.\n' +'| imei\'s generated by CGT |'+'\n._________________________.\n') 	
		_generate.close()
		sleep(1)
		print(c.BLUE+'generated'+c.RED+' imei '+c.BLUE+'in' +c.GREEN+' : '+c.YELLOW+'CGT-Files/5/'+c.RED+'IMEI.txt')
		startfile(home+'\\Desktop\\CGT-Files\\5\\IMEI.TXT')

def if_5():
	if os_type().upper() == 'WINDOWS':
		windows()
	elif os_type().upper() == 'LINUX':
		linux()
	else:
		pass
