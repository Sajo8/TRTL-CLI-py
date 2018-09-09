import requests
import re
from datetime import datetime
from math import ceil
from colorama import Fore, Style, init
init()

updated = None

git_conn1 = True
git_conn2 = True

now_time = str(datetime.now())
time_int = re.sub('[-:]', '', now_time)

time = time_int.split(' ')

try:
    pulls = requests.get('https://api.github.com/repos/turtlecoin/checkpoints/pulls').json()
except:
    git_conn1 = False
    print(Fore.RED + "\nCould not retrieve checkpoints stats\n" + Style.RESET_ALL)

if git_conn1:

    pull_time_raw = pulls[0]['created_at']

    pull_time_string = re.sub('[TZ]', ' ', pull_time_raw)

    pull_time_int = re.sub('[-:]', '', pull_time_string)

    pull_time = pull_time_int.split(' ')

try:
    commits = requests.get('https://api.github.com/repos/turtlecoin/checkpoints/commits').json()
except:
    git_conn2 = False
    print(Fore.RED + "\nCould not retrieve checkpoints stats\n" + Style.RESET_ALL)

if git_conn2:
    commit_time_raw = commits[0]['commit']['author']['date']

    commit_time_string = re.sub('[TZ]', ' ', commit_time_raw)

    commit_time_int = re.sub('[-:]', '', commit_time_string)

    commit_time = commit_time_int.split(' ')

if git_conn1 and git_conn2:

    def return_values():
        global updated    
    
        if int(commit_time[0]) > int(pull_time[0]):
            checkpoints = int(int(round(float(time[1]), 0)) - int(commit_time[1]))

        elif int(commit_time[0]) == int(pull_time[0]) and int(commit_time[1]) > int(pull_time[1]):
            checkpoints = int(int(round(float(time[1]), 0)) - int(commit_time[1]))

        elif int(commit_time[0]) == int(pull_time[0]) and int(commit_time[1]) < int(pull_time[1]):
            checkpoints = int(int(round(float(time[1]), 0)) - int(pull_time[1]))

        else:
            checkpoints = int(int(round(float(time[1]), 0)) - int(pull_time[1]))

        checkpoints = int(checkpoints) + 60000
        checkpoints = ceil(checkpoints)
        checkpoints = str(checkpoints)

        if len(str(checkpoints)) == 5:
            checkpoints = '0' + str(checkpoints)

        updated = list(checkpoints)
        updated = updated[0] + updated[1]
        return updated

    return_values()    
    