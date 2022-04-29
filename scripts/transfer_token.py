from scripts.helpful_scripts import (
    fund_with_link,
    get_account,
    get_contract,
    OPENSEA_URL,
    get_breed,
)
from brownie import AdvancedCollectible, network, config
from web3 import Web3
from metadata import sample_metadata
from pathlib import Path
from metadata.sample_metadata import metadata_template
import requests
import json


def transfer_token(_to_address, token_id):
    advanced_collectible = AdvancedCollectible[-1]

    # approve_tx = advanced_collectible.approve(
    #     _to_address, token_id, {"from": get_account()}
    # )
    # approve_tx.wait(1)

    transfer_tx = advanced_collectible.safeTransferFrom(
        get_account(), _to_address, token_id, {"from": get_account()}
    )

    transfer_tx.wait(1)

    print(
        f"Transfer token {token_id} from {get_account()} to {_to_address} completed. "
    )


def main():
    to_address = "0x7b85f42aC89f40f9199E4537720bf24C69beC250"
    token_id = 3

    transfer_token(to_address, token_id)
