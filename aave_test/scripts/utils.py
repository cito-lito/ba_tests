from brownie import accounts, network, config


SUPPORTED_TOKENS = config["networks"][network.show_active()]

def get_account(added_account=None):
    """load personal account if passed, else use ganache account
    Args:
        added_account (_type_, optional): added account. Defaults to None.
    Returns:
        _type_: account
    """
    if added_account:
        return accounts.load(added_account)
    return accounts[0]



    
    
    