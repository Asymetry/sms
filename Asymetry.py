#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os

os.system("clear")

print("""\033[96m
    \                              |              
   _ \    __| |   | __ `__ \   _ \ __|  __| |   | 
  ___ \ \__ \ |   | |   |   |  __/ |   |    |   | 
_/    _\____/\__, |_|  _|  _|\___|\__|_|   \__, | 
             ____/                         ____/  

##################################                                 

1-) Port tarama
2-) Exploit arama 
3-) MAC Adresi değiştirme 

###################################

""")

islemno = raw_input("\033[96mAracınızın numarasını girin ==> ")



if(islemno == "1"):
	
	hedefip = raw_input("\033[96mHedef İP Girin ==> ")
        os.system("nmap -sS -sV -O " + hedefip)


if(islemno == "2"):
	
	kelime = raw_input("\033[96mKelimenizi girin ==> ")
	os.system("searchsploit " + kelime)

if(islemno == "3"):
	
	print("""

  İnternete koblolu olarakmı yani eth0 olarakmı bağlanıyorsunuz yada
 kablosuz yani wlan0 olarakmı seçiniz. 

1-)eth0
2-)wlan0
3-)Mac adresini geri getirme
""")
	islem = raw_input("==> ")
if(islem == "1"):
	
	os.system("ifconfig eth0 down")
	os.system("macchanger -r eth0")
	os.system("ifconfig eth0 up")

if(islem == "2"):

	os.system("ifconfig wlan0 down")
	os.system("macchanger -r wlan0")
	os.system("ifconfig wlan0 up")

if(islem == "3"):

	print("""
1-)eth0
2-)wlan0
""")
	sec = raw_input("==> ")
if(sec == "1"):
	os.system("ifconfig eth0 down")
	os.system("macchanger -p eth0")
	os.system("ifconfig eth0 up")
elif(sec == "2"):
	os.system("ifconfig wlan0 down")
	os.system("macchanger -p wlan0")
	os.system("ifconfig wlan0 up")		












