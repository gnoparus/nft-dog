import os
from pathlib import Path
import requests


def upload_to_pinata(filepath):
    PINATA_BASE_URL = "https://api.pinata.cloud"
    endpoint = "/pinning/pinFileToIPFS"
    file_name = filepath.split("/")[-1:][0]

    headers = {
        "pinata_api_key": os.getenv("PINATA_API_KEY"),
        "pinata_secret_api_key": os.getenv("PINATA_API_SECRET"),
    }

    with Path(filepath).open("rb") as fp:
        image_binary = fp.read()

        response = requests.post(
            PINATA_BASE_URL + endpoint,
            files={"file": (file_name, image_binary)},
            headers=headers,
        )
        print(response.json())
        ipfs_hash = response.json()["IpfsHash"]
        image_uri = f"https://ipfs.io/ipfs/{ipfs_hash}?filename={file_name}"
        print(f"image_url={image_uri}")

    return image_uri


def main():
    upload_to_pinata("./img/pug.png")
