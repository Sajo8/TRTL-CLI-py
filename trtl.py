import market #processes and returns info for commands `m` or `market`
import network #processes and returns info for commands `n` or `network`
import msgs #add the big stringz in a seperate file
from askee import values #processes and returns info for commands `a` or `ascii`
import checkpoints #for c or checkpoints

from random import randint
from colorama import Fore, Style, init
from termcolor import colored
init() #init the colored stuff so it works on windows

running = True # so that checks for input
run1 = True #prints out on 1st launch if true

options_1 = ['help', 'h']
options_2 = ['version', 'v']

commands_1 = ['market', 'm']
commands_2 = ['supply', 's']
commands_3 = ['network', 'n']
commands_4 = ['price', 'p']
commands_5 = ['ascii', 'a']
commands_6 = ['ascii list', 'al']
commands_7 = ['checkpoints', 'c']
ascii_art =  ['flyingturtle', 'happyturtle', 'pineapple', 'seaturtle', 'snail', 'swanson', 'TRTL', 'turtle', 'turtlefighter', 'walker']



if run1:
	print(msgs.welcome_msg)
	run1 = False

try:
	while running:

		inp = str(input('> ')).lower().strip()

		if inp == options_1[0] or inp == options_1[1]:
			print(msgs.help_msg)
			continue

		elif inp == options_2[0] or inp == options_2[1]:
			print(msgs.version)
			continue

		elif inp == commands_1[0] or inp == commands_1[1]:

			if market.received_cmc:

				print("\nCurrent USD Price: $" + market.mk_usd)
				print("Current Litoshi Price: Ł" + str(market.mk_ltc) + "(litoshis)")
			
				#print in magenta if it's sub zero else print green. red 2 dark 4 me
				#using termcolor because colarama required only a string. if i converted it to string i couldnt use the inequality operator
				if market.h24_change < 0:
					print(colored("\n24h price change: " + str(market.h24_change) + "%", 'magenta'))

				else:
					print(colored("\n24h price change: " + str(market.h24_change) + "%", 'green'))

				print("24h volume: " + str(market.h24_vol))

				print("\nCirculating Supply: " + market.c_supply + " TRTL \n")
			else:
				print(Fore.RED + "\nCould not retrieve market stats, please try again.\n" + Style.RESET_ALL)
			continue

		elif inp == commands_2[0] or inp == commands_2[1]:
			if market.received_cmc:
				print("\nCirculating Supply: " + market.c_supply + " TRTL \n")
			else:
				print(Fore.RED + "\nCould not retrieve supply stats, please try again.\n" + Style.RESET_ALL)

			continue
		
		elif inp == commands_3[0] or inp == commands_3[1]:
			if network.received_info:
				print("\nNetwork block height: " + network.height)
				print("The current global hashrate is: " + network.hashrate + " MH/s")
				print("Mining difficulty: " + network.difficulty)
				print("Client version: " + network.client_version + "\n")
			else:
				print(Fore.RED + "\nCould not retrieve network stats, please try again.\n" + Style.RESET_ALL)
			continue
		
		elif inp.startswith(commands_4[0]) or inp.startswith(commands_4[1]):
			price_inp = inp.split()

			#get out of this conditional if anything other than p or price. needed since first elif needs to take into account the numbers as well, not just the command itself
			if price_inp[0] != commands_4[0] and price_inp[0] != commands_4[1]:
				print(Fore.RED + f"\nSorry, command not recognized: {inp}\n" + Style.RESET_ALL)
				continue
			
			if market.received_cmc:

				if len(price_inp) < 2:
					print("\nCurrent price: $" + str(market.mk_usd) + " or Ł" + str(market.mk_ltc) + "(litoshis)")
					print(Fore.YELLOW + " \nYou can also try 'price <amount> to calculate how much your TRTLs are worth. \n" + Style.RESET_ALL)
				else:
					price_in_usd = int(price_inp[1]) * float(market.mk_usd)
					price_in_ltc = int(price_inp[1]) * market.mk_ltc

					print("\nCurrent price: $" + str(market.mk_usd) + " or Ł" + str(market.mk_ltc) + "(litoshis)")

					print(str(price_inp[1]) + " TRTL is: $" + str(price_in_usd))
					print(str(price_inp[1]) + " TRTL is: Ł" + str(price_in_ltc) + "(litoshis)")

			else:
				print(Fore.RED + "\nCould not retrieve price stats, please try again.\n" + Style.RESET_ALL)

				continue

		elif inp == commands_6[0] or inp == commands_6[1]:
			print(msgs.ascii_msg)
			continue

		elif inp.startswith(commands_5[0]) or inp.startswith(commands_5[1]):

			ascii_inp = inp.lower().split()

			if ascii_inp[0] != commands_5[0] and ascii_inp[0] != commands_5[1]:
				print(Fore.RED + f"\nSorry, command not recognized: {inp}\n" + Style.RESET_ALL)
				continue
			
			if len(ascii_inp) <2:
				rand_number = randint(0, 9)

				print(values(rand_number))
				

			elif ascii_inp[1] == 'flyingturtle':
				print(values(0))

			elif ascii_inp[1] == 'happyturtle':
				print(values(1))

			elif ascii_inp[1] == 'pineapple':
				print(values(2))

			elif ascii_inp[1] == 'seaturtle':
				print(values(3))				

			elif ascii_inp[1] == 'snail':
				print(values(4))				

			elif ascii_inp[1] == 'swanson':
				print(values(5))				

			elif ascii_inp[1] == 'trtl':
				print(values(6))

			elif ascii_inp[1] == 'turtle':
				print(values(7))

			elif ascii_inp[1] == 'turtlefighter':
				print(values(8))
			elif ascii_inp[1] == 'walker':
				print(values(9))
			else:
				print(Fore.RED + f"\nCouldn't find ascii art specified: '{ascii_inp[1]}'" + Style.RESET_ALL)
			continue

		elif inp == commands_7[0] or inp == commands_7[1]:
			if checkpoints.git_conn:
				print(f"\nCheckpoints updated {checkpoints.updated} {checkpoints.h_t_s} ago.")
				print("Download checkpoints from: http://checkpoints.info\n")
			continue

		elif inp == "":
			continue

		elif inp == "exit" or inp == "e":
			print(Fore.YELLOW + 'Exiting...' + Style.RESET_ALL)
			break

		else:
			print(Fore.RED + f"\nSorry, command not recognized: {inp}\n" + Style.RESET_ALL)
			continue

except KeyboardInterrupt:
	running = False
	print(Fore.YELLOW + ' \n \nShutdown requested, exiting' + Style.RESET_ALL)

print('Bye')