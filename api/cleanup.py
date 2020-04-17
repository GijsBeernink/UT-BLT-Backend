import re
import os

# Location of the result of the API call. Store these to make less API calls and get blocked less
# fast.
FILE_STRUCTURE_API_CALL = '../databases/result_for_address_{}.txt'
# Store results with specific depth.
FILE_STRUCTURE_RESULT_WITH_DEPTH = '../databases/results/address_{}_with_depth_{}.txt'


def get_address_from_file(filename):
    try:
        res = filename.split('_')[3].split('.')[0]
    except IndexError:
        print("Went wrong at {} ".format(filename))
        return
    return res


f = open(FILE_STRUCTURE_RESULT_WITH_DEPTH.format("1LYz7EgAF8PU6bSN8GDecnz9Gg814fs81W", 2))
# lines = str(f.readlines())

pattern = re.compile("[1-3a-km-zA-HJ-NP-Z1-9]{25,34}")

addresses = pattern.findall(f.readlines()[0])

for file in os.listdir("../databases/"):
    # print(file)
    # print(get_address_from_file(file))
    if get_address_from_file(file) not in addresses:
        try:
            os.remove("../databases/{}".format(file))
        except IsADirectoryError as e:
            print("Not removing directory")
