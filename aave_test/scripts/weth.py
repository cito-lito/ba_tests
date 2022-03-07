from brownie import accounts, interface, config, network, Wei


    
def deposit(account, amount):
    weth = interface.WethInterface(config["networks"][network.show_active()]["weth_token"])
    tx = weth.deposit({"from":account, "value":amount})   
    tx.wait(1)
    return tx 
    
def witdraw(account, amount):
    weth = interface.WethInterface(config["networks"][network.show_active()]["weth_token"])
    tx = weth.withdraw(amount, {"from":account})    
    tx.wait(1)
    return tx 
    

def main():
    ## checking...
    account = accounts.load("dev")
    tx = deposit(account, Wei("0.2 ether"))  
    print(f"deposit transaction is: {tx}")
    tx = witdraw(account, Wei("0.1 ether"))  
    print(f"witdraw transaction is: {tx}")
    
if __name__ == "__main__":
    main()