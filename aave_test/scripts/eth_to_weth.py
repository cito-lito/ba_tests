from brownie import accounts, interface, config, network, Wei


    
def eth_to_weth():
    account = accounts.load("dev")
    print(f"account is {account}")
    #token = config(["networks"][network.show_active()]["weth_token"])
    weth = interface.WethInterface('0xd0A1E359811322d97991E03f863a0C30C2cF029C')
    ##deposit eth and get weth
    tx = weth.deposit({"from":account, "value": Wei("0.3 ether")})   
    tx.wait(1)
    return tx 
    

def main():
    
    eth_to_weth()