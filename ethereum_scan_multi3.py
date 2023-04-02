import time
import requests
from colorama import init
from termcolor import colored
from eth_account import Account

token = "A4F1HBCMZPYBMFKJVG7K2E9GRG9B4GTSNX"
wei = 1000000000000000000

private_key_default = 0
private_key_max = 1000000
steps = 20

if __name__ == "__main__":

  try:
    f = open("ethereum_scan.log", "r+")

    # Walkthrough the entire file
    for line in f:
      pass

    # Get private key value from last line
    private_key = line.split()[0]

    #print(private_key)

    # Convert private key string to int and increment it
    private_key_ini = int(private_key, base=16) + 1
  except:
    print('Warning: file does not exist, using default private_key')
    f = open("ethereum_scan.log", "a")
    private_key_ini = private_key_default

  print("Scan will start from: 0x%064X" % (private_key_ini))
  time.sleep(2)

  for x in range(private_key_ini, (private_key_ini + private_key_max), steps):
    accounts = dict()
    addresses = ""

    for i in range(steps):
      # Compute index
      j = x + i

      # Create a bytes array of 32bytes based on 'j'
      private_key = j.to_bytes(32, 'big')

      # Get public key/address based on private key
      acct = Account.from_key(private_key)

      #print("0x%s %s" % (private_key.hex(), acct.address))

      # Add private key and public key (Ether address) to the dict
      accounts[acct.address] = "0x" + private_key.hex()

      # Build field for http request
      addresses += acct.address + ","

    # Remove last character ','
    addresses = addresses[:-1]

    #print(accounts)
    #print(addresses)
    retry = 0
    end = 0

    while(end == 0):
      try:
        # Get balance information from Etherscan
        r = requests.get('https://api.etherscan.io/api?module=account&action=balancemulti&address=' + addresses + '&tag=latest&apikey=' + token)
        
        if(r.ok):
          end = 1
      except:
        retry = retry + 1
        print("Request error, retry %d..." % (retry))

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

          s = "%s %s %017.08f " % (private_key, address, balance)
          s_color = s

          # As long balance is not null, it means that the address was used at least once
          if(balance > 0):
            status = "Active"
            s += status
            s_color += colored(status, 'green')
          else:
            status = "Inactive"
            s += status
            s_color += colored(status, 'red')

          # Print to stdout (with color)
          print(s_color)

          # Save to file
          f.write(s + "\n")

    # 5 requests max per seconds (~200ms)
    time.sleep(0.250)

  f.close()
