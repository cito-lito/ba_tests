from brownie import  Owner


## read the last set owner of the contract
def get_owner():
    #last deployed contract
    owner_contract = Owner[-1]
    print(owner_contract.getOwner())
    
def main():
    get_owner()
