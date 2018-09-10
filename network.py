"""import urllib.request
import json

raw_json = urllib.request.urlopen("http://public.turtlenode.io:11898/getinfo").read()
    

get_info = json.loads(raw_json)
"""
import requests
from colorama import Fore, Style, init
init() 

received_info = True

try:
    get_info = requests.get('http://public.turtlenode.io:11898/getinfo').json()
except:
    received_info = False

if received_info:

    height = str(get_info['height'])

    hashrate_kh = get_info['hashrate']
    hashrate_decimals = hashrate_kh / 1000000 #convert to mhs
    hashrate = str(round(hashrate_decimals,2)) #round to 2 decimal places

    difficulty_nocomas = get_info['difficulty']
    difficulty = '{:,}'.format(difficulty_nocomas)

    client_version = str(get_info['version'])

else:
    print(Fore.RED + "\nCould not retrieve network stats." + Style.RESET_ALL)