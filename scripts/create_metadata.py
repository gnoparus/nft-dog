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


def upload_to_ipfs(filepath):
    with Path(filepath).open("rb") as fp:
        image_binary = fp.read()
        ipfs_url = "http://127.0.0.1:5001"
        endpoint = "/api/v0/add"
        response = requests.post(ipfs_url + endpoint, files={"file": image_binary})
        ipfs_hash = response.json()["Hash"]
        file_name = filepath.split("/")[-1:][0]
        image_uri = f"https://ipfs.io/ipfs/{ipfs_hash}?filename={file_name}"
        print(f"image_uri = {image_uri}")
        return image_uri


def create_metadata():
    advanced_collectible = AdvancedCollectible[-1]
    number_of_advanced_collectibles = advanced_collectible.tokenCounter()
    print(f"You've created {number_of_advanced_collectibles} collectible(s)")

    for token_id in range(number_of_advanced_collectibles):
        breed = get_breed(advanced_collectible.tokenIdToBreed(token_id))
        metadata_file_name = (
            f"./metadata/{network.show_active()}/{token_id}-{breed}.json"
        )
        print(f"metada_file_name = {metadata_file_name}")

        collectible_metadata = metadata_template
        if Path(metadata_file_name).exists():
            print(f"{metadata_file_name} is already exists. Delete it to overwrite.")
        else:
            print(f"Creating metadata file {metadata_file_name}")

            collectible_metadata["name"] = breed
            collectible_metadata["description"] = f"Adoreble breed of {breed}"
            collectible_metadata["image_uri"] = ""
            # print(f"collectible_metadata = {collectible_metadata}")
            image_file_name = "./img/" + breed.lower().replace("_", "-") + ".png"
            image_uri = upload_to_ipfs(image_file_name)
            collectible_metadata["image_uri"] = image_uri

            with open(metadata_file_name, "w") as file:
                json.dump(collectible_metadata, file)
            json_uri = upload_to_ipfs(metadata_file_name)

            settoken_tx = advanced_collectible.setTokenURI(
                token_id, json_uri, {"from": get_account()}
            )
            settoken_tx.wait(1)
        print(
            f"You can view your NFT at {OPENSEA_URL}/{advanced_collectible.address}/{token_id}"
        )


def set_token_uri(token_id, json_uri):
    advanced_collectible = AdvancedCollectible[-1]

    settoken_tx = advanced_collectible.setTokenURI(
        token_id, json_uri, {"from": get_account()}
    )

    settoken_tx.wait(1)

    print(
        f"You can view your NFT at {OPENSEA_URL}/{advanced_collectible.address}/{token_id}"
    )


def main():
    create_metadata()

    # token_id = 2
    # json_uri = "https://bualabs.com/dpu-9999333444/2-ST_BERNARD.json"
    # set_token_uri(token_id=token_id, json_uri=json_uri)
