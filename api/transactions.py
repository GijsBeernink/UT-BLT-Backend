import requests
import pprint
import json
import os
import api

BLOCKCHAIN_API = 'https://blockchain.info/rawaddr/'
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

    neighbours = dict()
    neighbours_in = dict()
    neighbours_out = dict()

    with open(FILE_STRUCTURE.format(address)) as f:
        data = json.load(f)
        data_dict = json.loads(data)

    txs = data_dict.get('txs')[0]
    txs_inputs = txs.get('inputs')
    for tx_in in txs_inputs:
        prev_out = tx_in.get('prev_out')
        address = prev_out.get('addr')
        value = prev_out.get('value')
        neighbours_in[address] = value

    txs_outputs = txs.get('out')
    for tx_out in txs_outputs:
        address = tx_out.get('addr')
        value = tx_out.get('value')
        neighbours_out[address] = value

    neighbours['in'] = neighbours_in
    neighbours['out'] = neighbours_out

    return {address: neighbours}


def request_address_data(address):
    """
    Retrieve address data from BLOCKCHAIN_API.
    :param address: the address to get transaction data for.
    :return: False if api call did not succeed. True if successfully written to disk.
    """
    response = requests.get(BLOCKCHAIN_API + address)
    if not response.ok:
        return False
    data = response.text
    # pprint.pprint(data)
    with open(FILE_STRUCTURE.format(address), 'w+') as f:
        f.seek(0)
        f.truncate()
        json.dump(data.replace('\n', ''), f)
        return True


def get_neighbours_with_depth(address, depth=1):
    """
    Get neighbours of node with specific depth.
    :param address: address to find neighbours for
    :param depth: Optional, find neighbours until some specific depth.
    :return: neighbours of given address.
    """
    neighbours = get_neighbours(address)

    in_neighbours = neighbours.get('in')
    out_neighbours = neighbours.get('out')

    for in_neighbour in in_neighbours.keys():
        neighbours_of_in = get_neighbours(in_neighbour)


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


if __name__ == '__main__':
    # result = request_address_data('184CQ7agrApMYpnKTzWnsMjV9Wx3raHw7S', demo=False)
    # pprint.pprint(result)
    abuse_addresses = get_abuse_addresses()
    # get_neighbours_with_depth('184CQ7agrApMYpnKTzWnsMjV9Wx3raHw7S', depth=1)
    print(len(abuse_addresses))
    for address in abuse_addresses:

    # print("\n\n")
    # print(result)
