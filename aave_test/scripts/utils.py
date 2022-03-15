from brownie import accounts, interface


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


def approve_erc20(account, amount, token_addr, spender_addr):
    """allow spender_addr to use your tokens
    Args:
        account (_type_): user account
        amount (_type_): token amount 
        token_addr (_type_): user token addr
        spender_addr (_type_): spender, contract, pool, eoa ...
    """
    token = interface.IERC20(token_addr)
    tx = token.approve(spender_addr, amount, {"from": account})
    tx.wait(1)
    amount = token.allowance(account.address, spender_addr)
    #print(amount.to("ether"))
    
    
    