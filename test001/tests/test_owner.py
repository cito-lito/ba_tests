from brownie import accounts, Owner

def test_deploy():
    "check if owner is set correctly"
    #using ganache chain
    owner_contract = Owner.deploy({"from":accounts[0]})
    eoa_add = owner_contract.getOwner()
    assert eoa_add == accounts[0]

def test_change_owner():
    "change owner to accouts[1]"
    owner_contract = Owner.deploy({"from":accounts[0]})
    owner_contract.changeOwner(accounts[1],{"from": accounts[0]})
    assert accounts[1] == owner_contract.getOwner()