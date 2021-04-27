import os
import requests
import time

GREEN = "\033[1;32m"
RED = "\033[1;31m"
RESET = "\33[0;0m"

userValidate = "null"
findSname = ['Facebook', 'Twitter', 'Instagram', 'YouTube', 'Pinterest', 'Skype', 'TikTok', 'Dailymotion', 'SoundCloud', 'github', '0x00sec', 'Pastebin', 'Crackedto', 'Linktree']
findLink = ['www.facebook.com/', 'twitter.com/', 'www.instagram.com/', 'www.youtube.com/', 'gr.pinterest.com/', 'www.skypli.com/profile', 'www.tiktok.com/@', 'dailymotion.com/', 'soundcloud.com/', 'github.com/', '0x00sec.org/u/', 'pastebin.com/u/', 'cracked.to/', 'linktr.ee/']

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def style():
    clear()
    print('='*60+'\n'+' '*25+'FireOSINT'+'\n'+'='*60+'\n')

def ValidRun():
    lockSelect = 0
    for f in range(len(findSname)):
        url = 'https://'+str(findLink[lockSelect])+str(userValidate)
        if requests.get(url).status_code == 200:
            print(GREEN+'[+] '+RESET+str(findSname[lockSelect]) +' --> True | '+str(url))
        else:
            print(RED+'[-] '+RESET+str(findSname[lockSelect]) +' --> False')
        lockSelect = lockSelect + 1

style()
userValidate = input('Username to validade: ')
style()
print('Finding ['+str(userValidate)+']...')
print('Time: '+str(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime()))+'\n')
ValidRun()
print('\n')
