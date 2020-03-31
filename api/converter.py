import json
import ast

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
# <<<<<<< HEAD
#     for n in nodes:
#         k = n['key']
#         if k not in j_obj['nodes']:
#             j_obj['nodes'].append(
#                 {"id": k, "label": k[:10] + "..", "title": k,  "color": {"background": "rgb(233,9,26)", "border": "rgb(233,9,26)"}}
#             )
#         for i in n['in']:
#             if i not in j_obj['nodes']:
#                 j_obj['nodes'].append(
#                     {"id": i, "label": i[:10] + "..", "title": i,"group": 1, "color": {"background": "rgb(26,19,233)", "border": "rgb(26,19,233)"}}
#                 )
#             j_obj['edges'].append(
#                 {"from": i, "to": k, "title": str(format(n['in'].get(i), ',d')), "width": (n['in'].get(i) / (sum(n['in'].values())/10)) + 0.5, "color": "rgb(233,150,122)", "arrows": "to"}
#             )
#         for o in n['out']:
#             if o not in j_obj['nodes']:
#                 j_obj['nodes'].append(
#                     {"id": o, "label": o[:10] + "..", "title": o, "group": 2, "color": {"background": "rgb(159,159,163)", "border": "rgb(159,159,163)"}}
#                 )
#             print(o)
#             j_obj['edges'].append(
#                 {"from": k, "to": o, "title": str(format(n['out'].get(o), ',d')), "width": (n['out'].get(o)/ (sum(n['out'].values())/10)) + 0.5, "color": "rgb(159,159,163)", "arrows": "to"}
#             )
#     return json.dumps(j_obj)
# =======

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
                    {"from": i, "to": j, "title": str(format(out_dict.get(j), ',d')), "width": (out_dict.get(j)/ (sum(out_dict.values())/10)) + 0.5, "color.color": "rgb(233,150,122)", "color.highlight": "rgb(10,9,233)", "arrows": "to"}
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
        if rec_k[0] == 1:
            for key in rec_k:
                add_trans(arr.get(key))
        else:
            for key in rec_k:
                find_trans(arr.get(key))

    find_trans(n)
    return j_obj
        # if k not in [j['id'] for j in j_obj['nodes']]:
        #     j_obj['nodes'].append(
        #         {"id": k, "label": k, "color": {"background": "rgb(233,9,26)", "border": "rgb(233,9,26)"}}
        #     )
        # for i in n['in'][0]:
        #     if i not in [j['id'] for j in j_obj['nodes']]:
        #         j_obj['nodes'].append(
        #             {"id": i, "label": i, "color": {"background": "rgb(26,19,233)", "border": "rgb(26,19,233)"}}
        #         )
        #     j_obj['edges'].append(
        #         {"from": i, "to": k, "value": str(n['in'][0].get(i)), "color": "rgb(233,150,122)", "arrows": "to"}
        #     )
        # for o in n['out'][0]:
        #     if o not in [j['id'] for j in j_obj['nodes']]:
        #         j_obj['nodes'].append(
        #             {"id": o, "label": o, "color": {"background": "rgb(159,159,163)", "border": "rgb(159,159,163)"}}
        #         )
        #     j_obj['edges'].append(
        #         {"from": k, "to": o, "value": str(n['in'][0].get(o)), "color": "rgb(159,159,163)", "arrows": "to"}
        #     )


