#!/usr/bin/python
#-*- coding: utf-8 -*-
import requests
import re
import sys
from bs4 import BeautifulSoup
from time import sleep
import os

def exitproc():
	print "Usage)"
	print "     python ManpageHunter.py [Str1] [Str2] [...]"
	print "Example)"
	print "     python ManpageHunter.py '*function' 'tk.h' "
	sys.exit()

if __name__=='__main__':

	if len(sys.argv) < 2:
		exitproc()

	rootpage = 'https://linux.die.net/man/3/'
	
	f = open('pagelist')	
	while True:
		line = f.readline()
		if not line: break
		
		command = 'wget --output-file=log --output-document=z '+ line 
		os.system(command)
		sleep(1)
	
		f2 = open('z')
		contents = f2.read()

		hit = 'no'
		for i in range(1, len(sys.argv)):
			if sys.argv[i] in contents:
				hit = 'yes'
				break
		
		if hit == 'yes':
			print '[O] ' + line
		else:
			print '[X] ' + line

		f2.close()
	
	f.close()
