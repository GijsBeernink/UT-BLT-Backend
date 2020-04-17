import ast
import json
from api.transactions import get_neighbours_with_depth, save_to_file
from api.walletexplorer_api import get_label

# Write to json file with naming of address by using .format(address)
# WRITE_FILE_STRUCTURE = '../converted_database/converted_{}.json'
# Write to standard json file
WRITE_FILE_STRUCTURE = '../converted_database/converted_file.json'
# Reading from txt file with naming of address and certain depth by using .format(address, depth)
READ_FILE_STRUCTURE = '../databases/results/address_{}_with_depth_{}.txt'


def get_relative_width(nodes):
    max_width = 0

    for n in nodes:
        print("sum")
        print(sum(n['in'].values()))
        print(sum(n['out'].values()))
        max_width = max(max_width, max(max(n['in'].values()), max(n['out'].values())))
    print(max_width)
    return max_width / 20


def get_width(value, max_value):
    result = 1
    if value is not None:
        result = value / max_value
    print(result)
    return result


def convert(n):
    """"
    Converts all transactions to a usable JSON object.
    :param n: The complete dictionary object with all transactions.
    :return: JSON object.
    """
    j_obj = {"nodes": [], "edges": []}
    main_node = n['main_node']
    j_obj['nodes'].append(
        {"id": main_node, "label": main_node[:10] + "..", "title": main_node, "group": 1,
         "color": {"background": "rgb(233,9,26)", "border": "rgb(233,9,26)"}}
    )
    possible_mal = set()

    def color_nodes(in_dict, out_dict, color_in, color_out, is_in=False):
        """"
        Adds nodes and edges to the main JSON object to return.
        :param in_dict: Dictionary with all addresses used to fund the transaction.
        :param out_dict: Dictionary with all addresses where transactions ends up.
        :param color_in: Color of in-address-nodes.
        :param color_out: Color of out-address-nodes.
        :param is_in: Set to True when malicious node is in in_dict, meaning that other nodes in in_dict can be
        malicious as well. This goes on recursively for these nodes as well.
        """
        first = True
        for i in in_dict:
            if i != 'null':
                if i not in [jo['id'] for jo in j_obj['nodes']]:
                    j_obj['nodes'].append(
                        {"id": i, "label": i[:10] + "..", "title": i, "group": 1,
                         "color": {"background": color_in, "border": color_in}}
                    )
                for j in out_dict:
                    if j != 'null':
                        if is_in:
                            possible_mal.add(j)
                        if first and j not in [jo['id'] for jo in j_obj['nodes']]:
                            j_obj['nodes'].append(
                                {"id": j, "label": j[:10] + "..", "title": j, "group": 2,
                                 "color": {"background": color_out, "border": color_out}}
                            )
                        j_obj['edges'].append(
                            {"from": i, "to": j, "title": str(format(out_dict.get(j), ',d')),
                             "width": (out_dict.get(j) / (sum(out_dict.values()) / 10)) + 0.5,
                             "color.color": "rgb(233,150,122)", "color.highlight": "rgb(10,9,233)", "arrows": "to"}
                        )
                first = False

    def add_trans(arr):
        """"
        Add an transaction's addresses to the JSON object.
        :param arr: The transaction which contains the in addresses and out addresses.
        """
        in_dict = arr.get('in')
        out_dict = arr.get('out')
        # If the malicious node is in out-addresses, the in-addresses are possible victims.
        if main_node in out_dict:
            color_nodes(in_dict, out_dict, "rgb(26,19,233)", "rgb(159,159,163)")
        # If malicious node is in in-addresses, other addresses are colored gray as they are potentially related to
        # the malicious node.
        elif main_node in in_dict:
            color_nodes(in_dict, out_dict, "rgb(159,159,163)", "rgb(159,159,163)", True)
        # If malicious node not in either in or out,
        # check whether the added possible malicious nodes are in the in-addresses
        for i in possible_mal:
            if i in in_dict:
                color_nodes(in_dict, out_dict, "rgb(159,159,163)", "rgb(159,159,163)", True)
                break

    def find_trans(arr, key=None):
        """"
        Recursively add transactions to the JSON object.
        :param arr: All transactions.
        :param key: Address that was used to lookup the transaction.
        """
        rec_k = list(arr.keys())
        # Position in dictionary where transactions are:
        if str(rec_k[0]) == '1':
            # Possible exchange, add/change label of node from address to the exchange name.
            if len(rec_k) >= 50:
                label = get_label(key)
                if label is not None:
                    if key not in [jo['id'] for jo in j_obj['nodes']]:
                        j_obj['nodes'].append(
                            {"id": key, "label": key[:10] + "..", "title": label, "group": 1,
                             "color": {"background": "rgb(102,233,64)", "border": "rgb(102,233,64)"}}
                        )
                    else:
                        for ns in j_obj['nodes']:
                            if ns['id'] == key:
                                ns['title'] = label
                                ns['color']['background'] = "rgb(102,233,64)"
                                ns['color']['border'] = "rgb(102,233,64)"
            # Add all transactions
            for key in rec_k:
                add_trans(arr.get(key))
        # Not position in dictionary where transactions are, go one layer deeper for every key.
        else:
            for key in rec_k:
                if key != 'null':
                    find_trans(arr.get(key), key)

    find_trans(n['data'])
    return j_obj


def start_analysis(address, depth):
    # Save address' transactions to a certain depth in databases/results
    save_to_file(address=address, depth=depth,
                 resulting_neighbours_dict=get_neighbours_with_depth(address=address, depth=depth))

    # Load in result
    with open(READ_FILE_STRUCTURE.format(address, depth), 'r') as f:
        s = f.read()
        node = ast.literal_eval(s)

    # If an address is not found on blockchain.info, then return nothing.
    if 'main_node' not in node.keys():
        return

    # Convert results to JSON file and save it in converted_database
    with open(WRITE_FILE_STRUCTURE, 'w') as f:
        f.seek(0)
        f.truncate()
        json.dump(convert(node), f)
        print("Done.")


if __name__ == '__main__':
    start_analysis('1LYz7EgAF8PU6bSN8GDecnz9Gg814fs81W', 2)
