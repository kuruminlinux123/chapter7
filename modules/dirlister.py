# coding: utf-8

import os
import math

def run(**args):
	#print("[*] In dirlister module.")
	files = os.listdir(".")
	files.append(math.pow(2,2))
	return str(files)