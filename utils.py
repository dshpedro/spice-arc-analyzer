def read_file(filename):
    with open(filename, 'r') as file:
        lines = file.readlines()
        return [line.strip() for line in lines]

def write_file(filename, data):
    with open(filename, 'w') as file:
        for line in data:
            file.write(f"{line}\n")

def map_arcs(arcs, interval=1):
    arcs_map = {}
    td = -2

    for polarized_arc in arcs:
        polarity = polarized_arc[-1] # last char is either (D)irect or (R)everse
        arc = polarized_arc[:-1] # everything but the polarity char
        literal = next(char for char in arc if char.isalpha())

        td += 3 * interval
        arcs_map[arc] = {'literal': literal, 'td': td, 'polarity': polarity}

    return arcs_map

