from colorama import Fore, Style, init

version = Fore.YELLOW + """\
  
  TRTL CLI py
  Made by Sajo8
  Based off of TRTL CLI made by mrrovot and Xaz

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
	
	exit|e         Quit the program
""" + Style.RESET_ALL

welcome_msg = Fore.GREEN + """\

  Welcome to TRTL CLI py!

  Options:

	version|v  output the version number
	help|h     output the help message
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
