import json

FILE_STRUCTURE = '../converted_database/added_positions.json'

with open('../converted_database/converted_address.json', 'r') as f:
    network_dict = json.load(f)

with open('../converted_database/positions.json', 'r') as f:
    position_dict = json.load(f)

j_obj = {"nodes": [], "edges": []}
count = 0

for x in network_dict['nodes']:
    if x['id'] in position_dict:
        j_obj['nodes'].append(
            {"id": x['id'], "label": x['label'], "title": x['title'], "group": x['group'],
             "color": x['color'], "x": position_dict[x['id']]['x'], "y": position_dict[x['id']]['y']}
        )
    else:
        count += 1
        print(x)
print(count)
print(len(network_dict['nodes']))
print(len(position_dict))
j_obj['edges'] = network_dict['edges']

with open(FILE_STRUCTURE, 'w') as f:
    f.seek(0)
    f.truncate()
    json.dump(j_obj, f)
    print("Done.")
