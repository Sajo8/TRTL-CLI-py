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
init(autoreset=True)

def network():

	try:
		print(Fore.YELLOW + "\nReceiving network stats...")

		network_info = requests.get('http://public.turtlenode.io:11898/getinfo').json()

		# grab height
		height = str(network_info['height'])

		#grab hashrate
		hashrate_kh = network_info['hashrate']
		hashrate_decimals = hashrate_kh / 1000000 #convert to mhs
		hashrate = str(round(hashrate_decimals,2)) #round to 2 decimal places

		# grab diff with  no commas
		difficulty_nocomas = network_info['difficulty']
		difficulty = '{:,}'.format(difficulty_nocomas) #add commas

		client_version = str(network_info['version']) #get client version

		return {'received_info': True, 'height': height, 'hashrate': hashrate, 'difficulty': difficulty, 'client_version': client_version}
	
	except:
		return {'received_info': False}

if __name__ == "__main__":
	print('\n', network())
