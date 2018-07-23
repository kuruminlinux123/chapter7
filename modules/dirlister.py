# coding: utf-8

import os
teste = 'teste'
def run(**args):
	#print("[*] In dirlister module.")
	files = os.listdir(".")
	return str(files)