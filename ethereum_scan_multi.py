import requests
from eth_account import Account

token = "A4F1HBCMZPYBMFKJVG7K2E9GRG9B4GTSNX"
wei = 1000000000000000000

if __name__ == "__main__":
    
    accounts = dict()
    addresses = ""

    # Generate 20 accounts (Etherscan limit)
    for x in range(20):
      # Generate an account (private and public keys)
      acct = Account.create()

      # Add private key and public key (Ether address) to the dict
      accounts[acct.address] = acct.key.hex()

      # Build field for http request
      addresses += acct.address + ","

    # Remove last character ','
    addresses = addresses[:-1]

    #print(accounts)
    #print(addresses)

    # Get balance information from Etherscan
    r = requests.get('https://api.etherscan.io/api?module=account&action=balancemulti&address=' + addresses + '&tag=latest&apikey=' + token)
    
    #print(r.text)

    if(r.ok):
      # Response from Ethersan is build on json, so let's get the decoded data
      j = r.json()

      # Get list of accounts and balance (list of dicts)
      l = j['result']
      #print(l)

      # Build dict from list
      tmp = dict()

      for infos in l:
        tmp[infos['account']] = infos['balance']

      for address, private_key in accounts.items():
        # Extract balance information
        balance = tmp[address]
        #print(balance)

        # Convert balance in Ether (in wei by default) 
        balance = float(balance)/wei

        print("%s %s %.06f" % (private_key, address, balance))
