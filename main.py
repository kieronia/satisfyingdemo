import os
from random import *
import time
size = int(15)

while True:

	cmd = (f'mode {size},{size}')
	os.system(cmd)
	#time.sleep(0.01)
	size = size + 1
	os.system("color 9f")

	if size > 100:
		for kieronia in range(0,85):
			size = size - 1
			os.system("color bf")
			cmd = (f'mode {size},{size}')
			os.system(cmd)
			#time.sleep(0.01)
