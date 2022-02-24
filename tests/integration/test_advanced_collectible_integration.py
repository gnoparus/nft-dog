from scripts.helpful_scripts import (
    LOCAL_BLOCKCHAIN_ENVIRONMENTS,
    fund_with_link,
    get_account,
    get_contract,
    OPENSEA_URL,
)
from scripts.create_collectible_advance import create_collectible_advance
from scripts.deploy_and_create_advance import deploy_and_create_advance
from brownie import AdvancedCollectible, network, config
from web3 import Web3
import pytest
import time


def test_advanced_collectible_integration():
    if network.show_active() in LOCAL_BLOCKCHAIN_ENVIRONMENTS:
        pytest.skip()
    get_account()
    advanced_collectible, creating_tx = deploy_and_create_advance()
    ### emit requestCollectible(requestId, msg.sender)
    time.sleep(180)

    assert advanced_collectible.tokenCounter() == 1
    # assert advanced_collectible.tokenIdToBreed(0) == STATIC_RNG % 3
    assert advanced_collectible.ownerOf(0) == get_account()
    assert advanced_collectible.balanceOf(get_account()) == 1


def main():
    test_advanced_collectible_integration()
