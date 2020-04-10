import time
import requests as rq

API_URL = "http://www.walletexplorer.com/api/1/"


def lookup_address(address, s="address"):
    # Looks up address' wallet and all transactions with that wallet using that address
    # So not all the wallet's transactions, for that set s parameter to wallet and give the wallet's address
    m_from = 100
    j_obj = rq.get(f"{API_URL}{s}?{s}={address}&from=0&count=100&caller=blockchain_project").json()
    if not j_obj['found']:
        time.sleep(1)
        return None
    while j_obj['txs_count'] > m_from:
        time.sleep(1)
        j_obj['txs'].append(rq.get(
            f"{API_URL}{s}?{s}={address}&from={m_from}&count=100&caller=blockchain_project").json()[
                                'txs'])
        m_from += 100
    return j_obj


def get_wallet_address(address):
    # Gets the wallet address from the given Bitcoin address
    j_obj = rq.get(f"{API_URL}address-lookup?address={address}&caller=blockchain_project").json()
    time.sleep(1)
    return j_obj if j_obj['found'] else None


def get_label(address):
    j_obj = get_wallet_address(address)
    return None if j_obj is None else j_obj.get('label', None)


def main():
    # Gets transactions of address
    # j_obj = lookup_address(address="1NzFEQWtzpWjR9GfBHJuNMNFhrSZsDmeXm")
    # print(j_obj if j_obj is not None else "Address not found in walletexplorer")
    #
    # # Gets transactions of address' wallet
    # j_obj = get_wallet_address("12cgpFdJViXbwHbhrA3TuW1EGnL25Zqc3P")
    # if j_obj is not None:
    #     # Print possible exchange
    #     if 'label' in j_obj.keys():
    #         print(j_obj['label'])
    #     # Get all transactions of wallet
    #     print(lookup_address(address=j_obj['address'], s="wallet"))
    # else:
    #     print("Address not found in walletexplorer")

    label = get_label('15TK6tdZyDNbm4sUJCagjoes2fE6LygBfK')
    print(label)

if __name__ == '__main__':
    main()
