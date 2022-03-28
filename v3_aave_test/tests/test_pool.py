from brownie import config, network, accounts, Wei
from scripts import erc20, utils, pool
import pytest

# 1. Arrange, or set up, the conditions for the test
# 2. Act by calling some function or method
# 3. Assert that some end condition is true


@pytest.fixture(scope="module")
def dev_account():
    return utils.get_account("dev")


@pytest.fixture(scope="module")
def amount():
    return Wei("0.2 ether")


@pytest.fixture(scope="module")
def dai_addr():
    return config["networks"][network.show_active()]["dai"]


@pytest.fixture(scope="module")
def weth_addr():
    return config["networks"][network.show_active()]["weth"]


def test_get_pool():
    assert pool.get_pool() != None


def test_supply(dai_addr, amount, dev_account):
    a = erc20.balance_of(
        dev_account.address, config["networks"][network.show_active()]["aDAI"]
    )
    lp = pool.get_pool()
    erc20.approve_erc20(dev_account,amount,dai_addr,lp.address)
    x = erc20.check_allowance(dev_account.address,dai_addr,lp.address)
    print(f"approved: {x}")
    # Act
    pool.supply(dai_addr,amount,dev_account)
    b = erc20.balance_of(
        dev_account.address, config["networks"][network.show_active()]["aDAI"]
    )
    # Assert
    print(f"a: {a} b: {b}")
    assert (b-a) >= amount 