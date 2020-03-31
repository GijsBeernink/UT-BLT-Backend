import requests
import pprint
import json
import os
import api
import time
from local import BLOCKCHAIN_API_TOKEN

BLOCKCHAIN_API = 'https://blockchain.info/rawaddr/{}?apikey=' + BLOCKCHAIN_API_TOKEN
FILE_STRUCTURE = '../databases/result_for_address_{}.txt'


def get_neighbours(address):
    """
    Get the neighbours of an address. Neighbours are nodes that have some connection to address.
    :param address: Address to get the neighbouring nodes for.
    :return: Dictionary with address:neighbours dictionary. Where neighbours is an array
    of two dictionaries (one for in and one for outgoing transactions).
    """
    if not os.path.isfile(FILE_STRUCTURE.format(address)):
        request_address_data(address)

    with open(FILE_STRUCTURE.format(address)) as f:
        data = json.load(f)
        data_dict = json.loads(data)
    number_of_txs = int(data_dict.get('n_tx'))
    # print(number_of_txs)
    if number_of_txs == 0:
        return {address: 'No transactions'}
    txs = data_dict.get('txs')
    # print(txs)
    tx_counter = 0
    result = dict()
    neighbours = {}
    neighbours_in = {}
    neighbours_out = {}

    for tx in txs:
        tx_inputs = tx.get('inputs')
        for tx_in in tx_inputs:
            prev_out = tx_in.get('prev_out')
            addr = prev_out.get('addr')
            value = prev_out.get('value')
            neighbours_in[addr] = value

        tx_outputs = tx.get('out')
        for tx_out in tx_outputs:
            addr = tx_out.get('addr')
            value = tx_out.get('value')
            neighbours_out[addr] = value

        neighbours['in'] = neighbours_in
        neighbours['out'] = neighbours_out

        tx_counter += 1
        result[tx_counter] = neighbours

        neighbours = {}
        neighbours_in = {}
        neighbours_out = {}

    # print("Result of get_neighbours:\n")
    return {address: result}


def request_address_data(address, use_timeout=True):
    """
    Retrieve address data from BLOCKCHAIN_API.
    :param use_timeout: If True, wait for ten seconds before making api call. Used to not get
    blocked by api endpoint.
    :param address: the address to get transaction data for.
    """

    if use_timeout:
        time.sleep(5)
    print("Requesting data for {}...".format(address), end=' ')
    response = requests.get(BLOCKCHAIN_API.format(address))
    if not response.ok:
        raise Exception("Could not get data from API endpoint.")
    data = response.text
    # pprint.pprint(data)
    with open(FILE_STRUCTURE.format(address), 'w+') as f:
        f.seek(0)
        f.truncate()
        json.dump(data.replace('\n', ''), f)
        print("Done.")


def get_neighbours_with_depth(address, depth=1):
    if depth <= 0:
        return address
    return recursive_get_neighbours_with_depth(address, depth)


def recursive_get_neighbours_with_depth(address, depth):
    neighbours = get_neighbours(address)
    result = dict()
    if depth == 1:
        return neighbours

    for tx_s in dict(neighbours[address]).keys():
        current_tx = neighbours[address].get(tx_s)
        current_in = current_tx.get('in')
        current_out = current_tx.get('out')

        for addr_in in current_in:
            if addr_in not in result.keys():
                result[addr_in] = recursive_get_neighbours_with_depth(addr_in, depth - 1)
        for addr_out in current_out:
            if addr_out not in result.keys():
                result[addr_out] = recursive_get_neighbours_with_depth(addr_out, depth - 1)
    return result


def get_abuse_addresses():
    """
    Get abuse addresses from the abuse database file.
    :return: All addresses in the file.
    """
    db = api.open_abuse_database()
    addresses = []
    # print(db.address)
    for address in db.address.unique():
        # print(address)
        addresses.append(address)
    return addresses


def get_interesting_abuse_addresses():
    all_addresses = get_abuse_addresses()
    interesting = []
    for address in all_addresses:
        neighbours = get_neighbours(address)[address]
        if neighbours == 'No transactions':
            continue
        if len(neighbours.keys()) <= 2:
            continue
        interesting.append(address)
        print(interesting)

    return interesting


if __name__ == '__main__':
    # result = request_address_data('184CQ7agrApMYpnKTzWnsMjV9Wx3raHw7S', demo=False)
    # pprint.pprint(result)
    # abuse_addresses = get_abuse_addresses()

    # res = get_neighbours('1JRBisFrtAsY4E49419PSW6hLePH6jUdGi')
    # print(res)
    # res = get_neighbours_with_depth('1JRBisFrtAsY4E49419PSW6hLePH6jUdGi', depth=3)
    # print(res)
    res = get_neighbours_with_depth('1JRBisFrtAsY4E49419PSW6hLePH6jUdGi', depth=2)
    print(res)
    # print(neighbours)
    # some_abuse_address = abuse_addresses[6]
    # for address in abuse_addresses:
    #     print(get_neighbours_with_depth(address, 1))
    #
    # # print("\n\n")
    # print(result)
    # print(get_interesting_abuse_addresses())
