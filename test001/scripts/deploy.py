from brownie import accounts, Owner

## add account: brownie accounts new nameOfneAccount
### accounts.load("my_account")

def deploy_owner():
    #use ganache chain:
    owner_contract = Owner.deploy({"from":accounts[1]})
    print(f"owner_contract is {owner_contract}")
    owner_acc = owner_contract.getOwner()
    print(f"owner is {owner_acc}")
    
    # change owner:
    tx = owner_contract.changeOwner("0x1667E22c87d39Ad1c9fC5D22123C42b7bcB2fC3d", {"from":accounts[1]})
    #tx.wait(1)
    owner_acc = owner_contract.getOwner()
    print(f"owner is {owner_acc}")



def main():
    deploy_owner()

