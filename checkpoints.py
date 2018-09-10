import requests
import dateutil.parser
from math import ceil
from datetime import datetime, timezone
from colorama import Fore, Style, init
init() #print dem colored outputs

updated = None

git_conn = True

time = datetime.now(timezone.utc)

h_t_s = "hours" #default

try:
    commits = requests.get('https://api.github.com/repos/turtlecoin/checkpoints/commits').json()
except:
    git_conn = False
    print(Fore.RED + "\nCould not retrieve checkpoints stats\n" + Style.RESET_ALL)

if git_conn:
    
    last_update = dateutil.parser.parse(commits[0]['commit']['author']['date'])

    def return_values():
        global updated    
        global h_t_s

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

        return updated

    return_values()    