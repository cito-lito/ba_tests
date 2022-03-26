from brownie import accounts, config, network, Wei
from scripts import aave_deposit, erc20, pool, utils, weth

import time

# 1. Arrange, or set up, the conditions for the test
# 2. Act by calling some function or method
# 3. Assert that some end condition is true



def test_deposit_ether():
    # Arrange:
    account = utils.get_account("dev")
    token = "ether"
    amount = Wei("0.5 ether")
    eth_balance = account.balance()
    weth_balance = weth.balance_of(account.address)
    aWeth = erc20.balance_of(account.address, '0x608D11E704baFb68CfEB154bF7Fd641120e33aD4')
    print(aWeth)
    # Act:
    aave_deposit.deposit(account, token, amount)
    time.sleep(5)
    b = erc20.balance_of(account.address, '0x608D11E704baFb68CfEB154bF7Fd641120e33aD4')
    print(b) 
    assert (b-a) == amount