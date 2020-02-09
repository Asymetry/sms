#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os

os.system("apt-get install figlet")
os.system("apt-get install searchsploit")
os.system("clear")
os.system("figlet Asymetry")
os.system

print("""

##################################                                 
         * ASYMETRY *

1-) Port tarama
2-) Exploit arama 
3-) MAC Adresi değiştirme 
4-) MAC geri getirme

###################################

""")

islemno = raw_input("\033[91mAracınızın numarasını girin ==> ");



if(islemno == "1"):
	os.system("clear");
        os.system("figlet Asymetry");
	hedefip = raw_input("\033[96mHedef İP Girin ==> ");
        os.system("nmap -sS -sV -O " + hedefip);

elif(islemno == "2"):
	os.system("clear");
        os.system("figlet Asymetry");
	kelime = raw_input("\033[96mKelimenizi girin ==> ");
	os.system("searchsploit " + kelime);

elif(islemno == "3"):
	os.system("clear");
        os.system("figlet Asymetry");
	os.system("ifconfig eth0 down");
	os.system("macchanger -r eth0");
	os.system("ifconfig eth0 up");
	print("\033[96mYeni MAC Adresi random belirlendi.");


elif(islemno == "4"):
	os.system("ifconfig eth0 down");
	os.system("macchanger -p eth0");
	os.system("ifconfig eth0 up");
	print("\033[96mMAC adresiniz orjinaline döndürüldü.");  

istek = raw_input("Aracımız yeniden başlatılsınmı.( e ): ");

if(istek == "e"):
	os.system("python Asymetry.py")

else:
	os.system("python Asymetry.py");

