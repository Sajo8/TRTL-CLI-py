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

import msgs #add the big stringz in a seperate file
from market import market #processes and returns info for commands `m` or `market`
from network import network #processes and returns info for commands `n` or `network`
from askee import askee #processes and returns info for commands `a` or `ascii`
from checkpoints import checkpoints #for c or checkpoints
from price import price #for p or price

from random import randint # for random ascii art
from colorama import Fore, Style, init
init(autoreset=True) #init the colored stuff so it works on windows. autoreset resets it back to set cmd color by default every time

running = True # so that checks for input
run1 = True #prints out on 1st launch if true

help_options = ['help', 'h']
version_options = ['version', 'v']

market_commands = ['market', 'm']
supply_commands = ['supply', 's']
network_commands = ['network', 'n']
price_commands = ['price', 'p']
ascii_commands = ['ascii', 'a']
ascii_list_commands = ['ascii list', 'al']
checkpoints_commands = ['checkpoints', 'c']
license_commands = ['license', 'l']
exit_commands = ['exit', 'e']


if run1:
	print(msgs.license_msg)
	print(msgs.welcome_msg)
	run1 = False

try:
	while running:

		inp = str(input('> ')).lower().strip()
		split_input = inp.split()
		if split_input != []:
			command = split_input[0]
			command_args = split_input[1:]
		else:
			continue

		if command in help_options:
			print(msgs.help_msg)
			continue

		elif command in version_options:
			print(msgs.version)
			continue

		elif command in market_commands:
			mk_info = market()
			if mk_info['received_info']:

				print(f"\nCurrent USD Price: ${mk_info['mk_usd']}")
				print(f"Current Litoshi Price: Ł{mk_info['mk_ltc']} (litoshis)")
					
				#print in magenta if it's sub zero else print green. red 2 dark 4 me
				if mk_info['h24_change'] < 0:
					print(Fore.MAGENTA + "\n24h price change: " + str(mk_info['h24_change']) + '%')

				else:
					print(Fore.GREEN + "\n24h price change: " + str(mk_info['h24_change']) + '%')

				print("24h volume: " + str(mk_info['h24_vol']))

				print(f"\nCirculating Supply: {mk_info['c_supply']} TRTL \n")
			else:
				print(Fore.RED + "\nCould not retrieve market stats, please try again. \n")

				continue


		elif command in supply_commands:
			mk_info = market()
			if mk_info['received_info']:
				print(f"\nCirculating Supply: {mk_info['c_supply']} TRTL \n")
			else:
				print(Fore.RED + "\nCould not retrieve market stats, please try again. \n")

			continue
		
		elif command in network_commands:
			network_info = network()

			if network_info['received_info']:

				print(f"\nNetwork block height: {network_info['height']}")
				print(f"The current global hashrate is: {network_info['hashrate']} MH/s")
				print(f"Mining difficulty: {network_info['difficulty']}")
				print(f"Client version: {network_info['client_version']} \n")

			else:
				print(Fore.RED + "\nCould not retrieve network stats, please try again. \n")

			continue


		elif command.startswith('p') or command.startswith('price'):

			#get out of this conditional if anything other than p or price. needed since first elif needs to take into account the numbers as well, not just the command itself
			if command not in price_commands:
				print(Fore.RED + f"\nSorry, command not recognized: {inp}\n")
				continue

			if command and not command_args: #if command passed true and arent any additional args
				price_info = price() # get info
				if price_info['received_info']: # if succesfully received

					print("\nCurrent price: $" + str(price_info['mk_usd']) + " or Ł" + str(price_info['mk_ltc']) + "(litoshis)")
					print(Fore.YELLOW + " \nYou can also try 'price <amount> to calculate how much your TRTLs are worth. \n")

					continue
			
				else:
					print(Fore.RED + "\nCould not retrieve price stats, please try again.\n") #couldnt get stats for some reason

					continue
			else: #there are additional arguments passed
				command_args = list(map(int, command_args))[0] #convert list item to integer so that it can parse it. and grab it's value with [0]
				price_info = price(command_args) # get stats
				if price_info['received_info']: #if response 
					print("\nCurrent price: $" + str(price_info['mk_usd']) + " or Ł" + str(price_info['mk_ltc']) + "(litoshis)")

					print(str(command_args) + " TRTL is: $" + str(price_info['price_in_usd']))
					print(str(command_args) + " TRTL is: Ł" + str(price_info['price_in_ltc']) + "(litoshis)")

					continue
				else:
					print(Fore.RED + "\nCould not retrieve price stats, please try again.\n") #cudnt get stats for some reason

					continue

		elif command in ascii_list_commands:
			print(msgs.ascii_msg)
			continue

		elif command.startswith('a') or command.startswith('ascii'):

			if command not in ascii_commands: #once again, check if the thing passed isnt a or ascii
				print(Fore.RED + f"\nSorry, command not recognized: {inp}\n")
				continue
			
			if not command_args: # if it's only a or ascii
				rand_number = randint(0, 9) #get random number

				print(askee(rand_number)['ascii']) #pass to function which handles it

				
			else: # there are args for a specific art
				
				if command_args[0] == 'list':
					print(msgs.ascii_msg)
					continue
				
				ascii_art = askee(str(command_args[0])) # pass it to function

				if ascii_art['file_exists']: # if the filename specified exists
					print(ascii_art['ascii']) #print it
				else: #file name dont exist
					print(Fore.RED + "\nCouldn't find ascii art mentioned, please verify your spelling\n") #error out

				continue

		elif command in checkpoints_commands:
			checkpoint_info = checkpoints()
			if checkpoint_info['received_info']:

				print(f"\nCheckpoints updated {checkpoint_info['updated']} {checkpoint_info['h_t_s']} ago.")
				print("Download checkpoints from: http://checkpoints.info\n")
			else:
				print(Fore.RED + "\nCouldn't receive checkpoint information, please try again \n")
			continue

		elif command in license_commands:
			print(msgs.license_msg)
			continue

		elif command in exit_commands:
			print(Fore.YELLOW + 'Exiting...')
			break

		else:
			print(Fore.RED + f"\nSorry, command not recognized: {inp}\n")
			continue

except KeyboardInterrupt:
	running = False
	print(Fore.YELLOW + ' \n \nShutdown requested, exiting')

print('Bye')