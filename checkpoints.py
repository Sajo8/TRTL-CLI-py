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
import dateutil.parser
from math import ceil
from datetime import datetime, timezone
from colorama import Fore, Style, init
init(autoreset=True) #print dem colored outputs

def checkpoints():

	print(Fore.YELLOW + 'Receiving checkpoint information...')

	time = datetime.now(timezone.utc)

	h_t_s = "hours" #default

	try:
		commits = requests.get('https://api.github.com/repos/turtlecoin/checkpoints/commits').json()
		
		last_update = dateutil.parser.parse(commits[0]['commit']['author']['date'])

		difference = time - last_update

		if int(difference.total_seconds()) < 60:
			h_t_s = "seconds" #updated just seconds ago
			updated = ceil(difference.total_seconds())

		elif int(difference.total_seconds() / 60) < 60: #if minutes less than 60
			h_t_s = "minutes"
			updated = ceil(difference.total_seconds() / 60)

		elif int(difference.total_seconds() / 3600) < 24: #if hours less than 24
			h_t_s = "hours"
			updated = ceil(difference.total_seconds() / 3600)

		else:
			h_t_s = "days" #no checks for a year or month lol 
			updated = ceil((difference.total_seconds() / 3600) / 24)

		return {'received_info': True, 'updated': updated, 'h_t_s': h_t_s}

	except:
		return {'received_info': False}