
from scripts.utils import get_account
from scripts import weth
from brownie import Wei, interface, network, config


def aave_deposit(asset, amount, on_behalf_of, referral_code=0):
    pool = get_lending_pool_contract()
    tx = pool.deposit(asset, amount, on_behalf_of.address, referral_code, {"from": on_behalf_of})
    tx.wait(1)
    amount = amount.to("ether")
    print(f"deposit {asset}: {amount}, tx is : {tx}")

def approve_erc20(account, amount, token_addr, spender_addr):
    """allow spender addr to use your tokens

    Args:
        account (_type_): user account
        amount (_type_): token amount
        token_addr (_type_): user token addr
        spender_addr (_type_): spender, contract, pool, eoa ...
    """
    token = interface.IERC20(token_addr)
    tx = token.approve(spender_addr, amount, {"from": account})
    tx.wait(1)
    print(f"tx deposit: {tx}")
    

def get_lending_pool_contract():

    lending_pool_addr_prov = interface.ILendingPoolAddressesProvider(
        config["networks"][network.show_active()]["aave_pool_addr_provider"])
    print(f"lending pool addr: {lending_pool_addr_prov}")
    lending_pool_addr = lending_pool_addr_prov.getLendingPool()
    lending_pool_contract = interface.ILendingPool(lending_pool_addr)

    return lending_pool_contract


def main():
    ### cheecking...
    account = get_account("dev")
    asset = config["networks"][network.show_active()]["weth_token"]
    print("deposit eth, get weth...")
    weth.deposit(account, Wei("0.2 ether"))
    pool = get_lending_pool_contract()
    print("approve weth to lending pool")
    approve_erc20(account, Wei("0.2 ether"),asset, pool.address)
    print("deposit into the lending pool")
    aave_deposit(asset=asset, amount=Wei("0.2 ether"), on_behalf_of=account)
    
    
if __name__ == "__main__":
    main()