from web3 import Web3
rpc = "HTTP://127.0.0.1:7545"
web3 = Web3(Web3.HTTPProvider(rpc))
wallet_address = "0x2e7064fEB6641A21900D8C129A5b4c7F250e8b5a"


if web3.isConnected():
    if web3.isAddress(wallet_address):
        print('connected to rpc endpoint and wallet address is valid')
        balance = web3.eth.getBalance(wallet_address)
        print("Wallet Balance: ",web3.fromWei(balance,"ether"), "ETHER")


