import api
import requests
import os
import time

api = api.LeagueOfLegendsClientAPI()
try:
    while True:
        name = input('Enter your smurfer name: ')
        data = {"name":name}
        count = len(name)
        if count > 2 and count < 17:
            request = api.postSmurf('/lol-summoner/v1/summoners', data).json()
            try:
                if request['httpStatus']:
                    print('[!] Your Smurfer name is used already.')
                    
            except KeyError:
                os.system("taskkill /f /im LeagueClientUxRender.exe")
                print(f'[+] Have fun {name}!')
                print('[*] Restarting client...')
                print('[!] Script closing in 4s!')
                time.sleep(4)
                exit()
        else:
            print('[!] Your name need to have 3-16 characters.')
except KeyboardInterrupt:
    exit()
# method from x00bence lol-aram-boost