# def convert(nodes):
#     #maxWidth = getRelativeWidth(nodes)
#     j_obj = {"nodes": [], "edges": []}
#
#     def recursive_fun(arr):
#         for a in arr:
#             rec_k = list(a.keys())[0]
#             if rec_k not in [j['id'] for j in j_obj['nodes']]:
#                 j_obj['nodes'].append(
#                     {"id": rec_k, "label": rec_k, "color": {"background": "rgb(233,9,26)", "border": "rgb(233,9,26)"}}
#                 )
#             rec_arr = a.get(rec_k)
#             for t in rec_arr:
#                 if type(rec_arr.get(t)['in']) is dict:
#                     rec_t = rec_arr.get(t)['in']
#                 else:
#                     rec_t = rec_arr.get(t)['in'][0]
#                 for rec_i in rec_t:
#                     if rec_i not in [j['id'] for j in j_obj['nodes']]:
#                         j_obj['nodes'].append(
#                             {"id": rec_i, "label": rec_i, "color": {"background": "rgb(26,19,233)", "border": "rgb(26,19,233)"}}
#                         )
#                     j_obj['edges'].append(
#                         {"from": rec_i, "to": rec_k, "value": str(rec_t.get(rec_i)), "color": "rgb(233,150,122)",
#                          "arrows": "to"}
#                     )
#                 if type(rec_arr.get(t)['out']) is dict:
#                     rec_t = rec_arr.get(t)['out']
#                 else:
#                     rec_t = rec_arr.get(t)['out'][0]
#                 for rec_o in rec_t:
#                     if rec_o not in [j['id'] for j in j_obj['nodes']]:
#                         j_obj['nodes'].append(
#                             {"id": rec_o, "label": rec_o, "color": {"background": "rgb(159,159,163)", "border": "rgb(159,159,163)"}}
#                         )
#                     j_obj['edges'].append(
#                         {"from": rec_k, "to": rec_o, "value": str(rec_t.get(rec_o)), "color": "rgb(159,159,163)",
#                          "arrows": "to"}
#                     )
#                 if type(rec_arr.get(t)['in']) is list and rec_arr.get(t)['in'][1:]:
#                     recursive_fun(rec_arr.get(t)['in'][1:])
#                 elif type(rec_arr.get(t)['out']) is list and rec_arr.get(t)['out'][1:]:
#                     recursive_fun(rec_arr.get(t)['out'][1:])
#         return
#
#     for n in nodes:
#         k = n['address']
#         if k not in [j['id'] for j in j_obj['nodes']]:
#             j_obj['nodes'].append(
#                 {"id": k, "label": k, "color": {"background": "rgb(233,9,26)", "border": "rgb(233,9,26)"}}
#             )
#         for i in n['in'][0]:
#             if i not in [j['id'] for j in j_obj['nodes']]:
#                 j_obj['nodes'].append(
#                     {"id": i, "label": i, "color": {"background": "rgb(26,19,233)", "border": "rgb(26,19,233)"}}
#                 )
#             j_obj['edges'].append(
#                 {"from": i, "to": k, "value": str(n['in'][0].get(i)), "color": "rgb(233,150,122)", "arrows": "to"}
#             )
#         for o in n['out'][0]:
#             if o not in [j['id'] for j in j_obj['nodes']]:
#                 j_obj['nodes'].append(
#                     {"id": o, "label": o, "color": {"background": "rgb(159,159,163)", "border": "rgb(159,159,163)"}}
#                 )
#             j_obj['edges'].append(
#                 {"from": k, "to": o, "value": str(n['in'][0].get(o)), "color": "rgb(159,159,163)", "arrows": "to"}
#             )
#         recursive_fun(n['in'][1:])
#         recursive_fun(n['out'][1:])
#     return json.dumps(j_obj)


#  "value": str(n['in'].get(i)),
# "value": str(n['in'].get(o)),


def get_first_address(node):
    return list(node.keys())[0]


def main():
    addr = '115p7UMMngoj1pMvkpHijcRdfJNXj6LrLn'
    depth = 3
    with open(READ_FILE_STRUCTURE.format(addr, depth), 'r') as f:
        s = f.read()
        node = ast.literal_eval(s)
    with open(WRITE_FILE_STRUCTURE.format(addr), 'w') as f:
        f.seek(0)
        f.truncate()
        json.dump(convert(node), f)
        print("Done.")

if __name__ == '__main__':
    main()
