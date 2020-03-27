import json


def getRelativeWidth(nodes):
    maxWidth = 0

    for n in nodes:
        maxWidth = max(maxWidth, max(max(n['in'].values()), max(n['out'].values())))
    print(maxWidth)
    return maxWidth/20


def getWidth(value, maxValue):
    result = 1
    if value is not None:
        result = value/maxValue
    print(result)
    return result


def convert(nodes):
    maxWidth = getRelativeWidth(nodes)
    j_obj = {"nodes": [], "edges": []}

    def recursive_fun(arr, s="in"):
        for a in arr:
            rec_k = a.keys()[0]
            if rec_k not in j_obj['nodes']:
                j_obj['nodes'].append(
                    {"id": rec_k, "label": rec_k, "color": {"background": "rgb(233,9,26)", "border": "rgb(233,9,26)"}}
                )
            for rec_a in a.get(rec_k):
                rec_a
        return

    for n in nodes:
        k = n['address']
        if k not in j_obj['nodes']:
            j_obj['nodes'].append(
                {"id": k, "label": k, "color": {"background": "rgb(233,9,26)", "border": "rgb(233,9,26)"}}
            )
        for i in n['in'][0]:
            if i not in j_obj['nodes']:
                j_obj['nodes'].append(
                    {"id": i, "label": i, "color": {"background": "rgb(26,19,233)", "border": "rgb(26,19,233)"}}
                )
            j_obj['edges'].append(
                {"from": i, "to": k, "value": str(n['in'][0].get(i)), "color": "rgb(233,150,122)", "arrows": "to"}
            )
        for o in n['out'][0]:
            if o not in j_obj['nodes']:
                j_obj['nodes'].append(
                    {"id": o, "label": o, "color": {"background": "rgb(159,159,163)", "border": "rgb(159,159,163)"}}
                )
            print(o)
            j_obj['edges'].append(
                {"from": k, "to": o, "value": str(n['in'][0].get(o)), "color": "rgb(159,159,163)", "arrows": "to"}
            )
        recursive_fun(n['in'][1:])
        recursive_fun(n['out'][1:], s="out")
    return json.dumps(j_obj)

#  "value": str(n['in'].get(i)),
# "value": str(n['in'].get(o)),

