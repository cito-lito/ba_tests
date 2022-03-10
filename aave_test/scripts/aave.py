from scripts.utils import get_account
from scripts import weth
from brownie import Wei, interface, network, config


def get_lending_pool_contract():
    #account = get_account("dev")
    lending_pool_addr_prov = interface.ILendingPoolAddressesProvider(
        config["networks"][network.show_active()]["aave_pool_addr_provider"])
    print(f"lending pool addr: {lending_pool_addr_prov}")
    lending_pool_contract = lending_pool_addr_prov.getLendingPool()
    print(f"lending pool contract: {lending_pool_contract}")
    return lending_pool_contract



def main():
    get_lending_pool_contract()
    