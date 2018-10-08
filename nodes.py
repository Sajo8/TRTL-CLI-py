import requests
from prettytable import PrettyTable

from colorama import Fore, Style, init
init(autoreset=True) #init the colored stuff so it works on windows. autoreset resets it back to set cmd color by default every time

def nodes():

    t = PrettyTable(['Name', 'URL', 'Port', 'SSL'])

    nodes = requests.get('https://raw.githubusercontent.com/turtlecoin/turtlecoin-nodes-json/master/turtlecoin-nodes.json').json()

    nn = 0

    try:
        while True:
            node_name = Fore.GREEN + nodes['nodes'][nn]['name'] + Fore.RESET
            url_link = Fore.GREEN + nodes['nodes'][nn]['url'] + Fore.RESET
            port_no = Fore.YELLOW + str(nodes['nodes'][nn]['port']) + Fore.RESET
            ssl_stat = nodes['nodes'][nn]['ssl']
            if ssl_stat:
                ssl_status = Fore.GREEN + str(ssl_stat) + Fore.RESET
            else:
                ssl_status = Fore.RED + str(ssl_stat) + Fore.RESET

            t.add_row([node_name, url_link, port_no, ssl_status])
            nn += 1

    except IndexError:
        pass

    return {'table': t}
