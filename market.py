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

    def market_values():
        return mk_usd
        return mk_ltc
        return h24_change
        return h24_vol
        return c_supply

else:
    print(Fore.RED + "\nCould not retrieve market stats." + Style.RESET_ALL)