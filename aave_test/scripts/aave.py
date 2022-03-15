
from scripts.utils import get_account 
from scripts import weth
from brownie import Wei, interface, network, config


def aave_deposit(asset, amount, on_behalf_of, referral_code=0):
    pool = get_lending_pool_contract()
    tx = pool.deposit(asset, amount, on_behalf_of.address, referral_code, {"from": on_behalf_of})
    tx.wait(1)
    amount = amount.to("ether")
    print(f"deposit {asset}: {amount}, tx is : {tx}")

def get_user_acc_data(addr):
    """ get account data
    Args:
        addr (_type_): account address
    Returns:
        tuple: 
    total_collateral_ETH,
    total_debt_ETH,
    available_borrow_ETH,
    liquidation_threshold,
    ltv,
    health_factor """
    
    pool = get_lending_pool_contract()
    return pool.getUserAccountData(addr) 

def get_lending_pool_contract():
    lending_pool_addr_prov = interface.ILendingPoolAddressesProvider(
        config["networks"][network.show_active()]["aave_pool_addr_provider"])
    lending_pool_addr = lending_pool_addr_prov.getLendingPool()
    lending_pool_contract = interface.ILendingPool(lending_pool_addr)
    return lending_pool_contract

    
if __name__ == "__main__":
    account = get_account("dev")
    asset = config["networks"][network.show_active()]["weth_token"]
