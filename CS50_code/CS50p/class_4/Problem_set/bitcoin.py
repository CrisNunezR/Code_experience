"""

In a file called bitcoin.py, implement a program that:

Expects the user to specify as a command-line argument
the number of Bitcoins, n, that they would like to buy.

If that argument cannot be converted to a float,
the program should exit via sys.exit with an error message.

Queries the API for the CoinDesk Bitcoin Price Index
at https://api.coindesk.com/v1/bpi/currentprice.json,
which returns a JSON object, among whose nested keys
is the current price of Bitcoin as a float. Be sure to
catch any exceptions.

JSON structure:
{"time":
    {
        "updated":"Aug 8, 2023 18:41:00 UTC",
        "updatedISO":"2023-08-08T18:41:00+00:00",
        "updateduk":"Aug 8, 2023 at 19:41 BST"
    },
    "disclaimer":"This data was produced from the CoinDesk Bitcoin Price Index (USD). Non-USD currency data converted using hourly conversion rate from openexchangerates.org",
    "chartName":"Bitcoin",
    "bpi": {
        "USD":{"code":"USD","symbol":"&#36;","rate":"29,903.6615","description":"United States Dollar","rate_float":29903.6615},
        "GBP":{"code":"GBP","symbol":"&pound;","rate":"24,987.2603","description":"British Pound Sterling","rate_float":24987.2603},
        "EUR":{"code":"EUR","symbol":"&euro;","rate":"29,130.5322","description":"Euro","rate_float":29130.5322}
            }
}

"""

"""
How to API call in python
source: https://www.dataquest.io/blog/python-api-tutorial/
    install requests if not installed (pip install requests)

"""

"""
format as USD with 4 decimal places
https://stackoverflow.com/questions/21208376/converting-float-to-dollars-and-cents
'${:,.4f}'.
"""

import sys
import requests
import json

def main():

    #validates there is an argument given
    if len(sys.argv) != 2:
        sys.exit("Missing command-line argument")
        #"Usage python bitcoin.py [bitcoins to buy]"
    try:
        bitcoins = float(sys.argv[1])
    except:
        sys.exit("Command-line argument is not a number")

    bitcoin_value = bitcoin_api()
    print(f"${bitcoins * bitcoin_value:,.4f}")

#fetches the current value of a bitcoin as a float using an API
def bitcoin_api() -> float:
    try:
        response = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
    except requests.RequestException:
        print("error with bitcoin API")
    if response.status_code == 200:
        data = response.json()
        return float(data['bpi']['USD']['rate_float'])
        #print("sucessfully fetched the data")
    else:
        print(f"{response.status_code} error with request")
        return 0





    return 2

if __name__ == "__main__":
    main()