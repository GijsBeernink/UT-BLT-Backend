import requests
import pprint
import json
import os
import api
import time

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
    number_of_txs = int(data_dict.get('n_tx'))
    # print(number_of_txs)
    if number_of_txs == 0:
        return {address: 'No transactions'}
    txs = data_dict.get('txs')
    # print(txs)
    tx_counter = 0
    result = dict()
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

    return {address: result}


def request_address_data(address, use_timeout=True):
    """
    Retrieve address data from BLOCKCHAIN_API.
    :param use_timeout: If True, wait for ten seconds before making api call. Used to not get
    blocked by api endpoint.
    :param address: the address to get transaction data for.
    """

    if use_timeout:
        time.sleep(10)
    print("Requesting data for {}...".format(address), end=' ')
    response = requests.get(BLOCKCHAIN_API + address)
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
    """
    Get neighbours of node with specific depth.
    :param address: address to find neighbours for
    :param depth: Optional, find neighbours until some specific depth.
    :return: neighbours of given address.
    """
    neighbours = get_neighbours(address)[address]
    if neighbours == 'No transactions':
        return {address: neighbours}
    # print(neighbours)
    for key in neighbours.keys():
        current_transaction = neighbours.get(key)
        in_neighbours = current_transaction.get('in')
        out_neighbours = current_transaction.get('out')

        in_result = []
        in_neighbours_at_current_depth = []
        in_neighbours_at_previous_depth = in_neighbours.keys()
        in_result.append(in_neighbours)
        for i in range(1, depth):
            for in_neighbour in in_neighbours_at_previous_depth:
                neighbours_of_in = get_neighbours(in_neighbour)
                in_result.append(neighbours_of_in)
                in_neighbours_at_current_depth.append(neighbours_of_in.keys())
            in_neighbours_at_previous_depth = in_neighbours_at_current_depth
            in_neighbours_at_current_depth = []

        out_result = []
        out_neighbours_at_current_depth = []
        out_neighbours_at_previous_depth = out_neighbours.keys()
        out_result.append(out_neighbours)
        for i in range(1, depth):
            for out_neighbour in out_neighbours_at_previous_depth:
                neighbours_of_out = get_neighbours(out_neighbour)
                out_result.append(neighbours_of_out)
                out_neighbours_at_current_depth.append(neighbours_of_out.keys())
            out_neighbours_at_previous_depth = out_neighbours_at_current_depth
            out_neighbours_at_current_depth = []

    return {'address': address, 'in': in_result, 'out': out_result}


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
    # abuse_addresses = get_abuse_addresses()
    res = get_neighbours_with_depth('1CbhowVaSNvdqHo9jpFZjc1UyYW4mnEc4R', depth=2)
    print(res)
    # print(neighbours)
    # some_abuse_address = abuse_addresses[6]
    # for address in abuse_addresses:
    #     print(get_neighbours_with_depth(address, 1))
    #
    # # print("\n\n")
    # print(result)