def main():
    node = {
        'address': '1CbhowVaSNvdqHo9jpFZjc1UyYW4mnEc4R',
        'in': [{
            '1JRBisFrtAsY4E49419PSW6hLePH6jUdGi': 39900000,
            '19ZLAYf7h4wW6UMo5usozjUtsazBS3MqyC': 6000000,
            '1KnGS1Dtw54C2v6DfCFXDdmdDHruDhuGHZ': 36237371,
            '1CbhowVaSNvdqHo9jpFZjc1UyYW4mnEc4R': 68990000,
            '1FAqpN9a918kr7K1PMb7gKiFQ7cWPVSDbk': 1734582,
            '1u1emSJcQ1FxkhZVcRncXyJ4vxXdhFgcX': 69990000,
            '112uaJKLqtxcmRHHhQAqNLUq9nXbPbwtSP': 1118510
        }, {
            '1JRBisFrtAsY4E49419PSW6hLePH6jUdGi': {
                1: {
                    'in': {
                        '1JRBisFrtAsY4E49419PSW6hLePH6jUdGi': 39900000,
                        '19ZLAYf7h4wW6UMo5usozjUtsazBS3MqyC': 6000000,
                        '1KnGS1Dtw54C2v6DfCFXDdmdDHruDhuGHZ': 36237371,
                        '1CbhowVaSNvdqHo9jpFZjc1UyYW4mnEc4R': 68990000,
                        '1FAqpN9a918kr7K1PMb7gKiFQ7cWPVSDbk': 1734582,
                        '1gdbvo92kybSKYRXuGrPyhJ3BfKDDcS6b': 40000000,
                        '1BkCY3SRFbYt1bRuGfz6Pk3h7ns9e5fNQD': 2199387
                    },
                    'out': {
                        '131gAMNZdfE3bxYzZ2VpNbixYkYhKukFap': 147000000,
                        '1fUXYsDpdLmDHzZyMRfAgF9zKWNN1xWDF': 4127371,
                        '1FCsvQBBHy8WJfPzV2CjiLSXsz6H756wmZ': 1694582,
                        '1EhCtx8Q5dWG9FXEGRnvbRwqQR5h9cftjr': 100000,
                        '1JRBisFrtAsY4E49419PSW6hLePH6jUdGi': 39900000,
                        '1sX66g9pa3k4Lx9pvK2XX1yYUJaPwL5hW': 2179387
                    }
                },
                2: {
                    'in': {
                        '1JRBisFrtAsY4E49419PSW6hLePH6jUdGi': 39900000,
                        '19ZLAYf7h4wW6UMo5usozjUtsazBS3MqyC': 6000000,
                        '1KnGS1Dtw54C2v6DfCFXDdmdDHruDhuGHZ': 36237371,
                        '1CbhowVaSNvdqHo9jpFZjc1UyYW4mnEc4R': 68990000,
                        '1FAqpN9a918kr7K1PMb7gKiFQ7cWPVSDbk': 1734582,
                        '1gdbvo92kybSKYRXuGrPyhJ3BfKDDcS6b': 40000000,
                        '1BkCY3SRFbYt1bRuGfz6Pk3h7ns9e5fNQD': 2199387
                    },
                    'out': {
                        '131gAMNZdfE3bxYzZ2VpNbixYkYhKukFap': 147000000,
                        '1fUXYsDpdLmDHzZyMRfAgF9zKWNN1xWDF': 4127371,
                        '1FCsvQBBHy8WJfPzV2CjiLSXsz6H756wmZ': 1694582,
                        '1EhCtx8Q5dWG9FXEGRnvbRwqQR5h9cftjr': 100000,
                        '1JRBisFrtAsY4E49419PSW6hLePH6jUdGi': 39900000,
                        '1sX66g9pa3k4Lx9pvK2XX1yYUJaPwL5hW': 2179387
                    }
                }
            }
        }, {
            '19ZLAYf7h4wW6UMo5usozjUtsazBS3MqyC': {
                1: {
                    'in': {
                        '1JRBisFrtAsY4E49419PSW6hLePH6jUdGi': 39900000,
                        '19ZLAYf7h4wW6UMo5usozjUtsazBS3MqyC': 6000000,
                        '1KnGS1Dtw54C2v6DfCFXDdmdDHruDhuGHZ': 36237371,
                        '1CbhowVaSNvdqHo9jpFZjc1UyYW4mnEc4R': 68990000,
                        '1FAqpN9a918kr7K1PMb7gKiFQ7cWPVSDbk': 1734582,
                        '12f47RSYPtV5PG5L5o8XikP4MfHfSPFUgy': 9000000,
                        '1NuRLMX4wv8QxJ2nWKzQXjeGHrEuaPDmkZ': 859620
                    },
                    'out': {
                        '131gAMNZdfE3bxYzZ2VpNbixYkYhKukFap': 147000000,
                        '1fUXYsDpdLmDHzZyMRfAgF9zKWNN1xWDF': 4127371,
                        '1FCsvQBBHy8WJfPzV2CjiLSXsz6H756wmZ': 1694582,
                        '1QK168vv3HWzJQnCNDkiFwPhzXubHmKDt1': 3000000,
                        '19ZLAYf7h4wW6UMo5usozjUtsazBS3MqyC': 6000000,
                        '16bgWQBVYXoXCrSJvxEw3WnPCEAbsnoLpM': 839620
                    }
                },
                2: {
                    'in': {
                        '1JRBisFrtAsY4E49419PSW6hLePH6jUdGi': 39900000,
                        '19ZLAYf7h4wW6UMo5usozjUtsazBS3MqyC': 6000000,
                        '1KnGS1Dtw54C2v6DfCFXDdmdDHruDhuGHZ': 36237371,
                        '1CbhowVaSNvdqHo9jpFZjc1UyYW4mnEc4R': 68990000,
                        '1FAqpN9a918kr7K1PMb7gKiFQ7cWPVSDbk': 1734582,
                        '12f47RSYPtV5PG5L5o8XikP4MfHfSPFUgy': 9000000,
                        '1NuRLMX4wv8QxJ2nWKzQXjeGHrEuaPDmkZ': 859620
                    },
                    'out': {
                        '131gAMNZdfE3bxYzZ2VpNbixYkYhKukFap': 147000000,
                        '1fUXYsDpdLmDHzZyMRfAgF9zKWNN1xWDF': 4127371,
                        '1FCsvQBBHy8WJfPzV2CjiLSXsz6H756wmZ': 1694582,
                        '1QK168vv3HWzJQnCNDkiFwPhzXubHmKDt1': 3000000,
                        '19ZLAYf7h4wW6UMo5usozjUtsazBS3MqyC': 6000000,
                        '16bgWQBVYXoXCrSJvxEw3WnPCEAbsnoLpM': 839620
                    }
                }
            }
        }, {
            '1KnGS1Dtw54C2v6DfCFXDdmdDHruDhuGHZ': {
                1: {
                    'in': {
                        '1JRBisFrtAsY4E49419PSW6hLePH6jUdGi': 39900000,
                        '19ZLAYf7h4wW6UMo5usozjUtsazBS3MqyC': 6000000,
                        '1KnGS1Dtw54C2v6DfCFXDdmdDHruDhuGHZ': 36237371,
                        '1CbhowVaSNvdqHo9jpFZjc1UyYW4mnEc4R': 68990000,
                        '1FAqpN9a918kr7K1PMb7gKiFQ7cWPVSDbk': 1734582,
                        '1KHJkHoZVg7AASSDnZZ6xLDyGRfFa5rdR6': 37237371,
                        '1Pk8fRv9XhcYfwLkZ9o6kL55oG6t7kB3fg': 2479506
                    },
                    'out': {
                        '131gAMNZdfE3bxYzZ2VpNbixYkYhKukFap': 147000000,
                        '1fUXYsDpdLmDHzZyMRfAgF9zKWNN1xWDF': 4127371,
                        '1FCsvQBBHy8WJfPzV2CjiLSXsz6H756wmZ': 1694582,
                        '1BMKGcsYSYJfSLpJfb2Ji8zcDmeLxn1WBw': 1000000,
                        '1KnGS1Dtw54C2v6DfCFXDdmdDHruDhuGHZ': 36237371,
                        '1VCXxGvjbdVrSGnpPEBD4TUhw1eQY54b1': 2459506
                    }
                },
                2: {
                    'in': {
                        '1JRBisFrtAsY4E49419PSW6hLePH6jUdGi': 39900000,
                        '19ZLAYf7h4wW6UMo5usozjUtsazBS3MqyC': 6000000,
                        '1KnGS1Dtw54C2v6DfCFXDdmdDHruDhuGHZ': 36237371,
                        '1CbhowVaSNvdqHo9jpFZjc1UyYW4mnEc4R': 68990000,
                        '1FAqpN9a918kr7K1PMb7gKiFQ7cWPVSDbk': 1734582,
                        '1KHJkHoZVg7AASSDnZZ6xLDyGRfFa5rdR6': 37237371,
                        '1Pk8fRv9XhcYfwLkZ9o6kL55oG6t7kB3fg': 2479506
                    },
                    'out': {
                        '131gAMNZdfE3bxYzZ2VpNbixYkYhKukFap': 147000000,
                        '1fUXYsDpdLmDHzZyMRfAgF9zKWNN1xWDF': 4127371,
                        '1FCsvQBBHy8WJfPzV2CjiLSXsz6H756wmZ': 1694582,
                        '1BMKGcsYSYJfSLpJfb2Ji8zcDmeLxn1WBw': 1000000,
                        '1KnGS1Dtw54C2v6DfCFXDdmdDHruDhuGHZ': 36237371,
                        '1VCXxGvjbdVrSGnpPEBD4TUhw1eQY54b1': 2459506
                    }
                }
            }
        }, {
            '1CbhowVaSNvdqHo9jpFZjc1UyYW4mnEc4R': {
                1: {
                    'in': {
                        '1JRBisFrtAsY4E49419PSW6hLePH6jUdGi': 39900000,
                        '19ZLAYf7h4wW6UMo5usozjUtsazBS3MqyC': 6000000,
                        '1KnGS1Dtw54C2v6DfCFXDdmdDHruDhuGHZ': 36237371,
                        '1CbhowVaSNvdqHo9jpFZjc1UyYW4mnEc4R': 68990000,
                        '1FAqpN9a918kr7K1PMb7gKiFQ7cWPVSDbk': 1734582,
                        '1u1emSJcQ1FxkhZVcRncXyJ4vxXdhFgcX': 69990000,
                        '112uaJKLqtxcmRHHhQAqNLUq9nXbPbwtSP': 1118510
                    },
                    'out': {
                        '131gAMNZdfE3bxYzZ2VpNbixYkYhKukFap': 147000000,
                        '1fUXYsDpdLmDHzZyMRfAgF9zKWNN1xWDF': 4127371,
                        '1FCsvQBBHy8WJfPzV2CjiLSXsz6H756wmZ': 1694582,
                        '12SghsJ6U3eDmoa9AV76ryQiMqAXAp2jXt': 1000000,
                        '1CbhowVaSNvdqHo9jpFZjc1UyYW4mnEc4R': 68990000,
                        '1P5J71DPQ3EHN1DuZssLVxQkcRmVkoGKGp': 1098510
                    }
                },
                2: {
                    'in': {
                        '1JRBisFrtAsY4E49419PSW6hLePH6jUdGi': 39900000,
                        '19ZLAYf7h4wW6UMo5usozjUtsazBS3MqyC': 6000000,
                        '1KnGS1Dtw54C2v6DfCFXDdmdDHruDhuGHZ': 36237371,
                        '1CbhowVaSNvdqHo9jpFZjc1UyYW4mnEc4R': 68990000,
                        '1FAqpN9a918kr7K1PMb7gKiFQ7cWPVSDbk': 1734582,
                        '1u1emSJcQ1FxkhZVcRncXyJ4vxXdhFgcX': 69990000,
                        '112uaJKLqtxcmRHHhQAqNLUq9nXbPbwtSP': 1118510
                    },
                    'out': {
                        '131gAMNZdfE3bxYzZ2VpNbixYkYhKukFap': 147000000,
                        '1fUXYsDpdLmDHzZyMRfAgF9zKWNN1xWDF': 4127371,
                        '1FCsvQBBHy8WJfPzV2CjiLSXsz6H756wmZ': 1694582,
                        '12SghsJ6U3eDmoa9AV76ryQiMqAXAp2jXt': 1000000,
                        '1CbhowVaSNvdqHo9jpFZjc1UyYW4mnEc4R': 68990000,
                        '1P5J71DPQ3EHN1DuZssLVxQkcRmVkoGKGp': 1098510
                    }
                }
            }
        }, {
            '1FAqpN9a918kr7K1PMb7gKiFQ7cWPVSDbk': {
                1: {
                    'in': {
                        '1JRBisFrtAsY4E49419PSW6hLePH6jUdGi': 39900000,
                        '19ZLAYf7h4wW6UMo5usozjUtsazBS3MqyC': 6000000,
                        '1KnGS1Dtw54C2v6DfCFXDdmdDHruDhuGHZ': 36237371,
                        '1CbhowVaSNvdqHo9jpFZjc1UyYW4mnEc4R': 68990000,
                        '1FAqpN9a918kr7K1PMb7gKiFQ7cWPVSDbk': 1734582,
                        '1BFtQJcNbGEgPNt8F1oZL3UorbdtHzUfUg': 6500000000,
                        '1KUzKRH86L3JD4sZMKhbREvu4YMD4Ut3AC': 1754582
                    },
                    'out': {
                        '131gAMNZdfE3bxYzZ2VpNbixYkYhKukFap': 147000000,
                        '1fUXYsDpdLmDHzZyMRfAgF9zKWNN1xWDF': 4127371,
                        '1FCsvQBBHy8WJfPzV2CjiLSXsz6H756wmZ': 1694582,
                        '1JuU2htC73x6KUi6JgySgEaj1kxkTUqF5A': 6500000000,
                        '1FAqpN9a918kr7K1PMb7gKiFQ7cWPVSDbk': 1734582
                    }
                },
                2: {
                    'in': {
                        '1JRBisFrtAsY4E49419PSW6hLePH6jUdGi': 39900000,
                        '19ZLAYf7h4wW6UMo5usozjUtsazBS3MqyC': 6000000,
                        '1KnGS1Dtw54C2v6DfCFXDdmdDHruDhuGHZ': 36237371,
                        '1CbhowVaSNvdqHo9jpFZjc1UyYW4mnEc4R': 68990000,
                        '1FAqpN9a918kr7K1PMb7gKiFQ7cWPVSDbk': 1734582,
                        '1BFtQJcNbGEgPNt8F1oZL3UorbdtHzUfUg': 6500000000,
                        '1KUzKRH86L3JD4sZMKhbREvu4YMD4Ut3AC': 1754582
                    },
                    'out': {
                        '131gAMNZdfE3bxYzZ2VpNbixYkYhKukFap': 147000000,
                        '1fUXYsDpdLmDHzZyMRfAgF9zKWNN1xWDF': 4127371,
                        '1FCsvQBBHy8WJfPzV2CjiLSXsz6H756wmZ': 1694582,
                        '1JuU2htC73x6KUi6JgySgEaj1kxkTUqF5A': 6500000000,
                        '1FAqpN9a918kr7K1PMb7gKiFQ7cWPVSDbk': 1734582
                    }
                }
            }
        }, {
            '1u1emSJcQ1FxkhZVcRncXyJ4vxXdhFgcX': {
                1: {
                    'in': {
                        '1u1emSJcQ1FxkhZVcRncXyJ4vxXdhFgcX': 69990000,
                        '112uaJKLqtxcmRHHhQAqNLUq9nXbPbwtSP': 1118510,
                        '1Gq3utV3KwYB3KJxGyx716Mt4gRZPMCBBD': 69990000,
                        '18xVSdavF3TAoeQwW5xhxP6Rx3dfnNjnCW': 379694
                    },
                    'out': {
                        '12SghsJ6U3eDmoa9AV76ryQiMqAXAp2jXt': 1000000,
                        '1CbhowVaSNvdqHo9jpFZjc1UyYW4mnEc4R': 68990000,
                        '1P5J71DPQ3EHN1DuZssLVxQkcRmVkoGKGp': 1098510,
                        '1u1emSJcQ1FxkhZVcRncXyJ4vxXdhFgcX': 69990000,
                        '1NrjxfyFwft6t2afehJX9bLb41SBqzuaWp': 359694
                    }
                },
                2: {
                    'in': {
                        '1u1emSJcQ1FxkhZVcRncXyJ4vxXdhFgcX': 69990000,
                        '112uaJKLqtxcmRHHhQAqNLUq9nXbPbwtSP': 1118510,
                        '1Gq3utV3KwYB3KJxGyx716Mt4gRZPMCBBD': 69990000,
                        '18xVSdavF3TAoeQwW5xhxP6Rx3dfnNjnCW': 379694
                    },
                    'out': {
                        '12SghsJ6U3eDmoa9AV76ryQiMqAXAp2jXt': 1000000,
                        '1CbhowVaSNvdqHo9jpFZjc1UyYW4mnEc4R': 68990000,
                        '1P5J71DPQ3EHN1DuZssLVxQkcRmVkoGKGp': 1098510,
                        '1u1emSJcQ1FxkhZVcRncXyJ4vxXdhFgcX': 69990000,
                        '1NrjxfyFwft6t2afehJX9bLb41SBqzuaWp': 359694
                    }
                }
            }
        }, {
            '112uaJKLqtxcmRHHhQAqNLUq9nXbPbwtSP': {
                1: {
                    'in': {
                        '1u1emSJcQ1FxkhZVcRncXyJ4vxXdhFgcX': 69990000,
                        '112uaJKLqtxcmRHHhQAqNLUq9nXbPbwtSP': 1118510,
                        '1Jskpfj6dt4byhwkCHxTC4LYqjVt9RBsjQ': 6300000,
                        '1DUK82c588CdgqQ9trd2Yc4D65tPu2vkNp': 1138510
                    },
                    'out': {
                        '12SghsJ6U3eDmoa9AV76ryQiMqAXAp2jXt': 1000000,
                        '1CbhowVaSNvdqHo9jpFZjc1UyYW4mnEc4R': 68990000,
                        '1P5J71DPQ3EHN1DuZssLVxQkcRmVkoGKGp': 1098510,
                        '1FVairxT8nnjmsZrNHLNEqDZ52SYYdm6YA': 6300000,
                        '112uaJKLqtxcmRHHhQAqNLUq9nXbPbwtSP': 1118510
                    }
                },
                2: {
                    'in': {
                        '1u1emSJcQ1FxkhZVcRncXyJ4vxXdhFgcX': 69990000,
                        '112uaJKLqtxcmRHHhQAqNLUq9nXbPbwtSP': 1118510,
                        '1Jskpfj6dt4byhwkCHxTC4LYqjVt9RBsjQ': 6300000,
                        '1DUK82c588CdgqQ9trd2Yc4D65tPu2vkNp': 1138510
                    },
                    'out': {
                        '12SghsJ6U3eDmoa9AV76ryQiMqAXAp2jXt': 1000000,
                        '1CbhowVaSNvdqHo9jpFZjc1UyYW4mnEc4R': 68990000,
                        '1P5J71DPQ3EHN1DuZssLVxQkcRmVkoGKGp': 1098510,
                        '1FVairxT8nnjmsZrNHLNEqDZ52SYYdm6YA': 6300000,
                        '112uaJKLqtxcmRHHhQAqNLUq9nXbPbwtSP': 1118510
                    }
                }
            }
        }
        ],
        'out': [{
            '131gAMNZdfE3bxYzZ2VpNbixYkYhKukFap': 147000000,
            '1fUXYsDpdLmDHzZyMRfAgF9zKWNN1xWDF': 4127371,
            '1FCsvQBBHy8WJfPzV2CjiLSXsz6H756wmZ': 1694582,
            '12SghsJ6U3eDmoa9AV76ryQiMqAXAp2jXt': 1000000,
            '1CbhowVaSNvdqHo9jpFZjc1UyYW4mnEc4R': 68990000,
            '1P5J71DPQ3EHN1DuZssLVxQkcRmVkoGKGp': 1098510
        }, {
            '131gAMNZdfE3bxYzZ2VpNbixYkYhKukFap': {
                1: {
                    'in': {
                        '131gAMNZdfE3bxYzZ2VpNbixYkYhKukFap': 147000000,
                        '16Zr3hByzj8HPcJRzBscTCmvfFGtw4QKUQ': 1639584,
                        '1JRBisFrtAsY4E49419PSW6hLePH6jUdGi': 39900000,
                        '19ZLAYf7h4wW6UMo5usozjUtsazBS3MqyC': 6000000,
                        '1KnGS1Dtw54C2v6DfCFXDdmdDHruDhuGHZ': 36237371,
                        '1CbhowVaSNvdqHo9jpFZjc1UyYW4mnEc4R': 68990000,
                        '1FAqpN9a918kr7K1PMb7gKiFQ7cWPVSDbk': 1734582
                    },
                    'out': {
                        '1KEYehgg3otPkpFhMrq6JRiob55UUsKiUn': 147000000,
                        '19mXLbWHN1cbw2hH6zU28tXd16TPKrjKVq': 1619584,
                        '131gAMNZdfE3bxYzZ2VpNbixYkYhKukFap': 147000000,
                        '1fUXYsDpdLmDHzZyMRfAgF9zKWNN1xWDF': 4127371,
                        '1FCsvQBBHy8WJfPzV2CjiLSXsz6H756wmZ': 1694582
                    }
                },
                2: {
                    'in': {
                        '131gAMNZdfE3bxYzZ2VpNbixYkYhKukFap': 147000000,
                        '16Zr3hByzj8HPcJRzBscTCmvfFGtw4QKUQ': 1639584,
                        '1JRBisFrtAsY4E49419PSW6hLePH6jUdGi': 39900000,
                        '19ZLAYf7h4wW6UMo5usozjUtsazBS3MqyC': 6000000,
                        '1KnGS1Dtw54C2v6DfCFXDdmdDHruDhuGHZ': 36237371,
                        '1CbhowVaSNvdqHo9jpFZjc1UyYW4mnEc4R': 68990000,
                        '1FAqpN9a918kr7K1PMb7gKiFQ7cWPVSDbk': 1734582
                    },
                    'out': {
                        '1KEYehgg3otPkpFhMrq6JRiob55UUsKiUn': 147000000,
                        '19mXLbWHN1cbw2hH6zU28tXd16TPKrjKVq': 1619584,
                        '131gAMNZdfE3bxYzZ2VpNbixYkYhKukFap': 147000000,
                        '1fUXYsDpdLmDHzZyMRfAgF9zKWNN1xWDF': 4127371,
                        '1FCsvQBBHy8WJfPzV2CjiLSXsz6H756wmZ': 1694582
                    }
                }
            }
        }, {
            '1fUXYsDpdLmDHzZyMRfAgF9zKWNN1xWDF': {
                1: {
                    'in': {
                        '1LYXVbkQ8UyqqDgJhfWoYTJqFVgUWmUcNu': 6964282,
                        '1fUXYsDpdLmDHzZyMRfAgF9zKWNN1xWDF': 4127371,
                        '1Eo68QFUekAoEUkBF7ZXdk6dxB669jemi9': 2659349,
                        '1JRBisFrtAsY4E49419PSW6hLePH6jUdGi': 39900000,
                        '19ZLAYf7h4wW6UMo5usozjUtsazBS3MqyC': 6000000,
                        '1KnGS1Dtw54C2v6DfCFXDdmdDHruDhuGHZ': 36237371,
                        '1CbhowVaSNvdqHo9jpFZjc1UyYW4mnEc4R': 68990000,
                        '1FAqpN9a918kr7K1PMb7gKiFQ7cWPVSDbk': 1734582
                    },
                    'out': {
                        '12YTv5PeKXfnTfadfVxMQ4DZ8Wqzh89iRy': 10000000,
                        '1CHFm64uGdndBM4GDf9ZYAoVfxyNAbqJCX': 1091653,
                        '1Bnq9MDLg4wupXuzF9Q8KR4v5RNDXKfkV3': 2639349,
                        '131gAMNZdfE3bxYzZ2VpNbixYkYhKukFap': 147000000,
                        '1fUXYsDpdLmDHzZyMRfAgF9zKWNN1xWDF': 4127371,
                        '1FCsvQBBHy8WJfPzV2CjiLSXsz6H756wmZ': 1694582
                    }
                },
                2: {
                    'in': {
                        '1LYXVbkQ8UyqqDgJhfWoYTJqFVgUWmUcNu': 6964282,
                        '1fUXYsDpdLmDHzZyMRfAgF9zKWNN1xWDF': 4127371,
                        '1Eo68QFUekAoEUkBF7ZXdk6dxB669jemi9': 2659349,
                        '1JRBisFrtAsY4E49419PSW6hLePH6jUdGi': 39900000,
                        '19ZLAYf7h4wW6UMo5usozjUtsazBS3MqyC': 6000000,
                        '1KnGS1Dtw54C2v6DfCFXDdmdDHruDhuGHZ': 36237371,
                        '1CbhowVaSNvdqHo9jpFZjc1UyYW4mnEc4R': 68990000,
                        '1FAqpN9a918kr7K1PMb7gKiFQ7cWPVSDbk': 1734582
                    },
                    'out': {
                        '12YTv5PeKXfnTfadfVxMQ4DZ8Wqzh89iRy': 10000000,
                        '1CHFm64uGdndBM4GDf9ZYAoVfxyNAbqJCX': 1091653,
                        '1Bnq9MDLg4wupXuzF9Q8KR4v5RNDXKfkV3': 2639349,
                        '131gAMNZdfE3bxYzZ2VpNbixYkYhKukFap': 147000000,
                        '1fUXYsDpdLmDHzZyMRfAgF9zKWNN1xWDF': 4127371,
                        '1FCsvQBBHy8WJfPzV2CjiLSXsz6H756wmZ': 1694582
                    }
                }
            }
        }, {
            '1FCsvQBBHy8WJfPzV2CjiLSXsz6H756wmZ': {
                1: {
                    'in': {
                        '1FzYx4dNdYuTT9Y2fpVELhXwvb93mcZPHR': 8000000,
                        '1FCsvQBBHy8WJfPzV2CjiLSXsz6H756wmZ': 1694582,
                        '1JRBisFrtAsY4E49419PSW6hLePH6jUdGi': 39900000,
                        '19ZLAYf7h4wW6UMo5usozjUtsazBS3MqyC': 6000000,
                        '1KnGS1Dtw54C2v6DfCFXDdmdDHruDhuGHZ': 36237371,
                        '1CbhowVaSNvdqHo9jpFZjc1UyYW4mnEc4R': 68990000,
                        '1FAqpN9a918kr7K1PMb7gKiFQ7cWPVSDbk': 1734582
                    },
                    'out': {
                        '15B2bQhF7ePoBeqm8LMTmf271oLhNxNyaR': 1000000,
                        '191x1PRTUT5mdH1AiZ2r59jPHWgtoaQJw4': 7000000,
                        '15jDJHmbM2w7Gc8m3vmNps1ZT1ms8J65DU': 1674582,
                        '131gAMNZdfE3bxYzZ2VpNbixYkYhKukFap': 147000000,
                        '1fUXYsDpdLmDHzZyMRfAgF9zKWNN1xWDF': 4127371,
                        '1FCsvQBBHy8WJfPzV2CjiLSXsz6H756wmZ': 1694582
                    }
                },
                2: {
                    'in': {
                        '1FzYx4dNdYuTT9Y2fpVELhXwvb93mcZPHR': 8000000,
                        '1FCsvQBBHy8WJfPzV2CjiLSXsz6H756wmZ': 1694582,
                        '1JRBisFrtAsY4E49419PSW6hLePH6jUdGi': 39900000,
                        '19ZLAYf7h4wW6UMo5usozjUtsazBS3MqyC': 6000000,
                        '1KnGS1Dtw54C2v6DfCFXDdmdDHruDhuGHZ': 36237371,
                        '1CbhowVaSNvdqHo9jpFZjc1UyYW4mnEc4R': 68990000,
                        '1FAqpN9a918kr7K1PMb7gKiFQ7cWPVSDbk': 1734582
                    },
                    'out': {
                        '15B2bQhF7ePoBeqm8LMTmf271oLhNxNyaR': 1000000,
                        '191x1PRTUT5mdH1AiZ2r59jPHWgtoaQJw4': 7000000,
                        '15jDJHmbM2w7Gc8m3vmNps1ZT1ms8J65DU': 1674582,
                        '131gAMNZdfE3bxYzZ2VpNbixYkYhKukFap': 147000000,
                        '1fUXYsDpdLmDHzZyMRfAgF9zKWNN1xWDF': 4127371,
                        '1FCsvQBBHy8WJfPzV2CjiLSXsz6H756wmZ': 1694582
                    }
                }
            }
        }, {
            '12SghsJ6U3eDmoa9AV76ryQiMqAXAp2jXt': {
                1: {
                    'in': {
                        '12SghsJ6U3eDmoa9AV76ryQiMqAXAp2jXt': 1000000,
                        '15m5F8QjvSMktB1bqPA7YfhYnn6G17B1fY': 2019656,
                        '1u1emSJcQ1FxkhZVcRncXyJ4vxXdhFgcX': 69990000,
                        '112uaJKLqtxcmRHHhQAqNLUq9nXbPbwtSP': 1118510
                    },
                    'out': {
                        '1CNdqCrUyjjvEmkXL3Q8svi3BZULdeCwNs': 1000000,
                        '15knpSWE9wiJr6ztwg1hCkzCRk2prVYXZt': 1999656,
                        '12SghsJ6U3eDmoa9AV76ryQiMqAXAp2jXt': 1000000,
                        '1CbhowVaSNvdqHo9jpFZjc1UyYW4mnEc4R': 68990000,
                        '1P5J71DPQ3EHN1DuZssLVxQkcRmVkoGKGp': 1098510
                    }
                },
                2: {
                    'in': {
                        '12SghsJ6U3eDmoa9AV76ryQiMqAXAp2jXt': 1000000,
                        '15m5F8QjvSMktB1bqPA7YfhYnn6G17B1fY': 2019656,
                        '1u1emSJcQ1FxkhZVcRncXyJ4vxXdhFgcX': 69990000,
                        '112uaJKLqtxcmRHHhQAqNLUq9nXbPbwtSP': 1118510
                    },
                    'out': {
                        '1CNdqCrUyjjvEmkXL3Q8svi3BZULdeCwNs': 1000000,
                        '15knpSWE9wiJr6ztwg1hCkzCRk2prVYXZt': 1999656,
                        '12SghsJ6U3eDmoa9AV76ryQiMqAXAp2jXt': 1000000,
                        '1CbhowVaSNvdqHo9jpFZjc1UyYW4mnEc4R': 68990000,
                        '1P5J71DPQ3EHN1DuZssLVxQkcRmVkoGKGp': 1098510
                    }
                }
            }
        }, {
            '1CbhowVaSNvdqHo9jpFZjc1UyYW4mnEc4R': {
                1: {
                    'in': {
                        '1JRBisFrtAsY4E49419PSW6hLePH6jUdGi': 39900000,
                        '19ZLAYf7h4wW6UMo5usozjUtsazBS3MqyC': 6000000,
                        '1KnGS1Dtw54C2v6DfCFXDdmdDHruDhuGHZ': 36237371,
                        '1CbhowVaSNvdqHo9jpFZjc1UyYW4mnEc4R': 68990000,
                        '1FAqpN9a918kr7K1PMb7gKiFQ7cWPVSDbk': 1734582,
                        '1u1emSJcQ1FxkhZVcRncXyJ4vxXdhFgcX': 69990000,
                        '112uaJKLqtxcmRHHhQAqNLUq9nXbPbwtSP': 1118510
                    },
                    'out': {
                        '131gAMNZdfE3bxYzZ2VpNbixYkYhKukFap': 147000000,
                        '1fUXYsDpdLmDHzZyMRfAgF9zKWNN1xWDF': 4127371,
                        '1FCsvQBBHy8WJfPzV2CjiLSXsz6H756wmZ': 1694582,
                        '12SghsJ6U3eDmoa9AV76ryQiMqAXAp2jXt': 1000000,
                        '1CbhowVaSNvdqHo9jpFZjc1UyYW4mnEc4R': 68990000,
                        '1P5J71DPQ3EHN1DuZssLVxQkcRmVkoGKGp': 1098510
                    }
                },
                2: {
                    'in': {
                        '1JRBisFrtAsY4E49419PSW6hLePH6jUdGi': 39900000,
                        '19ZLAYf7h4wW6UMo5usozjUtsazBS3MqyC': 6000000,
                        '1KnGS1Dtw54C2v6DfCFXDdmdDHruDhuGHZ': 36237371,
                        '1CbhowVaSNvdqHo9jpFZjc1UyYW4mnEc4R': 68990000,
                        '1FAqpN9a918kr7K1PMb7gKiFQ7cWPVSDbk': 1734582,
                        '1u1emSJcQ1FxkhZVcRncXyJ4vxXdhFgcX': 69990000,
                        '112uaJKLqtxcmRHHhQAqNLUq9nXbPbwtSP': 1118510
                    },
                    'out': {
                        '131gAMNZdfE3bxYzZ2VpNbixYkYhKukFap': 147000000,
                        '1fUXYsDpdLmDHzZyMRfAgF9zKWNN1xWDF': 4127371,
                        '1FCsvQBBHy8WJfPzV2CjiLSXsz6H756wmZ': 1694582,
                        '12SghsJ6U3eDmoa9AV76ryQiMqAXAp2jXt': 1000000,
                        '1CbhowVaSNvdqHo9jpFZjc1UyYW4mnEc4R': 68990000,
                        '1P5J71DPQ3EHN1DuZssLVxQkcRmVkoGKGp': 1098510
                    }
                }
            }
        }, {
            '1P5J71DPQ3EHN1DuZssLVxQkcRmVkoGKGp': {
                1: {
                    'in': {
                        '19Jbb1z27XnC81nYBh7J1CtFxSSMyp4wgF': 5000000,
                        '1P5J71DPQ3EHN1DuZssLVxQkcRmVkoGKGp': 1098510,
                        '1u1emSJcQ1FxkhZVcRncXyJ4vxXdhFgcX': 69990000,
                        '112uaJKLqtxcmRHHhQAqNLUq9nXbPbwtSP': 1118510
                    },
                    'out': {
                        '1HzULVofqH7GjpV77bxagJR5tCPEmcMMLu': 5000000,
                        '1AbxNQpQWnx1F86fR8mpAL4JUMRBFbpzdH': 1078510,
                        '12SghsJ6U3eDmoa9AV76ryQiMqAXAp2jXt': 1000000,
                        '1CbhowVaSNvdqHo9jpFZjc1UyYW4mnEc4R': 68990000,
                        '1P5J71DPQ3EHN1DuZssLVxQkcRmVkoGKGp': 1098510
                    }
                },
                2: {
                    'in': {
                        '19Jbb1z27XnC81nYBh7J1CtFxSSMyp4wgF': 5000000,
                        '1P5J71DPQ3EHN1DuZssLVxQkcRmVkoGKGp': 1098510,
                        '1u1emSJcQ1FxkhZVcRncXyJ4vxXdhFgcX': 69990000,
                        '112uaJKLqtxcmRHHhQAqNLUq9nXbPbwtSP': 1118510
                    },
                    'out': {
                        '1HzULVofqH7GjpV77bxagJR5tCPEmcMMLu': 5000000,
                        '1AbxNQpQWnx1F86fR8mpAL4JUMRBFbpzdH': 1078510,
                        '12SghsJ6U3eDmoa9AV76ryQiMqAXAp2jXt': 1000000,
                        '1CbhowVaSNvdqHo9jpFZjc1UyYW4mnEc4R': 68990000,
                        '1P5J71DPQ3EHN1DuZssLVxQkcRmVkoGKGp': 1098510
                    }
                }
            }
        }
        ]
    }
    nodes = [node]
    print(convert(nodes))


if __name__ == '__main__':
    main()
