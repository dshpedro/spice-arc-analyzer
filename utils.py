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

    for arc in arcs:
        literal = next(char for char in arc if char.isalpha())
        td += 3 * interval
        arcs_map[arc] = {'literal': literal, 'td': td }

    return arcs_map

