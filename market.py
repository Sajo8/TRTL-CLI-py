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

import urllib.request
import json
from colorama import Fore, Style, init
init()

received_cmc = True

try:
    urllib.request.urlopen("https://api.coinmarketcap.com/v2/ticker/2958/?convert=LTC").read()
    r_mk_data = urllib.request.urlopen("https://api.coinmarketcap.com/v2/ticker/2958/?convert=LTC").read()
    p_mk_data = json.loads(r_mk_data)
except:
    received_cmc = False

if received_cmc:
    # value in usd
    mk_usd_s = p_mk_data['data']['quotes']['USD']['price']
    #convert to decimal notation
    mk_usd = "{:.10f}".format(float(mk_usd_s))

    #value in ltc
    mk_ltc_s = p_mk_data['data']['quotes']['LTC']['price']
    #convert to decimal notation
    mk_ltc = round(mk_ltc_s * 1e8, 2) # also round to 2 digits

    #24h price change
    h24_change = p_mk_data['data']['quotes']['USD']['percent_change_24h']

    #24h volume
    h24_vol_r = p_mk_data['data']['quotes']['USD']['volume_24h']
    #add commas
    h24_vol = "$" + "{:,.2f}".format(h24_vol_r)

    #circulating supply
    c_supply_r = p_mk_data['data']['circulating_supply']
    #add commas
    c_supply = "{:,.0f}".format(c_supply_r)

else:
    print(Fore.RED + "\nCould not retrieve market stats." + Style.RESET_ALL)