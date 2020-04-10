import time
import requests as rq

# API endpoint for scraping walletexplorer
API_URL = "http://www.walletexplorer.com/api/1/"
# Caller id used for walletexplorer's personal statistics
CALLER = "blockchain_project"


def lookup_address(address, s="address"):
    """"
    Looks up an address on walletexplorer.com and returns its transactions.
    :param address: Address to look up and return all its transactions.
    :param s: Default is address to look up a normal address on walletexplorer, when set to wallet,
    it means the address given is that of a wallet and it will look up the complete wallet's transactions.
    """
    m_from = 100
    j_obj = rq.get(f"{API_URL}{s}?{s}={address}&from=0&count=100&caller={CALLER}").json()
    if not j_obj['found']:
        time.sleep(1)
        return None
    while j_obj['txs_count'] > m_from:
        time.sleep(1)
        j_obj['txs'].append(rq.get(
            f"{API_URL}{s}?{s}={address}&from={m_from}&count=100&caller={CALLER}").json()['txs'])
        m_from += 100
    return j_obj


def get_wallet_address(address):
    """"
    Looks up an address on walletexplorer
    :param address: address to look up.
    :return: JSON object with transactions and additional information or None if the address is not found.
    """
    j_obj = rq.get(f"{API_URL}address-lookup?address={address}&caller={CALLER}").json()
    time.sleep(1)
    return j_obj if j_obj['found'] else None


def get_label(address):
    """"
    Checks whether the address is registered under a name (exchange)
    :param address: address to look up.
    :return: Name of the address or None if it has none.
    """
    j_obj = get_wallet_address(address)
    return None if j_obj is None else j_obj.get('label', None)


def main():
    # Three different applications of the walletexplorer API

    # Gets transactions of address
    a = "1LYz7EgAF8PU6bSN8GDecnz9Gg814fs81W"
    j_obj = lookup_address(address=a)
    print(j_obj if j_obj is not None else "Address not found in walletexplorer")


    # Gets transactions of address' wallet
    j_obj = get_wallet_address("1LYz7EgAF8PU6bSN8GDecnz9Gg814fs81W")
    if j_obj is not None:
        # Print possible registered name exchange
        if 'label' in j_obj.keys():
            print(j_obj['label'])
        # Get all transactions of wallet
        print(lookup_address(address=j_obj['wallet_id'], s="wallet"))
    else:
        print("Address not found in walletexplorer")


    # Gets the registered name exchange, if one, for the address. Example is of Poloniex.com
    print(get_label('12cgpFdJViXbwHbhrA3TuW1EGnL25Zqc3P'))


if __name__ == '__main__':
    main()
