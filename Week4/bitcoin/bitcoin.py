import sys
import requests

if(len(sys.argv) != 2):
    sys.exit("Missing command-line argument")

else:
    try:
        unit = float(sys.argv[1])
    except ValueError:
        sys.exit("Command-line argument is not a number")

r = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
data = r.json()
money_per_unit = data["bpi"]["USD"]["rate_float"]

amount = money_per_unit * unit
print(f"${amount:,.4f}")
