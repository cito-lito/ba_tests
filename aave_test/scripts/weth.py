from brownie import accounts, interface, config, network, Wei

def deposit(account, amount):
    """deposit eth and geth weth
    Args:
        account (_type_): account   
        amount (_type_): amount
    Returns:
        _type_:  deposit tx
    """
    weth = weth_contract()
    tx = weth.deposit({"from":account, "value":amount})   
    tx.wait(1)
    return tx 
    
def witdraw(account, amount):
    weth = weth_contract()
    tx = weth.withdraw(amount, {"from":account})    
    tx.wait(1)
    return tx 

def balance_of(addr):
    weth = weth_contract()
    return weth.balanceOf(addr)
    
def weth_contract():
    return (interface.WethInterface(config["networks"][network.show_active()]["weth_token"]))
    

def main():
    ## checking...
    account = accounts.load("dev")
    #tx = deposit(account, Wei("0.2 ether"))  
    #print(f"deposit transaction is: {tx}")
    #tx = witdraw(account, Wei("0.1 ether"))  
    #print(f"witdraw transaction is: {tx}")
    print(balance_of(account.address))
    
if __name__ == "__main__":
    main()