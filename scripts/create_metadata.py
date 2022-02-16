from scripts.helpful_scripts import (
    fund_with_link,
    get_account,
    get_contract,
    OPENSEA_URL,
)
from brownie import AdvancedCollectible, network, config
from web3 import Web3


def create_metadata():
    advanced_collectible = AdvancedCollectible[-1]
    number_of_advanced_collectibles = advanced_collectible.tokenCounter()
    print(f"You've created {number_of_advanced_collectibles} collectible(s)")


def main():
    create_metadata()
