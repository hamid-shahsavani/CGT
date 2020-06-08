# Copyright SYS113 2019. gpl v3.0 license , see readme file.

from random import choice

def line():
  text = "-"*102
  colors = ['\x1b[34m', '\x1b[36m', '\x1b[32m', '\x1b[90m',
  			 '\x1b[94m', '\x1b[96m', '\x1b[92m', '\x1b[95m',
  			  '\x1b[91m','\x1b[97m', '\x1b[93m', '\x1b[35m',
  			   '\x1b[31m', '\x1b[39m','\x1b[37m', '\x1b[33m']
  colored_chars = [choice(colors) + char for char in text]
  rand_line = ''.join(colored_chars)
  return rand_line

