import requests
from local import *

BLOCK_EXPLORER = "https://blockexplorer.com/api"
TEST_ADDRESS = "3Lo4nDzH7Bi572T7t8pQGU2Ax9jVymHeC6"


def search_from_address(address):
    print(f"{BLOCK_EXPLORER}/txs/?address={address}")
    trans = requests.get(f"{BLOCK_EXPLORER}/txs/?address={address}")

    print(trans.content)


def get_abuse():
    pass


def main():
    search_from_address(TEST_ADDRESS)


if __name__ == "__main__":
    main()
