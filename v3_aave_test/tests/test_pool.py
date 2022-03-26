from brownie import config, network, accounts, Wei
from scripts import erc20, utils
import pytest

# 1. Arrange, or set up, the conditions for the test
# 2. Act by calling some function or method
# 3. Assert that some end condition is true


@pytest.fixture(scope="module")
def dev_account():
    return utils.get_account("dev")


@pytest.fixture(scope="module")
def amount():
    return Wei("0.5 ether")


@pytest.fixture(scope="module")
def token_addr():
    return config["networks"][network.show_active()]["dai"]
