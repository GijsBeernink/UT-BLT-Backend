import requests
from local import *

BLOCK_EXPLORER = "https://blockexplorer.com/api"
BLOCKCHAIN_API = "https://blockchain.info/"
TEST_ADDRESS = "3Lo4nDzH7Bi572T7t8pQGU2Ax9jVymHeC6"


def search_from_address(address, limit=50):
    print(f"{BLOCKCHAIN_API}rawaddr/{address}")
    trans = requests.get(f"{BLOCKCHAIN_API}rawaddr/{address}?limit={limit}")

    print(len(trans.json()['txs']))

    for tx in trans.json()['txs']:
        print(tx)


def get_abuse():
    pass


def main():
    search_from_address(TEST_ADDRESS)


if __name__ == "__main__":
    main()
