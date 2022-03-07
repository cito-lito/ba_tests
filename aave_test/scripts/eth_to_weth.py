from brownie import accounts, interface, config, network, Wei


    
def eth_to_weth(account):
    #token = config(["networks"][network.show_active()]["weth_token"])
    weth = interface.WethInterface(config["networks"][network.show_active()]["weth_token"])
    ##deposit eth and get weth
    tx = weth.deposit({"from":account, "value": Wei("0.05 ether")})   
    tx.wait(1)
    return tx 
    
def weth_to_eth(account):
    weth = interface.WethInterface('0xd0A1E359811322d97991E03f863a0C30C2cF029C')
    tx = weth.withdraw(Wei("0.2 ether"), {"from":account})    
    tx.wait(1)
    return tx 
    
    
    
def main():
    account = accounts.load("dev")
    weth_to_eth(account)
    #eth_to_weth(account)