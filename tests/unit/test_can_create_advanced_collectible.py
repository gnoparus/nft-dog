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


def test_can_create_advanced_collectible():
    if network.show_active() not in LOCAL_BLOCKCHAIN_ENVIRONMENTS:
        pytest.skip()
    deploy_and_create_advance()
