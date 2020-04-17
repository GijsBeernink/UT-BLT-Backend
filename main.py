# Change the address to analyse here.
ADDRESS = '1LYz7EgAF8PU6bSN8GDecnz9Gg814fs81W'

# How far should be searched in all directions (inputs and outputs).
DEPTH = 2


if __name__ == '__main__':
    from api.converter import start_analysis
    start_analysis(address=ADDRESS, depth=DEPTH)
