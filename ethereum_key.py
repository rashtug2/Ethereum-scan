from eth_account import Account

if __name__ == "__main__":
    acct = Account.create()
    
    print("Private key: %s, Public key:%s" % (acct.key.hex(), acct.address))
