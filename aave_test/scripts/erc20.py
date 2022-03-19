from brownie import interface


def erc20_contract(token_addr):
    return interface.IERC20(token_addr)

def approve_erc20(account, amount, token_addr, spender_addr):
    token = erc20_contract(token_addr)
    tx = token.approve(spender_addr, amount, {"from": account})
    tx.wait(1)
    return True

def balance_of(acc_addr, token_addr):
    token = erc20_contract(token_addr)
    return token.balanceOf(acc_addr)
        
def check_allowance(owner_addr, token_addr, spender_addr):
    token = erc20_contract(token_addr)
    return token.allowance(owner_addr, spender_addr)
