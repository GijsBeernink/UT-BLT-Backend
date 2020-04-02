import ast
import json
from transactions import get_neighbours_with_depth, save_to_file

WRITE_FILE_STRUCTURE = '../converted_database/converted_{}.json'
READ_FILE_STRUCTURE = '../databases/results/address_{}_with_depth_{}.txt'


def getRelativeWidth(nodes):
    maxWidth = 0

    for n in nodes:
        print("sum")
        print(sum(n['in'].values()))
        print(sum(n['out'].values()))
        maxWidth = max(maxWidth, max(max(n['in'].values()), max(n['out'].values())))
    print(maxWidth)
    return maxWidth / 20


def getWidth(value, maxValue):
    result = 1
    if value is not None:
        result = value / maxValue
    print(result)
    return result


def convert(n):
    j_obj = {"nodes": [], "edges": []}
    main_node = list(n.keys())[0]
    j_obj['nodes'].append(
        {"id": main_node, "label": main_node[:10] + "..", "title": main_node, "group": 1,
         "color": {"background": "rgb(233,9,26)", "border": "rgb(233,9,26)"}}
    )
    possible_mal = set()

    def color_nodes(in_dict, out_dict, color_in, color_out, is_in=False):
        first = True
        for i in in_dict:
            if i not in [jo['id'] for jo in j_obj['nodes']]:
                j_obj['nodes'].append(
                    {"id": i, "label": i[:10] + "..", "title": i, "group": 1,
                     "color": {"background": color_in, "border": color_in}}
                )
            for j in out_dict:
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
        in_dict = arr.get('in')
        out_dict = arr.get('out')
        if main_node in out_dict:
            color_nodes(in_dict, out_dict, "rgb(26,19,233)", "rgb(159,159,163)")
        elif main_node in in_dict:
            color_nodes(in_dict, out_dict, "rgb(159,159,163)", "rgb(159,159,163)", True)
        for i in possible_mal:
            if i in in_dict:
                color_nodes(in_dict, out_dict, "rgb(159,159,163)", "rgb(159,159,163)", True)
                break

    def find_trans(arr):
        rec_k = list(arr.keys())
        if str(rec_k[0]) == '1':
            for key in rec_k:
                if key != 'null':
                    add_trans(arr.get(key))
        else:
            for key in rec_k:
                if key != 'null':
                    find_trans(arr.get(key))

    find_trans(n)
    return j_obj


def get_first_address(node):
    return list(node.keys())[0]


def main():
    address = '14ee2y99gEXeQXJ7RxrPv4G6ELL3A6gfFq'
    depth = 2
    save_to_file(address=address, depth=depth, resulting_neighbours_dict=get_neighbours_with_depth(address=address, depth=depth))
    with open(READ_FILE_STRUCTURE.format(address, depth), 'r') as f:
        s = f.read()
        node = ast.literal_eval(s)
    with open(WRITE_FILE_STRUCTURE.format(address), 'w') as f:
        f.seek(0)
        f.truncate()
        json.dump(convert(node), f)
        print("Done.")


if __name__ == '__main__':
    main()
