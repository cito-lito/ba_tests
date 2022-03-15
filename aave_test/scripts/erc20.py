from brownie import interface


def erc20_contract(token_addr):
    return interface.IERC20(token_addr)

def approve_erc20(account, amount, token_addr, spender_addr):
    """allow spender_addr to use your tokens
    Args:
        account (_type_): user account
        amount (_type_): token amount 
        token_addr (_type_): user token addr
        spender_addr (_type_): spender, contract, pool, eoa ...
    """
    token = erc20_contract(token_addr)
    tx = token.approve(spender_addr, amount, {"from": account})
    tx.wait(1)
        
def check_allowance(owner_addr, token_addr, spender_addr):
    token = erc20_contract(token_addr)
    return token.allowance(owner_addr, spender_addr)
    #print(amount.to("ether"))
