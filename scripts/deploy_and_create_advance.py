from scripts.helpful_scripts import (
    fund_with_link,
    get_account,
    get_contract,
    OPENSEA_URL,
)
from brownie import AdvancedCollectible, network, config


def deploy_and_create_advance():
    account = get_account()
    advanced_collectible = AdvancedCollectible.deploy(
        get_contract("vrf_coordinator"),
        get_contract("link_token"),
        config["networks"][network.show_active()]["key_hash"],
        config["networks"][network.show_active()]["fee"],
        {"from": account},
        publish_source=config["networks"][network.show_active()].get("verify", False),
    )
    print(f"Deployed AdvancedCollectible")
    fund_with_link(advanced_collectible.address, account=account)
    tx = advanced_collectible.createCollectible({"from": account})
    tx.wait(1)
    print(f"Created collectible")
    return advanced_collectible, tx


def main():
    deploy_and_create_advance()
