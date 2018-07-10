# batchInstall 
# -*- coding:utf-8 -*-
import os
libs = {"numpy","matplotilib","pillow","sklearn","requests",\
		"jieba","beautifulsoup4","wheel","networkx","sympy",\
		"pyinstaller","django","flask","weroot","pyqt5","pandas",\
		"pyopeng1","pypdf2","docopt","pygame"}
try :
	for lib in libs:
		os.system("pip install "+lib)
		print("successful")
except:
	print("failed somehow")