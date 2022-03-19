from brownie import network, Wei, config
from scripts import erc20, pool, utils, weth


def deposit(account, token, amount):

    #### if token is supported :
    token_addr = config["networks"][network.show_active()][token]
    balance = erc20.balance_of(account.address, token_addr)
    balance = balance.to("ether")
    print(f"account: {account.address} token: {token_addr} balance: {balance}")

    lending_pool = pool.get_lending_pool()

    allowed = erc20.check_allowance(account.address, token, lending_pool.address)
    print(allowed)
    # pool.deposit(token, amount, account)

    # result = pool.withdraw(token, amount,account)
    # result.info()
    # data = pool.get_user_acc_data(account.address)
    # for i in data:
    #    print(i.to("ether"))


def ether_deposit(account, amount):
    weth_token = config["networks"][network.show_active()]["weth_token"]
    weth_balance = erc20.balance_of(account.address, weth_token)
    eth_balance = account.balance()
    lending_pool = pool.get_lending_pool()
    
    ## not sure if needed: avoid vector attack: approve && transfer only the req amount
    allowed_amount = erc20.check_allowance(account.address, weth_token, lending_pool.address)
    if allowed_amount > 0:
        erc20.approve_erc20(account, 0, weth_token, lending_pool.address)
        
    if weth_balance >= amount:
        erc20.approve_erc20(account, amount, weth_token, lending_pool.address)
        pool.deposit(weth_token, amount, account)
    elif eth_balance >= (amount - weth_balance):
        # get weth from eth and deposit:
        weth_needed = amount - weth_balance
        weth.deposit(account, weth_needed)
        erc20.approve_erc20(account, amount, weth_token, lending_pool.address)
        pool.deposit(weth_token, amount, account)
    else:
        ## errors, amount...
        pass


def main():
    account = utils.get_account("dev")
    token = config["networks"][network.show_active()]["weth_token"]
    # deposit(account, token, Wei("0.05 ether"))
    ether_deposit(account, 0)
    pass


if __name__ == "__main__":
    main()
