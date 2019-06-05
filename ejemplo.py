#! usr/env/bin python3

from os import *
from sys import *
import fnmatch

a = getcwd()
b = listdir()
nombre = []
for file in listdir('.'):
	if fnmatch.fnmatch(file,'DNA*'):
		nombre.append(file) 


print(nombre)
