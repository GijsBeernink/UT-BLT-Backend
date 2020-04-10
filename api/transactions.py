import json
import os
import time

import requests

import api
from local import BLOCKCHAIN_API_TOKEN

# The blockchain API endpoint. Use it with .format(address).
BLOCKCHAIN_API = 'https://blockchain.info/rawaddr/{}?apikey=' + BLOCKCHAIN_API_TOKEN

# Location of the result of the API call. Store these to make less API calls and get blocked less
# fast.
FILE_STRUCTURE_API_CALL = '../databases/result_for_address_{}.txt'
# Store results with specific depth.
FILE_STRUCTURE_RESULT_WITH_DEPTH = '../databases/results/address_{}_with_depth_{}.txt'


def get_neighbours(address):
    """
    Get the neighbours of an address. Neighbours are nodes that have some connection to this
    address.
    :param address: Address to get the neighbouring nodes for.
    :return: Dictionary with address:neighbours dictionary. Where neighbours is an array
    of two dictionaries (one for in and one for outgoing transactions).
    """
    if not os.path.isfile(FILE_STRUCTURE_API_CALL.format(address)):
        request_address_data(address)

    with open(FILE_STRUCTURE_API_CALL.format(address)) as f:
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

    return {address: result}


def request_address_data(address, use_timeout=True):
    """
    Retrieve address data from BLOCKCHAIN_API.
    :param use_timeout: If True, wait for 5 seconds before making api call. Used to not get
    blocked by api endpoint.
    :param address: the address to get transaction data for.
    """

    if use_timeout:
        time.sleep(5)
    print("Requesting data for {}...".format(address), end=' ')
    response = requests.get(BLOCKCHAIN_API.format(address))
    if not response.ok:
        if response.status_code == 429:
            print("Too many requests to this API endpoint!\n")
            raise Exception("Blocked by the API. You've probably send too much API requests. Did "
                            "you use a timeout of 5 seconds?")
        raise Exception("Could not get data from API endpoint. Some error occurred")
    data = response.text
    with open(FILE_STRUCTURE_API_CALL.format(address), 'w+') as f:
        f.seek(0)
        f.truncate()
        json.dump(data.replace('\n', ''), f)
        print("Done.")


def get_neighbours_with_depth(address, depth=1):
    """
    Start of recursive function to get neighbours of the current address with a certain depth.
    :param address: The address from which to get all neighbours
    :param depth: The depth to which to find neighbours
    :return: Dictionary with the resulting nodes until specified depth.
    """
    if depth <= 0:
        return address
    neighbours = get_neighbours(address)
    if neighbours[address] == 'No transactions':
        print("No transactions for this address.")
        return neighbours
    return {'main_node': address, 'data': recursive_get_neighbours_with_depth(address, depth)}


def recursive_get_neighbours_with_depth(address, depth):
    """
    Recursive (util) part to get nodes with a specified depth.
    :param address: The current address to get the nodes for until a specified depth
    :param depth: How many hops to other nodes are made.
    :return: Resulting dictionary of addresses and its neighbours.
    """
    neighbours = get_neighbours(address)
    result = dict()
    if depth == 1:
        return neighbours

    for tx_s in dict(neighbours[address]).keys():
        current_tx = neighbours[address].get(tx_s)
        current_in = current_tx.get('in')
        current_out = current_tx.get('out')

        for addr_in in current_in:
            if addr_in is None:
                print("Found None, this is probably a Bech32 address.")
                result[addr_in] = 'Probably Some Bech32 Address'
            if addr_in not in result.keys():
                result[addr_in] = recursive_get_neighbours_with_depth(addr_in, depth - 1)
        for addr_out in current_out:
            if addr_out is None:
                print("Found None, this is probably a Bech32 address.")
                result[addr_out] = 'Probably Some Bech32 Address'
            if addr_out not in result.keys() and addr_out is not None:
                result[addr_out] = recursive_get_neighbours_with_depth(addr_out, depth - 1)
    return result


def get_abuse_addresses():
    """
    Get abuse addresses from the abuse database file.
    :return: All unique addresses in the database.
    """
    db = api.open_abuse_database()
    addresses = []
    for address in db.address.unique():
        addresses.append(address)
    return addresses


def get_interesting_abuse_addresses(transactions=2):
    """
    Find addresses from the abuse database that have at least a specified number amount of
    transactions.
    :return:
    """
    all_addresses = get_abuse_addresses()
    interesting = []
    for address in all_addresses:
        neighbours = get_neighbours(address)[address]
        if neighbours == 'No transactions':
            continue
        if len(neighbours.keys()) <= transactions:
            continue
        interesting.append(address)
        print(interesting)

    return interesting


def save_to_file(address, depth, resulting_neighbours_dict):
    """
    Save the resulting dictionary with all neighbours with a specified depth. If the file already
    exists it will discard all contents of this file.
    :param address: The address that is the starting point
    :param depth: Depth of how far up and down into the transactions to seek.
    :param resulting_neighbours_dict: the result of the get_neighbours_with_depth function.
    :return:
    """
    with open(FILE_STRUCTURE_RESULT_WITH_DEPTH.format(address, depth), 'w+') as f:
        f.seek(0)
        f.truncate()
        json.dump(resulting_neighbours_dict, f)
        print("Done.")


if __name__ == '__main__':
    # Address to search:
    addr = '1PGd8HMWW8w3h2Ftsp8rddM8Xg1sBAHUWk'
    # Depth to search this address:
    search_depth = 2

    res = get_neighbours_with_depth(address=addr, depth=search_depth)
    save_to_file(address=addr, depth=search_depth, resulting_neighbours_dict=res)
