from scripts.helpful_scripts import (
    fund_with_link,
    get_account,
    get_contract,
    OPENSEA_URL,
)
from brownie import AdvancedCollectible, network, config
from web3 import Web3


def create_collectible_advance():
    account = get_account()
    advanced_collectible = AdvancedCollectible[-1]
    fund_with_link(
        advanced_collectible.address, account=account, amount=Web3.toWei(0.1, "ether")
    )
    creating_tx = advanced_collectible.createCollectible({"from": account})
    creating_tx.wait(1)
    print(f"Created Collectible")
    return creating_tx


def main():
    create_collectible_advance()
