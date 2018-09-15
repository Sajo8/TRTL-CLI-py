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

from colorama import Fore, Style, init

version = Fore.YELLOW + """\
  
  TRTL CLI py
  Made by Sajo8
  Based off of TRTL CLI made by mrrovot, zack796, and brandonlehman

  Version 1.0.0
""" + Style.RESET_ALL

help_msg = Fore.YELLOW + """\

  Usage:  [options]

  TRTL CLI py

  Options:

	version|v  output the version number
	help|h     output this help message

  Commands:

	market|m       List market data
	supply|s       Lists circulating supply
	network|n      Shows network data
	price|p [qty]  Gives current price information
	ascii|a [pic]  Displays ASCII art
	ascii list|al  Displays a list of ASCII art
	checkpoints|c  Gets latest checkpoint update
	
	license|l      Show license information
  exit|e         Quit the program
""" + Style.RESET_ALL

welcome_msg = Fore.GREEN + """\

  Welcome to TRTL CLI py!

  Options:

	version|v  output the version number
	help|h     output the help message
 	license|l  show license information

""" + Style.RESET_ALL

ascii_msg = Fore.YELLOW + """\

  Available ASCII art:
    
    flyingturtle
    happyturtle
    pineapple
    seaturtle
    snail
    swanson
    TRTL
    turtle
    turtlefighter
    walker
""" + Style.RESET_ALL

license_msg = Fore.YELLOW + """\
  
  TRTL CLI py Copyright (C) 2018 Sajo8
  This program comes with ABSOLUTELY NO WARRANTY
  This is free software, and you are welcome to redistribute it
  under certain conditions
""" + Style.RESET_ALL
