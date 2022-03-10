from brownie import network, accounts, config


def get_account(added_account=None):
    if added_account:
        return accounts.load(added_account)
    return accounts[0]

