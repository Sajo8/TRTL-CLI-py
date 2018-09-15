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

from market import market
from colorama import Fore, Style, init
init(autoreset=True)


def price(args=None):

	print(Fore.YELLOW + "\nReceiving price stats...")

	try:
		mk_info = market()

		if not args:
			#print(Fore.YELLOW + " \nYou can also try 'price <amount> to calculate how much your TRTLs are worth. \n")

			return {'received_info': True, 'mk_usd': mk_info['mk_usd'], 'mk_ltc': mk_info['mk_ltc']}

		elif args:
			
			price_in_usd = round(int(args) * float(mk_info['mk_usd']), 2) #get equiv in ltc and round to 2
			price_in_ltc = round(int(args) * float(mk_info['mk_ltc']), 2) #get equiv in ltc and round to 2

			return {'received_info': True, 'mk_usd': mk_info['mk_usd'], 'mk_ltc': mk_info['mk_ltc'], 'price_in_usd': price_in_usd, 'price_in_ltc': price_in_ltc}

		else:
			return {'received_info': False}
	
	except:
		print(Fore.RED + "\nCould not receive price stats, please try again")
