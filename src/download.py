# Copyright SYS113 2019. gpl v3.0 license , see readme file.

from line import line
from clear import clear
from pathlib import Path
from getpass import getuser
from tzlocal import get_localzone
from requests import get , ConnectionError
from os.path import isfile , isdir , basename
from os import system , remove , rename , execv , getcwd
from platform import system as os_type
from zipfile import ZipFile
from shutil import  rmtree , move
from time import sleep , strftime
from urllib.request import urlretrieve , urlopen
from tqdm import tqdm
from error import error
from sys import executable , exit , argv
from re import sub

def xinput(s, *args, **kwargs):
    print(s, end='')
    return input('')

home = (str(Path.home()))

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
	CGT_VERSION = '0.1.0'
	if not isfile(home + '\\.CGT\\files\\VERSION'):
		if _language == 'TEHRAN':
			while True:
				print(line())
				CGT_new = xinput(c.END+c.BLUE + 'nasb shavad '+c.RED+'CGT '+c.GREEN+CGT_VERSION+c.RED+' ? ' + c.RED +c.YELLOW+'[ '+c.RED+'Y'+c.YELLOW+' ]' + c.RED + ' : ' + c.CYAN)
				username = c.BLUE+getuser()
				if (CGT_new == 'y') or (CGT_new == 'Y'):
					if ' ' in username:
						sleep(1)
						print(c.END+c.RED+'khata'+c.GREEN+' : '+c.BLUE+'be '+c.RED+'dalil'+c.BLUE+' vojod character '+c.GREEN+'\"'+c.RED+'fasele'+c.GREEN+'\"'+c.BLUE+' dar '+c.RED+'name karbari'+c.GREEN+' > '+c.YELLOW+'\"'+str(username).replace(' ',c.RED+'_'+c.BLUE)+c.YELLOW+'\"'+c.GREEN+' , '+c.BLUE+'nasb'+c.RED+' momken '+c.BLUE+'nist '+c.RED+'.'+c.GREEN+'.'+c.BLUE+'.')
						sleep(10)
						exit()
					try:
						def download_link():
						    download = get('https://raw.githubusercontent.com/sys113/CGT-dependencies/master/DOWNLOAD').text
						    for download_link in  download.splitlines():
						        if 'windows-'+CGT_VERSION in download_link:
						            return download_link
						download_link = download_link()
						download_file_name = basename(download_link)
						check_size = urlopen(download_link)
						size_download_link = c.RED+str(round((check_size.length / 1024) / 1024,2))+'mb'
						print(c.BLUE+'download'+c.GREEN+' : '+c.RED+download_file_name+c.GREEN+' , '+c.BLUE+'andaze'+c.GREEN+' : '+c.RED+size_download_link+c.BLUE+' .'+c.GREEN+'.'+c.RED+'.'+c.YELLOW)
						sleep(1)
						try:
							if not isdir(home+"\\.CGT-Download\\"):
								system('mkdir '+home+'\\.CGT-Download\\')
							class TqdmUpTo(tqdm):
								def update_to(self, b=1, bsize=1, tsize=None):
									if tsize is not None:
										self.total = tsize
										self.update(b * bsize - self.n)
							with TqdmUpTo(unit='B', unit_scale=True, miniters=1,
								desc=''.split('/')[-1]) as t:          
									urlretrieve(download_link, filename=home + "\\.CGT-Download\\"+download_file_name, 
									reporthook=t.update_to, data=None)
						except:
							print(c.END+c.RED+'khata'+c.GREEN+' : '+c.RED+'bad'+c.BLUE+' hast'+c.GREEN+' , '+c.BLUE+'sorate '+c.RED+'internet '+c.BLUE+'.'+c.GREEN+'.'+c.RED+'.')
							rmtree(home+'\\.CGT-Download')
							sleep(1)
							print(c.BLUE+'shoro\'e'+c.RED+' dobare '+c.BLUE+'.'+c.GREEN+'.'+c.RED+'.'+c.END)
							sleep(5)
							execv(executable, ['python'] + argv)
						if isdir(home + '\\.CGT'):
							rmtree(home + '\\.CGT')
						system('mkdir '+home+'\\.CGT')
						system('attrib +h '+home+"\\.CGT")
						move(home + "\\.CGT-Download\\"+download_file_name, home + "\\.CGT\\"+download_file_name)
						rmtree(home + '\\.CGT-Download')
						with ZipFile(home + "\\.CGT\\"+download_file_name, 'r') as zip_ref:
							zip_ref.extractall(home+'\\.CGT\\')
						remove(home + "\\.CGT\\"+download_file_name)
						version = open(home + '\\.CGT\\files\\VERSION', 'w')
						version.write(CGT_VERSION)
						version.close()
						make_Lang = open(home + '\\.CGT\\files\\LANGUAGE', 'w')
						make_Lang.write('FA')
						make_Lang.close()
						if isdir(home + '\\Desktop\\CGT-Files'):
							if(isdir(home+'\\Desktop\\CGT-Files\\1')) or (isdir(home+'\\Desktop\\CGT-Files\\2')) or (isdir(home+'\\Desktop\\CGT-Files\\3')) or (isdir(home+'\\Desktop\\CGT-Files\\4')) or (isdir(home+'\\Desktop\\CGT-Files\\5')):
								current_time = strftime("%Y-%m-%d-%H-%M-%S")
								try:
									if not isdir(home+'\\Desktop\\CGT-Backup\\'):
										print(c.BLUE+'sakhte poshe'+c.RED+' CGT-Backup '+c.BLUE+' .'+c.GREEN+'.'+c.RED+'.')
										system('mkdir '+ home+'\\Desktop\\CGT-Backup\\')
									move(home+'\\Desktop\\CGT-Files',home+'\\Desktop\\CGT-Backup\\'+current_time)
									sleep(1)
									print(c.RED+'name'+c.BLUE+' poshe '+c.RED+'CGT-Files'+c.BLUE+' taghir kard be '+c.RED+current_time+c.BLUE+' .'+c.GREEN+'.'+c.RED+'.')
									sleep(1)
									print(c.RED+'enteghal'+c.BLUE+' poshe '+c.RED+current_time+c.BLUE+' be '+c.RED+'CGT-Backup'+c.BLUE+' .'+c.GREEN+'.'+c.RED+'.')
								except:
										print(c.END+c.RED+'khata'+c.GREEN+' : '+c.BLUE+'dar hale hazer '+c.GREEN+','+c.RED+' faraayand '+c.BLUE+'digari'+c.RED+' bar roye'+c.BLUE+' poshe '+c.RED+'CGT-Files '+c.BLUE+'dar hale '+c.RED+'ejras '+c.BLUE+'.'+c.GREEN+'.'+c.RED+'.')
										rmtree(home+'\\.CGT\\')
										sleep(1)
										print(c.BLUE+'shoro\'e'+c.RED+' dobare '+c.BLUE+'.'+c.GREEN+'.'+c.RED+'.'+c.END)
										sleep(5)
										execv(executable, ['python'] + argv)
							else:
								print(c.RED+'hazf'+c.GREEN+' & '+c.RED+'sakht dobare'+c.BLUE+' poshe '+c.RED+'CGT-Files'+c.BLUE+' .'+c.GREEN+'.'+c.RED+'.')
								try:
									rmtree(home+'\\Desktop\\CGT-Files')
								except:
									sleep(1)
									print(c.END+c.RED+'khata'+c.GREEN+' : '+c.BLUE+'dar hale hazer '+c.GREEN+','+c.RED+' faraayand '+c.BLUE+'digari'+c.RED+' bar roye'+c.BLUE+' poshe '+c.RED+'CGT-Files '+c.BLUE+'dar hale '+c.RED+'ejras '+c.BLUE+'.'+c.GREEN+'.'+c.RED+'.')
									rmtree(home+'\\.CGT\\')
									sleep(1)
									print(c.BLUE+'shoro\'e'+c.RED+' dobare '+c.BLUE+'.'+c.GREEN+'.'+c.RED+'.'+c.END)
									sleep(5)
									execv(executable, ['python'] + argv)
						sleep(1)
						print(c.END+c.RED+'Download '+c.GREEN+','+c.BLUE+' be '+c.RED+'etmam '+c.BLUE+'resid'+c.RED+ ' .' + c.GREEN + '.' + c.BLUE + '.')
						sleep(1)
						print(c.BLUE+'shoro\'e'+c.RED+' dobare '+c.BLUE+'.'+c.GREEN+'.'+c.RED+'.'+c.END)
						sleep(5)
						execv(executable, ['python'] + argv)
					except ConnectionError:
						sleep(1)
						print(c.END+c.RED+'khata'+c.GREEN+' : '+c.RED+'motasel'+c.BLUE+' shavid be '+c.RED+'internet'+c.BLUE+' .'+c.GREEN+'.'+c.RED+'.')
						sleep(1)
						print(c.BLUE+'shoro\'e'+c.RED+' dobare '+c.BLUE+'.'+c.GREEN+'.'+c.RED+'.'+c.END)
						sleep(5)
						execv(executable, ['python'] + argv)
				else:
					sleep(1)
					print(c.END+c.RED+'khata'+c.GREEN+' : '+c.BLUE + 'faghat ' + c.RED + 'Y'+c.BLUE + ' .' + c.GREEN + '.' + c.RED + '.')
					sleep(1)
					print(c.BLUE+'shoro\'e'+c.RED+' dobare '+c.BLUE+'.'+c.GREEN+'.'+c.RED+'.'+c.END)
					sleep(5)
					execv(executable, ['python'] + argv)
		elif _language != 'TEHRAN':
			while True:
				print(line())
				CGT_new = xinput(c.END+c.BLUE + 'install '+c.RED+'CGT '+c.GREEN+CGT_VERSION+c.RED+' ? ' + c.RED +c.YELLOW+'[ '+c.RED+'Y'+c.YELLOW+' ]' + c.RED + ' : ' + c.CYAN)
				username = c.BLUE+getuser()
				if (CGT_new == 'y') or (CGT_new == 'Y'):
					if ' ' in username:
						sleep(1)
						# Error: Cannot install  Because of there is space character in username ..
						print(c.END+c.RED+'error'+c.GREEN+' : '+c.BLUE+'cant'+c.RED+' install '+c.BLUE+'because of there is'+c.RED+' space character '+c.BLUE+'in'+c.RED+' username'+c.GREEN+' > '+c.YELLOW+'\"'+str(username).replace(' ',c.RED+'_'+c.BLUE)+c.YELLOW+'\"'+c.RED+' .'+c.GREEN+'.'+c.BLUE+'.')
						sleep(10)
						exit()
					try:
						def download_link():
						    download = get('https://raw.githubusercontent.com/sys113/CGT-dependencies/master/DOWNLOAD').text
						    for download_link in  download.splitlines():
						        if 'windows-'+CGT_VERSION in download_link:
						            return download_link
						download_link = download_link()
						download_file_name = basename(download_link)
						check_size = urlopen(download_link)
						size_download_link = c.RED+str(round((check_size.length / 1024) / 1024,2))+'mb'
						print(c.BLUE+'download'+c.GREEN+' : '+c.RED+download_file_name+c.GREEN+' , '+c.BLUE+'size'+c.GREEN+' : '+c.RED+size_download_link+c.BLUE+' .'+c.GREEN+'.'+c.RED+'.'+c.YELLOW)
						sleep(1)
						try:
							if not isdir(home+"\\.CGT-Download\\"):
								system('mkdir '+home+'\\.CGT-Download\\')
							class TqdmUpTo(tqdm):
								def update_to(self, b=1, bsize=1, tsize=None):
									if tsize is not None:
										self.total = tsize
										self.update(b * bsize - self.n)
							with TqdmUpTo(unit='B', unit_scale=True, miniters=1,
								desc=''.split('/')[-1]) as t:          
									urlretrieve(download_link, filename=home + "\\.CGT-Download\\"+download_file_name, 
									reporthook=t.update_to, data=None)
						except:
							print(c.END+c.RED+'error'+c.GREEN+' : '+c.BLUE+'network'+c.RED+' speed '+c.BLUE+'is'+c.RED+' bad '+ c.BLUE+'.'+c.GREEN+'.'+c.RED+'.')
							rmtree(home+'\\.CGT-Download')
							sleep(1)
							print(c.BLUE+'restart '+c.RED+'.'+c.GREEN+'.'+c.BLUE+'.'+c.END)
							sleep(5)
							execv(executable, ['python'] + argv)
						if isdir(home + '\\.CGT'):
							rmtree(home + '\\.CGT')
						system('mkdir '+home+'\\.CGT')
						system('attrib +h '+home+"\\.CGT")
						move(home + "\\.CGT-Download\\"+download_file_name, home + "\\.CGT\\"+download_file_name)
						rmtree(home + '\\.CGT-Download')
						with ZipFile(home + "\\.CGT\\"+download_file_name, 'r') as zip_ref:
							zip_ref.extractall(home+'\\.CGT\\')
						remove(home + "\\.CGT\\"+download_file_name)
						version = open(home + '\\.CGT\\files\\VERSION', 'w')
						version.write(CGT_VERSION)
						version.close()
						make_Lang = open(home + '\\.CGT\\files\\LANGUAGE', 'w')
						make_Lang.write('EN')
						make_Lang.close()
						if isdir(home + '\\Desktop\\CGT-Files'):
							if(isdir(home+'\\Desktop\\CGT-Files\\1')) or (isdir(home+'\\Desktop\\CGT-Files\\2')) or (isdir(home+'\\Desktop\\CGT-Files\\3')) or (isdir(home+'\\Desktop\\CGT-Files\\4')) or (isdir(home+'\\Desktop\\CGT-Files\\5')):
								current_time = strftime("%Y-%m-%d-%H-%M-%S")
								try:
									if not isdir(home+'\\Desktop\\CGT-Backup\\'):
										print(c.BLUE+'creating'+c.RED+' CGT-Backup '+c.BLUE+'directory'+c.BLUE+' .'+c.GREEN+'.'+c.RED+'.')
										system('mkdir '+ home+'\\Desktop\\CGT-Backup\\')
									move(home+'\\Desktop\\CGT-Files',home+'\\Desktop\\CGT-Backup\\'+current_time)
									sleep(1)
									print(c.RED+'CGT-Files '+c.BLUE+'directory'+c.RED+' renamed '+c.BLUE+'to '+c.RED+current_time+c.BLUE+' .'+c.GREEN+'.'+c.RED+'.')
									sleep(1)
									print(c.RED+current_time+c.BLUE+' directory '+c.RED+'moved'+c.BLUE+' to '+c.RED+'CGT-Backup'+c.BLUE+' .'+c.GREEN+'.'+c.RED+'.')
								except:
										print(c.END+c.RED+'error'+c.GREEN+' : '+c.BLUE+'another'+c.RED+' process '+c.BLUE+'is currently'+c.RED+' running'+c.BLUE+' on '+c.RED+'CGT-Files '+c.BLUE+'directory '+c.RED+'.'+c.GREEN+'.'+c.BLUE+'.')
										rmtree(home+'\\.CGT\\')
										sleep(1)
										print(c.BLUE+'restart '+c.RED+'.'+c.GREEN+'.'+c.BLUE+'.'+c.END)
										sleep(5)
										execv(executable, ['python'] + argv)
							else:
								sleep(1)
								print(c.RED+'remove'+c.GREEN+' & '+c.RED+'create again'+c.GREEN+' CGT-Files '+c.BLUE+'directroy '+c.RED+'.'+c.GREEN+'.'+c.BLUE+'.')
								try:
									rmtree(home+'\\Desktop\\CGT-Files')
								except:
									sleep(1)
									print(c.END+c.RED+'error'+c.GREEN+' : '+c.BLUE+'another'+c.RED+' process '+c.BLUE+'is currently'+c.RED+' running'+c.BLUE+' on '+c.RED+'CGT-Files '+c.BLUE+'directory '+c.RED+'.'+c.GREEN+'.'+c.BLUE+'.')
									rmtree(home+'\\.CGT\\')
									sleep(1)
									print(c.BLUE+'restart '+c.RED+'.'+c.GREEN+'.'+c.BLUE+'.'+c.END)
									sleep(5)
									execv(executable, ['python'] + argv)
						sleep(1)
						print(c.END+c.BLUE+'Download '+c.RED+'Completed'+c.BLUE + ' .' + c.GREEN + '.' + c.RED + '.'+c.GREEN)
						sleep(1)
						print(c.BLUE+'restart '+c.RED+'.'+c.GREEN+'.'+c.BLUE+'.'+c.END)
						sleep(5)
						execv(executable, ['python'] + argv)
					except ConnectionError:
						sleep(1)
						print(c.END+c.RED+'error'+c.GREEN+' : '+c.BLUE+'please'+c.RED+' connect '+c.BLUE+'to'+c.RED+' network '+c.BLUE+'and'+c.RED+' try again '+ c.BLUE+'.'+c.GREEN+'.'+c.RED+'.')
						sleep(1)
						print(c.BLUE+'restart '+c.RED+'.'+c.GREEN+'.'+c.BLUE+'.'+c.END)
						sleep(5)
						execv(executable, ['python'] + argv)
				else:
					sleep(1)
					print(c.END+c.RED+'error'+c.GREEN+' : '+c.BLUE + 'only ' + c.RED + 'Y'+c.BLUE + ' .' + c.GREEN + '.' + c.RED + '.')
					sleep(1)
					print(c.BLUE+'restart '+c.RED+'.'+c.GREEN+'.'+c.BLUE+'.'+c.END)
					sleep(5)
					execv(executable, ['python'] + argv)
	elif isfile(home + '\\.CGT\\files\\VERSION'):
		if isfile(home+'\\.CGT\\files\\DIR'):
			if getcwd() != open(home+'\\.CGT\\files\\DIR','r').read():
				direc = open(home+'\\.CGT\\files\\DIR','w')
				direc.write(getcwd())
				direc.close()
		if not isfile(home+'\\.CGT\\files\\DIR'):
			direc = open(home+'\\.CGT\\files\\DIR','w')
			direc.write(getcwd())
			direc.close()
		if isfile(home+'\\.CGT\\files\\LANGUAGE'):
			language = open(home + '\\.CGT\\files\\LANGUAGE', 'r').read()
		if language == 'FA':
			if open(home + '\\.CGT\\files\\VERSION', 'r').read() != CGT_VERSION:
					while True:
						VerOld = open(home + '\\.CGT\\files\\VERSION', 'r').read()
						print(line())
						if open(home + '\\.CGT\\files\\VERSION', 'r').read() < CGT_VERSION:
							CGT_new = xinput(c.END+c.BLUE + 'afzayesh noskhe '+c.RED+'CGT'+c.BLUE+' az '+c.GREEN+open(home + '\\.CGT\\files\\VERSION', 'r').read()+c.BLUE+' be '+c.GREEN+CGT_VERSION+c.RED+' ? ' + c.RED +c.YELLOW+'[ '+c.RED+'Y'+c.YELLOW+' ]' + c.RED + ' : ' + c.CYAN)
						elif open(home + '\\.CGT\\files\\VERSION', 'r').read() > CGT_VERSION:
							CGT_new = xinput(c.END+c.BLUE + 'kahesh noskhe '+c.RED+'CGT'+c.BLUE+' az '+c.GREEN+open(home + '\\.CGT\\files\\VERSION', 'r').read()+c.BLUE+' be '+c.GREEN+CGT_VERSION+c.RED+' ? ' + c.RED +c.YELLOW+'[ '+c.RED+'Y'+c.YELLOW+' ]' + c.RED + ' : ' + c.CYAN)
						if (CGT_new == 'y') or (CGT_new == 'Y'):
							try:
								def download_link():
								    download = get('https://raw.githubusercontent.com/sys113/CGT-dependencies/master/DOWNLOAD').text
								    for download_link in  download.splitlines():
								        if 'windows-'+CGT_VERSION in download_link:
								            return download_link
								download_link = download_link()
								download_file_name = basename(download_link)
								check_size = urlopen(download_link)
								size_download_link = c.RED+str(round((check_size.length / 1024) / 1024,2))+'mb'
								print(c.BLUE+'download'+c.GREEN+' : '+c.RED+download_file_name+c.GREEN+' , '+c.BLUE+'andaze'+c.GREEN+' : '+c.RED+size_download_link+c.BLUE+' .'+c.GREEN+'.'+c.RED+'.'+c.YELLOW)
								sleep(1)
								try:
									if not isdir(home+"\\.CGT-Download"):
										system('mkdir '+home+'\\.CGT-Download')
									class TqdmUpTo(tqdm):
										def update_to(self, b=1, bsize=1, tsize=None):
											if tsize is not None:
												self.total = tsize
												self.update(b * bsize - self.n)
									with TqdmUpTo(unit='B', unit_scale=True, miniters=1,
										desc=''.split('/')[-1]) as t:          
										urlretrieve(download_link, filename=home + "\\.CGT-Download\\"+download_file_name, 
										reporthook=t.update_to, data=None)
								except:
									sleep(1)
									print(c.END + c.RED + 'khata' + c.GREEN+' : ' + c.BLUE + 'code '+c.YELLOW+'22' + c.GREEN+' | '+c.BLUE+'lotfan bbinid '+c.RED+'CGT-Files/FA-ErrorList.png'+c.BLUE+' .'+c.GREEN+'.'+c.RED+'.')
									error(22)
									rmtree(home+'\\.CGT-Download')
									sleep(1)
									print(c.BLUE+'shoro\'e'+c.RED+' dobare '+c.BLUE+'.'+c.GREEN+'.'+c.RED+'.'+c.END)
									sleep(5)
									execv(executable, ['python'] + argv)
								if isdir(home + '\\.CGT'):
									rmtree(home + '\\.CGT')
								system('mkdir '+home+'\\.CGT')
								system('attrib +h '+home+"\\.CGT")
								move(home + "\\.CGT-Download\\"+download_file_name, home + "\\.CGT\\"+download_file_name)
								rmtree(home + '\\.CGT-Download')
								with ZipFile(home + "\\.CGT\\"+download_file_name, 'r') as zip_ref:
									zip_ref.extractall(home+'\\.CGT')
								remove(home + "\\.CGT\\"+download_file_name)
								version = open(home + '\\.CGT\\files\\VERSION', 'w')
								version.write(CGT_VERSION)
								version.close()
								make_Lang = open(home + '\\.CGT\\files\\LANGUAGE', 'w')
								make_Lang.write('FA')
								make_Lang.close()
								if isdir(home + '\\Desktop\\CGT-Files'):
									if(isdir(home+'\\Desktop\\CGT-Files\\1')) or (isdir(home+'\\Desktop\\CGT-Files\\2')) or (isdir(home+'\\Desktop\\CGT-Files\\3')) or (isdir(home+'\\Desktop\\CGT-Files\\4')) or (isdir(home+'\\Desktop\\CGT-Files\\5')):
										current_time = strftime("%Y-%m-%d-%H-%M-%S")
										try:
											if not isdir(home+'\\Desktop\\CGT-Backup\\'):
												print(c.BLUE+'sakhte poshe'+c.RED+' CGT-Backup '+c.BLUE+'.'+c.GREEN+'.'+c.RED+'.')
												system('mkdir '+ home+'\\Desktop\\CGT-Backup\\')
											move(home+'\\Desktop\\CGT-Files',home+'\\Desktop\\CGT-Backup\\'+current_time)
											sleep(1)
											print(c.RED+'name'+c.BLUE+' poshe '+c.RED+'CGT-Files'+c.BLUE+' taghir kard be '+c.RED+current_time+c.BLUE+' .'+c.GREEN+'.'+c.RED+'.')
											sleep(1)
											print(c.RED+'enteghal'+c.BLUE+' poshe '+c.RED+current_time+c.BLUE+' be '+c.RED+'CGT-Backup'+c.BLUE+' .'+c.GREEN+'.'+c.RED+'.')
										except:
											print(c.END + c.RED + 'khata' + c.GREEN+' : ' + c.BLUE + 'code '+c.YELLOW+'24' + c.GREEN+' | '+c.BLUE+'lotfan bbinid '+c.RED+'CGT-Files/FA-ErrorList.png'+c.BLUE+' .'+c.GREEN+'.'+c.RED+'.')
											error(24)
											version = open(home + '\\.CGT\\files\\VERSION', 'w')
											version.write(VerOld)
											version.close()
											sleep(1)
											print(c.BLUE+'shoro\'e'+c.RED+' dobare '+c.BLUE+'.'+c.GREEN+'.'+c.RED+'.'+c.END)
											sleep(5)
											execv(executable, ['python'] + argv)
									else:
										sleep(1)
										print(c.RED+'hazf'+c.GREEN+' & '+c.RED+'sakht dobare'+c.BLUE+' poshe '+c.RED+'CGT-Files'+c.BLUE+' .'+c.GREEN+'.'+c.RED+'.')
										try:
											rmtree(home+'\\Desktop\\CGT-Files')
										except:
											sleep(1)
											print(c.END + c.RED + 'khata' + c.GREEN+' : ' + c.BLUE + 'code '+c.YELLOW+'24' + c.GREEN+' | '+c.BLUE+'lotfan bbinid '+c.RED+'CGT-Files/FA-ErrorList.png'+c.BLUE+' .'+c.GREEN+'.'+c.RED+'.')
											error(24)
											version = open(home + '\\.CGT\\files\\VERSION', 'w')
											version.write(VerOld)
											version.close()
											sleep(1)
											print(c.BLUE+'shoro\'e'+c.RED+' dobare '+c.BLUE+'.'+c.GREEN+'.'+c.RED+'.'+c.END)
											sleep(5)
											execv(executable, ['python'] + argv)
								sleep(1)
								print(c.END+c.RED+'Download '+c.GREEN+','+c.BLUE+' be '+c.RED+'etmam '+c.BLUE+'resid'+c.RED+ ' .' + c.GREEN + '.' + c.BLUE + '.')
								sleep(1)
								print(c.BLUE+'shoro\'e'+c.RED+' dobare '+c.BLUE+'.'+c.GREEN+'.'+c.RED+'.'+c.END)
								sleep(5)
								execv(executable, ['python'] + argv)
							except ConnectionError:
								sleep(1)
								print(c.END + c.RED + 'khata' + c.GREEN+' : ' + c.BLUE + 'code '+c.YELLOW+'20' + c.GREEN+' | '+c.BLUE+'lotfan bbinid '+c.RED+'CGT-Files/FA-ErrorList.png'+c.BLUE+' .'+c.GREEN+'.'+c.RED+'.')
								error(20)
								sleep(1)
								print(c.BLUE+'shoro\'e'+c.RED+' dobare '+c.BLUE+'.'+c.GREEN+'.'+c.RED+'.'+c.END)
								sleep(5)
								execv(executable, ['python'] + argv)
						else:
							sleep(1)
							print(c.END + c.RED + 'khata' + c.GREEN+' : ' + c.BLUE + 'code '+c.YELLOW+'21' + c.GREEN+' | '+c.BLUE+'lotfan bbinid '+c.RED+'CGT-Files/FA-ErrorList.png'+c.BLUE+' .'+c.GREEN+'.'+c.RED+'.')
							error(21)
							sleep(1)
							print(c.BLUE+'shoro\'e'+c.RED+' dobare '+c.BLUE+'.'+c.GREEN+'.'+c.RED+'.'+c.END)
							sleep(5)
							execv(executable, ['python'] + argv)
		elif language == 'EN':
			if open(home + '\\.CGT\\files\\VERSION', 'r').read() != CGT_VERSION:
					while True:
						VerOld = open(home + '\\.CGT\\files\\VERSION', 'r').read()
						print(line())
						if open(home + '\\.CGT\\files\\VERSION', 'r').read() < CGT_VERSION:
							CGT_new = xinput(c.END+c.BLUE + 'upgrade '+c.RED+'CGT '+c.GREEN+open(home + '\\.CGT\\files\\VERSION', 'r').read()+c.BLUE+' to '+c.GREEN+CGT_VERSION+c.RED+' ? ' + c.RED +c.YELLOW+'[ '+c.RED+'Y'+c.YELLOW+' ]' + c.RED + ' : ' + c.CYAN)
						elif open(home + '\\.CGT\\files\\VERSION', 'r').read() > CGT_VERSION:
							CGT_new = xinput(c.END+c.BLUE + 'downgrade '+c.RED+'CGT '+c.GREEN+open(home + '\\.CGT\\files\\VERSION', 'r').read()+c.BLUE+' to '+c.GREEN+CGT_VERSION+c.RED+' ? ' + c.RED +c.YELLOW+'[ '+c.RED+'Y'+c.YELLOW+' ]' + c.RED + ' : ' + c.CYAN)
						if (CGT_new == 'y') or (CGT_new == 'Y'):
							try:
								def download_link():
								    download = get('https://raw.githubusercontent.com/sys113/CGT-dependencies/master/DOWNLOAD').text
								    for download_link in  download.splitlines():
								        if 'windows-'+CGT_VERSION in download_link:
								            return download_link
								download_link = download_link()
								download_file_name = basename(download_link)
								check_size = urlopen(download_link)
								size_download_link = c.RED+str(round((check_size.length / 1024) / 1024,2))+'mb'
								print(c.BLUE+'download'+c.GREEN+' : '+c.RED+download_file_name+c.GREEN+' , '+c.BLUE+'size'+c.GREEN+' : '+c.RED+size_download_link+c.BLUE+' .'+c.GREEN+'.'+c.RED+'.'+c.YELLOW)
								sleep(1)
								try:
									if not isdir(home+"\\.CGT-Download"):
										system('mkdir '+home+'\\.CGT-Download')
									class TqdmUpTo(tqdm):
										def update_to(self, b=1, bsize=1, tsize=None):
											if tsize is not None:
												self.total = tsize
												self.update(b * bsize - self.n)
									with TqdmUpTo(unit='B', unit_scale=True, miniters=1,
										desc=''.split('/')[-1]) as t:          
										urlretrieve(download_link, filename=home + "\\.CGT-Download\\"+download_file_name, 
										reporthook=t.update_to, data=None)
								except:
									sleep(1)
									print(c.END + c.RED + 'error' + c.GREEN+' : ' + c.BLUE + 'code '+c.YELLOW+'22' + c.GREEN+' | '+c.BLUE+'please see '+c.RED+'CGT-Files/EN-ErrorList.png'+c.BLUE+' .'+c.GREEN+'.'+c.RED+'.')
									error(22)
									rmtree(home+'\\.CGT-Download')
									sleep(1)
									print(c.BLUE+'restart '+c.RED+'.'+c.GREEN+'.'+c.BLUE+'.'+c.END)
									sleep(5)
									execv(executable, ['python'] + argv)
								if isdir(home + '\\.CGT'):
									rmtree(home + '\\.CGT')
								system('mkdir '+home+'\\.CGT')
								system('attrib +h '+home+"\\.CGT")
								move(home + "\\.CGT-Download\\"+download_file_name, home + "\\.CGT\\"+download_file_name)
								rmtree(home + '\\.CGT-Download')
								with ZipFile(home + "\\.CGT\\"+download_file_name, 'r') as zip_ref:
									zip_ref.extractall(home+'\\.CGT')
								remove(home + "\\.CGT\\"+download_file_name)
								version = open(home + '\\.CGT\\files\\VERSION', 'w')
								version.write(CGT_VERSION)
								version.close()
								make_Lang = open(home + '\\.CGT\\files\\LANGUAGE', 'w')
								make_Lang.write('EN')
								make_Lang.close()
								if isdir(home + '\\Desktop\\CGT-Files'):
									if(isdir(home+'\\Desktop\\CGT-Files\\1')) or (isdir(home+'\\Desktop\\CGT-Files\\2')) or (isdir(home+'\\Desktop\\CGT-Files\\3')) or (isdir(home+'\\Desktop\\CGT-Files\\4')) or (isdir(home+'\\Desktop\\CGT-Files\\5')):
										current_time = strftime("%Y-%m-%d-%H-%M-%S")
										try:
											if not isdir(home+'\\Desktop\\CGT-Backup\\'):
												print(c.BLUE+'creating'+c.RED+' CGT-Backup '+c.BLUE+'directory'+c.BLUE+' .'+c.GREEN+'.'+c.RED+'.')
												system('mkdir '+ home+'\\Desktop\\CGT-Backup\\')
											move(home+'\\Desktop\\CGT-Files',home+'\\Desktop\\CGT-Backup\\'+current_time)
											sleep(1)
											print(c.RED+'CGT-Files '+c.BLUE+'directory'+c.RED+' renamed '+c.BLUE+'to'+c.RED+current_time+c.BLUE+' .'+c.GREEN+'.'+c.RED+'.')
											sleep(1)
											print(c.RED+current_time+c.BLUE+' directory '+c.RED+'moved'+c.BLUE+' to '+c.RED+'CGT-Backup'+c.BLUE+' .'+c.GREEN+'.'+c.RED+'.')
										except:
											print(c.END + c.RED + 'error' + c.GREEN+' : ' + c.BLUE + 'code '+c.YELLOW+'24' + c.GREEN+' | '+c.BLUE+'please see '+c.RED+'CGT-Files/EN-ErrorList.png'+c.BLUE+' .'+c.GREEN+'.'+c.RED+'.')
											error(24)
											version = open(home + '\\.CGT\\files\\VERSION', 'w')
											version.write(VerOld)
											version.close()
											sleep(1)
											print(c.BLUE+'restart '+c.RED+'.'+c.GREEN+'.'+c.BLUE+'.'+c.END)
											sleep(5)
											execv(executable, ['python'] + argv)
									else:
										sleep(1)
										print(c.RED+'remove'+c.GREEN+' & '+c.RED+'create again'+c.GREEN+' CGT-Files '+c.BLUE+'directroy '+c.RED+'.'+c.GREEN+'.'+c.BLUE+'.')
										try:
											rmtree(home+'\\Desktop\\CGT-Files')
										except:
											sleep(1)
											print(c.RED + 'error' + c.GREEN+' : ' + c.BLUE + 'code '+c.YELLOW+'24' + c.GREEN+' | '+c.BLUE+'please see '+c.RED+'CGT-Files/EN-ErrorList.png'+c.BLUE+' .'+c.GREEN+'.'+c.RED+'.')
											error(24)
											version = open(home + '\\.CGT\\files\\VERSION', 'w')
											version.write(VerOld)
											version.close()
											sleep(1)
											print(c.BLUE+'restart '+c.RED+'.'+c.GREEN+'.'+c.BLUE+'.'+c.END)
											sleep(5)
											execv(executable, ['python'] + argv)
								sleep(1)
								print(c.END+c.BLUE+'Download '+c.RED+'Completed'+c.BLUE + ' .' + c.GREEN + '.' + c.RED + '.'+c.GREEN)
								sleep(1)
								print(c.BLUE+'restart '+c.RED+'.'+c.GREEN+'.'+c.BLUE+'.'+c.END)
								sleep(5)
								execv(executable, ['python'] + argv)
							except ConnectionError:
								sleep(1)
								print(c.END + c.RED + 'error' + c.GREEN+' : ' + c.BLUE + 'code '+c.YELLOW+'20' + c.GREEN+' | '+ c.GREEN+' | '+c.BLUE+'please see '+c.RED+'CGT-Files/EN-ErrorList.png'+c.BLUE+' .'+c.GREEN+'.'+c.RED+'.')
								error(20)
								sleep(1)
								print(c.BLUE+'restart '+c.RED+'.'+c.GREEN+'.'+c.BLUE+'.'+c.END)
								sleep(5)
								execv(executable, ['python'] + argv)
						else:
							sleep(1)
							print(c.END + c.RED + 'error' + c.GREEN+' : ' + c.BLUE + 'code '+c.YELLOW+'21' + c.GREEN+' | '+c.BLUE+'please see '+c.RED+'CGT-Files/EN-ErrorList.png'+c.BLUE+' .'+c.GREEN+'.'+c.RED+'.')
							error(21)
							sleep(1)
							print(c.BLUE+'shoro\'e'+c.RED+' dobare '+c.BLUE+'.'+c.GREEN+'.'+c.RED+'.'+c.END)
							sleep(5)
							execv(executable, ['python'] + argv)

def download():
		if os_type().upper() == 'WINDOWS':
			windows()
		elif os_type().upper() == 'LINUX':
			linux()
		else:
			pass