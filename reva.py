import time
from numpy import number
import phonenumbers
from phonenumbers import timezone, geocoder, carrier
import colorama
from colorama import Fore, Back, Style
import sys
colorama.init()




banner = """


      ___           ___           ___           ___                                ___           ___           ___     
     /\  \         /\  \         /\__\         /\  \                   ___        /\__\         /\  \         /\  \    
    /::\  \       /::\  \       /:/  /        /::\  \                 /\  \      /::|  |       /::\  \       /::\  \   
   /:/\:\  \     /:/\:\  \     /:/  /        /:/\:\  \                \:\  \    /:|:|  |      /:/\:\  \     /:/\:\  \  
  /::\~\:\  \   /::\~\:\  \   /:/__/  ___   /::\~\:\  \               /::\__\  /:/|:|  |__   /::\~\:\  \   /:/  \:\  \ 
 /:/\:\ \:\__\ /:/\:\ \:\__\  |:|  | /\__\ /:/\:\ \:\__\           __/:/\/__/ /:/ |:| /\__\ /:/\:\ \:\__\ /:/__/ \:\__\
 \/_|::\/:/  / \:\~\:\ \/__/  |:|  |/:/  / \/__\:\/:/  /          /\/:/  /    \/__|:|/:/  / \/__\:\ \/__/ \:\  \ /:/  /
    |:|::/  /   \:\ \:\__\    |:|__/:/  /       \::/  /           \::/__/         |:/:/  /       \:\__\    \:\  /:/  / 
    |:|\/__/     \:\ \/__/     \::::/__/        /:/  /             \:\__\         |::/  /         \/__/     \:\/:/  /  
    |:|  |        \:\__\        ~~~~           /:/  /               \/__/         /:/  /                     \::/  /   
     \|__|         \/__/                       \/__/                              \/__/                       \/__/    
 
[+] Coded BY H04x For Reva 
"""
print(Fore.RED)
print(banner)

print(Fore.GREEN)
text = "Programımızı Tercih Ettiğiniz İçin Teşekkür Ederiz -H04x"

for t in text:
    print(t, end="", flush=True)
    time.sleep(0.03)

print(Fore.BLUE)
number = input("Numara Gir: \n > ")
phone = phonenumbers.parse(number)
zaman = timezone.time_zones_for_number(phone)
car = carrier.name_for_number(phone, "tr")
reg = geocoder.description_for_number(phone, "tr")



print("[i] Telefon Numarası Taranıyor..")
time.sleep(3)


print(Fore.CYAN)
print("[--RevaProjects Numara Info Sonuç Bulundu--]")
print(Fore.GREEN)
print("[+] Telefon Numarası: ", phone)
print("[+] Bölge/Şehir: ", zaman)
print("[+] Sağlayıcı: ", car)
print("[+] Ülke: ",reg)

time.sleep(10)