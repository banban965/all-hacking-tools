#import and from==================
import os
import time
import colorama 
from colorama import *
import datetime
import sys
import script1
import script2
import script3
import script4
import script5
import script6
import script7
import script8
import script9
import script10
import script11
import script12
import script13
import script14
import script15
import script16
import script17
import script18
import script19
import script20
#clear===========================
os.system('clear')
#slowed print def==================
def sp(text, delay=0.005):
    for char in str(text):
        print(char, end="", flush=True)
        time.sleep(delay)
    print()
#main menu======================
sp(Fore.BLUE + '♧===========================♤')
sp('♧============LTG============♤')
sp('♧===========================♤')
#selection number=================
sp(Fore.RED + '1.sms bomber')
sp('2.web cam hcaker')
sp('3.gmail bomber')
sp('4.file manger')
sp('5.about phone')
sp('6.wifi scanner')
sp('7.Bluetooth scanner')
sp('8.site info')
sp('9.test ping')
sp('10.nearby hack')
sp('11.gamil hacker')
sp('12.ÐÐơ§ hack')
sp('13.site attacker')
sp('14.game attacker')
sp('15.virus crafter')
sp('16.hacker tools 1')
sp('17.hacker tools 2')
sp('18.WI-FI J̣̌ammer')
sp('19.Bluetooth J̣̌ammer')
sp('20.Exiṭ')
sp(Fore.BLUE + '♧===========================♤')
User = input(Fore.GREEN + "ßelect Ɲumber? (1~20) : ")
os.system('clear')
os.system('clear')
os.system('clear')
#runninger========================
if User == "1":
    script1.run()

elif User == "2":
    script2.run()
    
elif User == "3":
    script3.run()
   
elif User == "4":
    script4.run()
    
elif User == "5":
    script5.run()
   
elif User == "6":
    script6.run()
   
elif User == "7":
    script7.run()
   
elif User == "8":
    script8.run()
   
elif User == "9":
    script9.run()
    
elif User == "10":
    script10.run()
    
elif User == "11":
    script11.run()
        
elif User == "12":
    script12.run()
        
elif User == "13":
    script13.run()
        
elif User == "14":
    script14.run()
        
elif User == "15":
    script15.run()
        
elif User == "16":
    script16.run()
        
elif User == "17":
    script17.run()
        
elif User == "18":
    script18.run()
        
elif User == "19":
    script19.run()
        
elif User == "20":
    script20.run()
    
else:
    sp(Fore.YELLOW + "try again...")
    sys.exit()