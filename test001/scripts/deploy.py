from brownie import accounts, network, config,  Owner

## add account: brownie accounts new nameOfneAccount
### accounts.load("my_account")

def deploy_owner():
    #
    account = get_account()
    owner_contract = Owner.deploy({"from":account})
    print(f"owner_contract is {owner_contract}")
    owner_acc = owner_contract.getOwner()
    print(f"owner is {owner_acc}")
    
    # change owner:
    #tx = owner_contract.changeOwner("0x1667E22c87d39Ad1c9fC5D22123C42b7bcB2fC3d", {"from":account})
    #tx.wait(1)
   # owner_acc = owner_contract.getOwner()
   # print(f"owner is {owner_acc}")


def get_account():
    if network.show_active() == "development":
        return accounts[0]
    else:
        return accounts.load("dev")

def main():
    deploy_owner()

