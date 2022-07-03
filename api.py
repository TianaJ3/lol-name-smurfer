import base64
import configparser
import ctypes
import os
import psutil
import requests
import sys
from urllib3 import disable_warnings

disable_warnings()

def get_process_by_name(process_name):
    while True:
        for proc in psutil.process_iter():
            try:
                if process_name in proc.name():
                    return proc
            except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
                pass

class LeagueOfLegendsClientAPI(object):
    
    def __init__(self):
        print('Waiting league client...')
        self.process = get_process_by_name("LeagueClientUx")
        
        try:
            self.lockfile = open(os.path.join(self.process.cwd(), "lockfile"), 'r').read()
        except:
            ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, " ".join(sys.argv), None, 1)
            exit()
        print('[*] Connected to League; Insert your smurf name to create a account, ^C to exit.')
        split = self.lockfile.split(":")

        self.process_name = split[0]
        self.process_id = split[1]
        self.port = split[2]
        self.password = str(base64.b64encode(("riot:" + split[3]).encode("utf-8")), "utf-8")
        self.protocol = split[4]
    
    def postSmurf(self, path, json=None):        
        return requests.post(
            self.protocol + "://127.0.0.1:" + self.port + path,
            verify=False,
            headers={"Authorization": "Basic " + self.password,"X-Riot-Source": "rcp-fe-lol-navigation"},
            json=json
        )
