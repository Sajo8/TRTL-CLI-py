"""
    Copyright (C) 2018 Sajo8

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <https://www.gnu.org/licenses/>.
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