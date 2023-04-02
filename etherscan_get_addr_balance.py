import requests

token = "A4F1HBCMZPYBMFKJVG7K2E9GRG9B4GTSNX"
address = "0x0904FbB79267CDD92352e53Cf5d98906Ae02bB82"

wei = 1000000000000000000

'''
 Get Ether Balance for a Single Address

 Request:
 https://api.etherscan.io/api
   ?module=account
   &action=balance
   &address=0xde0b295669a9fd93d5f28d9ec85e40f4cb697bae
   &tag=latest
   &apikey=YourApiKeyToken
 Response:
   {
   "status":"1",
   "message":"OK",
   "result":"40891626854930000000000" 
   }

   Note: the result (balance) is returned in wei 
'''

if __name__ == "__main__":
    
    # Get balance information from Etherscan
    r = requests.get('https://api.etherscan.io/api?module=account&action=balance&address=' + address + '&tag=latest&apikey=' + token)
    
    #print(r.text)

    if(r.ok):
      # Response from Ethersan is build on json, so let's get the "result" value
      balance = r.json()['result']

      # Convert balance in Ether (in wei by default)
      print("Ether addr: %s, Balance: %.06f Eth" % (address, float(balance)/wei))


