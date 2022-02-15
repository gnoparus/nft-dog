from scripts.helpful_scripts import LOCAL_BLOCKCHAIN_ENVIRONMENTS, get_account
from brownie import network
import pytest
from scripts.deploy_and_create_simple import deploy_and_create_simple


def test_can_create_simple_collectible():
    if network.show_active() not in LOCAL_BLOCKCHAIN_ENVIRONMENTS:
        pytest.skip()

    simple_collectible = deploy_and_create_simple()

    assert simple_collectible.ownerOf(0) == get_account()
    assert simple_collectible.tokenCounter() == 1
    assert simple_collectible.balanceOf(get_account()) == 1
