from scripts.utils import get_account
from scripts import weth
from brownie import Wei



def get_lending_pool():
    pass



def main():
    account = get_account()
    tx = weth.deposit(account, Wei("0.2 ether"))
    print(tx)