import os
from eth_account import Account

if __name__ == "__main__":

  # Choose a random value, e.g: 16
  i = 16

  # Create a bytes array of 32bytes based on 'i'
  private_key = i.to_bytes(32, 'big')

  # Display private as string
  print(private_key.hex())

  # Get public key/address based on private key
  account = Account.from_key(private_key)

  print("Private key: 0x%s, Public key:%s" % (private_key.hex(), account.address))  
