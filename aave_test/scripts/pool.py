from brownie import Wei, interface, network, config
from scripts import utils, erc20, weth


def deposit(asset_addr, amount, on_behalf_of, referral_code=0):
    """deposit asset into the lending pool
    Args:
        asset_addr: address of the token
        amount : amount
        on_behalf_of : user, asset owner
        referral_code (int, optional):  Defaults to 0.
    """
    pool = get_lending_pool()
    tx = pool.deposit(
        asset_addr, amount, on_behalf_of.address, referral_code, {"from": on_behalf_of}
    )
    tx.wait(1)


def withdraw(asset_addr, amount, to):
    pool = get_lending_pool()
    tx = pool.withdraw(asset_addr, amount, to.address, {"from": to})
    tx.wait(1)
    return tx


def get_user_acc_data(addr):
    """get account data
    Args:
        addr (_type_): account address
    Returns:
        tuple:
    total_collateral_ETH,
    total_debt_ETH,
    available_borrow_ETH,
    liquidation_threshold,
    ltv,
    health_factor"""
    pool = get_lending_pool()
    return pool.getUserAccountData(addr)


def get_lending_pool():
    pool_addr_prov = interface.ILendingPoolAddressesProvider(
        config["networks"][network.show_active()]["aave_pool_addr_provider"]
    )
    pool_addr = pool_addr_prov.getLendingPool()
    return interface.ILendingPool(pool_addr)


def main():
    # check eth, weth
    addr = config["networks"][network.show_active()]["weth_token"]
    lp = get_lending_pool()
    account = utils.get_account("dev")
    balance = account.balance().to("ether")
    amount = Wei("0.1 ether")
    print(f"balance is: {balance}")
    print(weth.balance_of(account.address))
    weth.deposit(account, amount)
    erc20.approve_erc20(account, amount, addr, lp.address )

    deposit(addr, amount, account)
    print(weth.balance_of(account.address))


if __name__ == "__main__":
    main()
