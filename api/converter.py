import json


def convert(nodes):
    j_obj = {"nodes": [], "edges": []}
    for n in nodes:
        k = n['key']
        if k not in j_obj['nodes']:
            j_obj['nodes'].append(
                {"id": k, "label": k, "color": {"background": "rgb(233,9,26)", "border": "rgb(233,9,26)"}}
            )
        for i in n['in']:
            if i not in j_obj['nodes']:
                j_obj['nodes'].append(
                    {"id": i, "label": i, "color": {"background": "rgb(26,19,233)", "border": "rgb(26,19,233)"}}
                )
            j_obj['edges'].append(
                {"from": i, "to": k, "value": str(n['in'].get(i)), "color": "rgb(233,150,122)", "arrows": "to"}
            )
        for o in n['out']:
            if o not in j_obj['nodes']:
                j_obj['nodes'].append(
                    {"id": o, "label": o, "color": {"background": "rgb(159,159,163)", "border": "rgb(159,159,163)"}}
                )
            j_obj['edges'].append(
                {"from": k, "to": o, "value": str(n['in'].get(o)), "color": "rgb(159,159,163)", "arrows": "to"}
            )
    return json.dumps(j_obj)


def main():
    node = {
        'key': '14jqiHgifMDyr12GQJqKJZHRb79ebp1209',
        'in':
            {
                '18SGN6S2KpTeu2tUhCijzLLXWGSQ6yV8Qv': 4941000000,
                '1DabMAaRa9Gnf4y214k1nKPhCx7zmHcRZa': 1144504400,
                '1KcHHBzLDULprCVVmN6Truhe7euEuAN4WH': 5000100000,
                '1G67HRELGsvemJrNgHYeLnjLH2MemjiEgw': 2566124623,
                '12DyiWj7diBRFSU7CZjtxKrnYHyJrAv8kN': 4941000000,
                '14NfNEgGQiLwkMQUWw5hwYJELtDvdpDtxa': 4752000000,
                '17eqngFA38rVGjCn2z8HowTsSTXsuo56T3': 3668900000,
                '1GcJcSm67wS19fgaXCFeVZU7kQCfnV77s5': 5000000000,
                '1B5AUoAyPpQRBYgcwWXMnqfqCy859jAX7X': 5000000000,
                '1DjqiHgifMDyr1EGQJqHRZHRb79ebp85hz': 10002050000,
                '1DuDhtjKNE4faN29Ymh2autCLGQzrXd4Wq': 2565243300,
                '1nXDysGMxab8TzMTpUZnGtyEkDWTd5iBr': 2117135100,
                '14G3zw28jHfFDFDGxzc7zH9VFTK9jg1EcD': 3453161200,
                '1GwE4hFy4vhMoLp6F9ZngoGSzQcEFWAeGq': 3413342300,
                '1KmxueGS1anasLESEbTXf4o7xawAU4otzp': 3390900000,
                '1N7FwhaedvZQxfTP41dAAJ5LEq8E3c5MMe': 50547003,
                '1PiwpfdV6bckqiqdp2XkmephuiixWS2KEw': 4941000000,
                '17SXiCrirPoLtS9SaX1ALXHSBMfMTm4Rh4': 4624000000,
                '1At6AMsCyyeepMNAPbEB8QnipNKiRnEu5b': 3806000000,
                '184CQ7agrApMYpnKTzWnsMjV9Wx3raHw7S': 2000000000,
                '12uK1qNrFAM42yyz8YizXGnmnSXkHptfWq': 4941000000,
                '1PapcumPDGgKVSgxyRX2GEVym2mAWA5cj4': 3463900000,
                '1Af7jQYb7dnEDdXvWCM7bgQEW8EmqhFe4X': 1065447,
                '1HnmAMXWnZ3CUeQXwQLJYuoST3MQqXVsZY': 3578000000,
                '1ATf4wTRDDM8R4gafdNGKoQCAGc2DXJtJr': 1067900,
                '1NTshZ6dm7XFUZqomwPvfVZgvgpvMVKHZY': 2221352000,
                '14WzoLYsT4VrABHJ4EANBUkW8yE767KNk5': 5000000000,
                '17DDRumKvmcShkFt4kFMpzpwDjEEiN5ZpJ': 4985000000,
                '17H3PiatM6H1WFgqUcPmqPeJ9DckAQTuJ8': 3864900000
            },
        'out':
            {
                '14zVvBYpyw32fL2xZNMxshbKVKVzR9HEB8': 1015615,
                '12mS3W2yr6TSFhf5juS9ikR5B1BFrrQ9sH': 500000000000
            }
    }
    nodes = [node]
    print(convert(nodes))


if __name__ == '__main__':
    main()
