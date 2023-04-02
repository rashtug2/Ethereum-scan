import requests
from eth_account import Account

token = "A4F1HBCMZPYBMFKJVG7K2E9GRG9B4GTSNX"
wei = 1000000000000000000

if __name__ == "__main__":
    
    # Generate an account (private and public keys)
    acct = Account.create()

    # Get balance information from Etherscan
    r = requests.get('https://api.etherscan.io/api?module=account&action=balance&address=' + acct.address + '&tag=latest&apikey=' + token)
    
    #print(r.text)

    if(r.ok):
      # Response from Ethersan is build on json, so let's get the "result" value
      balance = r.json()['result']
      balance = float(balance)/wei

      # Convert balance in Ether (in wei by default)
      print("%s %s %.06f" % (acct.key.hex(), acct.address, balance))
