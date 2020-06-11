# Copyright SYS113 2019. gpl v3.0 license , see readme file.

# import libs ...

from os import system
from platform import system as os_type
from platform import release as os_release
from cursor import hide , show
from sys import stdout
from subprocess import check_output
from threading import Thread
from time import sleep as zzz
from inspect import getframeinfo , stack
from random import choice
from queue import Queue
from contextlib import redirect_stdout

def loading(speed = None , sleep = None , function = None ,args = None , method = None):

	threads = []

	# find (filename or line) python file ...

	x = stack()[1]
	x = x[0]
	get_python_file_name_or_line = getframeinfo(x)

	# set valur for find line in python file ...

	line_python_file = str(get_python_file_name_or_line.lineno)

	# set value for find python file name ...

	python_file_name = str(get_python_file_name_or_line.filename)

	# set speed for animates function , default is 5 ...

	if speed == None:
		speed = 0.040
	elif type(speed) != int:
		print('tekrar module - error | python file : '+python_file_name+' | line : '+line_python_file+' | problem : speed argument must be number range of 1 to 10 ...')
		return
	elif speed == 1:
		speed = 0.020
	elif speed == 2:
		speed = 0.030
	elif speed == 3:
		speed = 0.040
	elif speed == 4:
		speed = 0.050
	elif speed == 5:
		speed = 0.060
	elif speed == 6:
		speed = 0.070
	elif speed == 7:
		speed = 0.080
	elif speed == 8:
		speed = 0.090
	elif speed == 9:
		speed = 0.200
	elif speed == 10:
		speed = 0.350
	else:
		print('tekrar module - error | python file : '+python_file_name+' | line : '+line_python_file+' | problem : speed argument must be number range of 1 to 10 ...')
		return

	# set method for animates function , default 1 ...

	if method == None:
		method = 1
	elif type(method) != int:
		print('tekrar module - error | python file : '+python_file_name+' | line : '+line_python_file+' | problem : method argument must be number range of 1 to 2 ...')
		return
	elif method == 1:
		method = 1
	elif method == 2:
		method = 2
	else:
		print('tekrar module - error | python file : '+python_file_name+' | line : '+line_python_file+' | problem : method argument must be number range of 1 to 2 ...')
		return

	# hide command line cursor ...

	hide()

	# fix show text color ...

	system('')

	# if finished == True break animate function ...

	finished = False

	# check command prompet columns size

	if os_type().upper() == 'WINDOWS':
		resize = str(check_output("mode con:", shell=True))
		resize = resize.split('\\r\\n    K', 1)[0]
		a = resize[-3]
		b = resize[-2]
		c = resize[-1]
		resize = a+b+c
		resize = resize.replace(' ','')
	elif os_type().upper() == 'LINUX':
		resize = str(check_output("resize", shell=True))
		resize = resize[10],resize[11],resize[12]
		resize = str(resize)
		resize = resize.replace(' ','')
		resize = resize.replace(',','')
		resize = resize.replace('\'','')
		resize = resize.replace(')','')
		resize = resize.replace('(','')
		resize = resize.replace(';','')
	
	#  command prompet size method 1 ...

	command_line_size_method_1 = int(resize)

	# command prompet half size method 2 ...

	half_command_line_size_method_1 = (command_line_size_method_1 - 3)//2

	# command prompet size method 2 ...

	command_line_size_method_2 = int(resize)-4

	# colored stars animate functions ...
	
	if os_release == '7':
		class star:
			blue = '*'
			green = '*'
			red = '*'
			yellow = '*'
	else:
		class star:
			blue = '\033[94m'+'*'
			green = '\033[92m'+'*'
			red = '\033[91m'+'*'
			yellow = '\033[33m'+'*'

	# b == blue , g == green , r == red , y == yellow in animate method 1 comment ...

	# --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

	# animate method 1 function ...

	def animate_method_1(speed):

		# infinite repetition until forced exit ...

		while True:

		# show loading ...

			for space in range(half_command_line_size_method_1):

				# end color ...
				
				stdout.write('\033[0m')

				# delete line ...

				stdout.flush() ; stdout.write('\033[D \033[D'*command_line_size_method_1) ; zzz(speed) ; stdout.write(' '*command_line_size_method_1+'\r')

				# show loading , |      bgy r     |

				stdout.write(' '*half_command_line_size_method_1+star.blue+star.green+star.yellow+' '*space+star.red)

				# exit from animate function , if runtime ended ...

				if (not thread.isAlive()) or (finished):
					
					# show command line cursor ...

					show()
					
					# delete line and close animate function ...

					stdout.write('\r\033[D \033[D'*command_line_size_method_1) ; stdout.write(' '*command_line_size_method_1+'\033[0m\r') ; return

			# show loading ...

			for space in range(half_command_line_size_method_1):

				# end color ...
				
				stdout.write('\033[0m')
				
				# add star to 3 stars from left varable

				reverse = (half_command_line_size_method_1-1)-space

				# delete line ...

				stdout.flush() ; stdout.write('\033[D \033[D'*command_line_size_method_1) ; zzz(speed) ; stdout.write(' '*command_line_size_method_1+'\r')

				# show loading , |     r bgy     |

				stdout.write(' '*space+star.red+' '*reverse+star.blue+star.green+star.yellow)

				# exit from animate function , if runtime ended ...

				if (not thread.isAlive()) or (finished):
					
					# show command line cursor ...

					show()
					
					# delete line and close animate function ...

					stdout.write('\r\033[D \033[D'*command_line_size_method_1) ; stdout.write(' '*command_line_size_method_1+'\033[0m\r') ; return

			# show loading ...

			for space in range(half_command_line_size_method_1):

				# end color ...
				
				stdout.write('\033[0m')
				
				# delete line ...

				stdout.flush() ; stdout.write('\033[D \033[D'*command_line_size_method_1) ; zzz(speed) ; stdout.write(' '*command_line_size_method_1+'\r')

				# show loading , |     rbg y     |

				stdout.write(' '*half_command_line_size_method_1+star.red+star.blue+star.green+' '*space+star.yellow)

				# exit from animate function , if runtime ended ...

				if (not thread.isAlive()) or (finished):
					
					# show command line cursor ...

					show()
					
					# delete line and close animate function ...

					stdout.write('\r\033[D \033[D'*command_line_size_method_1) ; stdout.write(' '*command_line_size_method_1+'\033[0m\r') ; return

			# show loading ...

			for space in range(half_command_line_size_method_1):

				# end color ...
				
				stdout.write('\033[0m')
				
				# add star to 3 stars from left varable

				reverse = (half_command_line_size_method_1-1)-space

				# delete line ...

				stdout.flush() ; stdout.write('\033[D \033[D'*command_line_size_method_1) ; zzz(speed) ; stdout.write(' '*command_line_size_method_1+'\r')

				# show loading , |     y rgbg     |

				stdout.write(' '*space+star.yellow+' '*reverse+star.red+star.blue+star.green)

				# exit from animate function , if runtime ended ...

				if (not thread.isAlive()) or (finished):
					
					# show command line cursor ...

					show()
					
					# delete line and close animate function ...

					stdout.write('\r\033[D \033[D'*command_line_size_method_1) ; stdout.write(' '*command_line_size_method_1+'\033[0m\r') ; return

			# show loading ...

			for space in range(half_command_line_size_method_1):

				# end color ...
				
				stdout.write('\033[0m')
				
				# delete line ...

				stdout.flush() ; stdout.write('\033[D \033[D'*command_line_size_method_1) ; zzz(speed) ; stdout.write(' '*command_line_size_method_1+'\r')

				# show loading , |     yrb g     |

				stdout.write(' '*half_command_line_size_method_1+star.yellow+star.red+star.blue+' '*space+star.green)

				# exit from animate function , if runtime ended ...

				if (not thread.isAlive()) or (finished):
					
					# show command line cursor ...

					show()
					
					# delete line and close animate function ...

					stdout.write('\r\033[D \033[D'*command_line_size_method_1) ; stdout.write(' '*command_line_size_method_1+'\033[0m\r') ; return

			# show loading ...

			for space in range(half_command_line_size_method_1):

				# end color ...
				
				stdout.write('\033[0m')
				
				# add star to 3 stars from left varable ...

				reverse = (half_command_line_size_method_1-1)-space

				# delete line ...

				stdout.flush() ; stdout.write('\033[D \033[D'*command_line_size_method_1) ; zzz(speed) ; stdout.write(' '*command_line_size_method_1+'\r')

				# show loading , |     g yrb     |

				stdout.write(' '*space+star.green+' '*reverse+star.yellow+star.red+star.blue)

				# exit from animate function , if runtime ended ...

				if (not thread.isAlive()) or (finished):
					
					# show command line cursor ...

					show()
					
					# delete line and close animate function ...

					stdout.write('\r\033[D \033[D'*command_line_size_method_1) ; stdout.write(' '*command_line_size_method_1+'\033[0m\r') ; return

			# show loading ...

			for space in range(half_command_line_size_method_1):

				# end color ...
				
				stdout.write('\033[0m')
				
				# delete line ...

				stdout.flush() ; stdout.write('\033[D \033[D'*command_line_size_method_1) ; zzz(speed) ; stdout.write(' '*command_line_size_method_1+'\r')

				# show loading , |     gyr b     |

				stdout.write(' '*half_command_line_size_method_1+star.green+star.yellow+star.red+' '*space+star.blue)

				# exit from animate function , if runtime ended ...

				if (not thread.isAlive()) or (finished):
					
					# show command line cursor ...

					show()
					
					# delete line and close animate function ...

					stdout.write('\r\033[D \033[D'*command_line_size_method_1) ; stdout.write(' '*command_line_size_method_1+'\033[0m\r') ; return

			# show loading ...

			for space in range(half_command_line_size_method_1):

				# end color ...
				
				stdout.write('\033[0m')

				# add star to 3 stars from left varable

				reverse = (half_command_line_size_method_1-1)-space

				# delete line ...

				stdout.flush() ; stdout.write('\033[D \033[D'*command_line_size_method_1) ; zzz(speed) ; stdout.write(' '*command_line_size_method_1+'\r')

				# show loading , |     b gyr     |

				stdout.write(' '*space+star.blue+' '*reverse+star.green+star.yellow+star.red)

				# exit from animate function , if runtime ended ...

				if (not thread.isAlive()) or (finished):
					
					# show command line cursor ...

					show()
					
					# delete line and close animate function ...

					stdout.write('\r\033[D \033[D'*command_line_size_method_1) ; stdout.write(' '*command_line_size_method_1+'\033[0m\r') ; return

	# --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

	# animate method 2 function ...

	def animate_method_2(speed):

		# infinite repetition until forced exit ...

		while True:

			# move stars from left to right

			for space in range(command_line_size_method_2):

				# end color ...

				stdout.write('\033[0m')

				# stars variable ...

				stars = ' '*space+"***"

				# set stars random color ...

				colors = ['\x1b[34m', '\x1b[36m', '\x1b[32m', '\x1b[90m',
							 '\x1b[94m', '\x1b[96m', '\x1b[92m', '\x1b[95m',
							  '\x1b[91m','\x1b[97m', '\x1b[93m', '\x1b[35m',
							   '\x1b[31m', '\x1b[39m','\x1b[37m', '\x1b[33m']

				# delete line ...

				stdout.flush() ; stdout.write('\033[D \033[D'*int(resize)) ; zzz(speed) ; stdout.write(' '*int(resize)+'\r')

				# show stars random color ...

				stdout.write(''.join([choice(colors) + char for char in stars]))

				# exit from animate function method 2 , if runtime ended ...

				if (not thread.isAlive()) or (finished):
					
					# show command line cursor ...

					show()
				
					# delete line and close animate method 2 function ...

					stdout.write('\r\033[D \033[D'*command_line_size_method_1) ; stdout.write(' '*command_line_size_method_1+'\033[0m\r') ; return
					
			# move stars from right to left

			for space in range(command_line_size_method_2):

				# end color ...
				
				stdout.write('\033[0m')

				# stars variable ...

				stars = ' '*(command_line_size_method_2-space)+"***"

				# set stars random color ...

				colors = ['\x1b[34m', '\x1b[36m', '\x1b[32m', '\x1b[90m',
							 '\x1b[94m', '\x1b[96m', '\x1b[92m', '\x1b[95m',
							  '\x1b[91m','\x1b[97m', '\x1b[93m', '\x1b[35m',
							   '\x1b[31m', '\x1b[39m','\x1b[37m', '\x1b[33m']

				# delete line ...

				stdout.flush() ; stdout.write('\033[D \033[D'*int(resize)) ; zzz(speed) ; stdout.write(' '*int(resize)+'\r')

				# show stars random color ...

				stdout.write(''.join([choice(colors) + char for char in stars]))

				# exit from animate function method 2 , if runtime ended ...

				if (not thread.isAlive()) or (finished):

					# show command line cursor ...

					show()
				
					# delete line and close animate function ...

					stdout.write('\r\033[D \033[D'*command_line_size_method_1) ; stdout.write(' '*command_line_size_method_1+'\033[0m\r') ; return

	# --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

	# create loading by sleep ...

	if sleep != None:

		# if type sleep is not int or float , break ...

		if (type(sleep) == int) or (type(sleep) == float):

			# if use 'sleep' argument , cannot use 'function' and 'args' arguments ...

			if (function != None) or (args != None):
				print('tekrar module - error | python file : '+python_file_name+' | line : '+line_python_file+' | problem : if use \'sleep\' argument , cannot use \'function\' and \'args\' arguments ...')
				return

			# animate method function selection ...

			if method == 1:

				# show animate function method 1 ...

				thread = Thread(target = animate_method_1 , args = [speed])
				thread.start()

				# if sleep time ended break animate function ...

				zzz(sleep)

				# delete line ...

				stdout.write('\033[D \033[D'*int(resize)) ; stdout.write(' '*int(resize)+'\033[0m\r')

				# if finished == True breaked animate method 1 function ...

				finished = True

			elif method == 2:

				# show animate function method 2 ...

				thread = Thread(target = animate_method_2 , args = [speed])

				# start thread ...
				
				thread.start()

				# if sleep time ended break animate function ...

				zzz(sleep)

				# delete line ...
				
				stdout.write('\033[D \033[D'*int(resize)) ; stdout.write(' '*int(resize)+'\033[0m\r')

				# if finished == True breaked animate method 2 function ...

				finished = True

		# if type sleep is not int or float show error ...

		else:
			print('tekrar module - error | python file : '+python_file_name+' | line : '+line_python_file+' | problem : sleep argument must be int type ...')
			return

	# --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

	# create loading by function ...

	elif function != None:

		# check function return value ...

		return_value = Queue()
		
		def storeInQueue(function):
			def returned(*args):
			
					return_value.put(function(*args))
			return returned
			

		# if is arguments ...

		if args != None:

			# if type args is not list show error ...

			if type(args) != list:
				print('tekrar module - error | python file : '+python_file_name+' | line : '+line_python_file+' | problem : argument \'args\' must be a list type ...')
				return

			# create thread ...

			thread = Thread(target = storeInQueue(function) , args = args)

		# if is not arguments ...

		if args == None:

			# create thread ...

			t = Thread(target = storeInQueue(function))
			threads.append(t)

		# redirect print ...

		with redirect_stdout(None):

			# start thread and show loading ...
			for thread in threads:
				thread.start()

		# if function is running ...

		while thread.isAlive():

			# selection method to show animate ...

			if method == 1:
				animate_method_1(speed)
			elif method == 2:
				animate_method_2(speed)

		for thread in threads:
			thread.join()
		
		# return function value ...

		return return_value.get()
		
