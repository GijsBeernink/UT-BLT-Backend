import requests
import pprint
import json
import os

BLOCKCHAIN_API = 'https://blockchain.info/rawaddr/'
BLOCKCHAIN_API_2 = 'https://chain.api.btc.com/v3/address/'
FILE_STRUCTURE = '../databases/result_for_address_{}.txt'


def get_neighbours(address):
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

    return neighbours


def request_address_data(address):
    response = requests.get(BLOCKCHAIN_API + address)

    data = response.text
    # pprint.pprint(data)
    with open(FILE_STRUCTURE.format(address), 'w+') as f:
        f.seek(0)
        f.truncate()
        json.dump(data.replace('\n', ''), f)


if __name__ == '__main__':
    # result = request_address_data('184CQ7agrApMYpnKTzWnsMjV9Wx3raHw7S', demo=False)
    # pprint.pprint(result)
    neighbour_addresses_and_balances = get_neighbours('184CQ7agrApMYpnKTzWnsMjV9Wx3raHw7S')
    print(neighbour_addresses_and_balances)
    # print("\n\n")
    # print(result)
