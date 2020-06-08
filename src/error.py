# Copyright SYS113 2019. gpl v3.0 license , see readme file.

from tkinter import Tk , Label
from pathlib import Path
from PIL.ImageTk import PhotoImage
from PIL import Image
from platform import system as os_type
from os.path import isfile
from pathlib import Path
from time import sleep
from threading import Timer

home = str(Path.home())

if os_type().upper() == 'WINDOWS':
	if isfile(home+'\\.CGT\\files\\LANGUAGE'):
		language = open(home + '\\.CGT\\files\\LANGUAGE', 'r').read()
elif os_type().upper() == 'LINUX':
	if isfile(home+'/.CGT/files/LANGUAGE'):
		language = open(home + '/.CGT/files/LANGUAGE', 'r').read()
else:
	pass

root = None

def error(code):
	global root
	if root is not None:
		try:
			root.destroy()
		except:
			pass
	root = Tk()
	root.resizable(False, False)
	root.title("cgt error , code : "+str(code))
	if language == 'EN':
		if os_type().upper() == 'WINDOWS':
			root.iconbitmap(home +"\\.CGT\\files\\CGT.ico")
			im = Image.open(home +'\\.CGT\\errors\\EN\\'+str(code)+'.png')
		elif os_type().upper() == 'LINUX':
			im = Image.open(home +'/.CGT/errors/EN/'+str(code)+'.png')
		else:
			return
		photo = PhotoImage(im)
		label = Label(root, image=photo)
		label.image = photo
		label.pack()
		root.update()     
	if language == 'FA':
		if os_type().upper() == 'WINDOWS':
			root.iconbitmap(home +"\\.CGT\\files\\CGT.ico")
			im = Image.open(home +'\\.CGT\\errors\\FA\\'+str(code)+'.png')
		elif os_type().upper() == 'LINUX':
			im = Image.open(home +'/.CGT/errors/FA/'+str(code)+'.png')  
		else:
			return         
		photo = PhotoImage(im)
		label = Label(root, image=photo)
		label.image = photo
		label.pack()
		root.update()