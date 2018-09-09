import requests
import dateutil.parser
from datetime import datetime, timezone
from colorama import Fore, Style, init
init()

updated = None

git_conn = True

time = datetime.now(timezone.utc)

try:
    commits = requests.get('https://api.github.com/repos/turtlecoin/checkpoints/commits').json()
except:
    git_conn = False
    print(Fore.RED + "\nCould not retrieve checkpoints stats\n" + Style.RESET_ALL)

if git_conn:
    
    last_update = dateutil.parser.parse(commits[0]['commit']['author']['date'])

    def return_values():
        global updated    

        difference = time - last_update

        updated = int(difference.total_seconds() // 3600)

        return updated

    return_values()    
    