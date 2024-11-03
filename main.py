def read_file(filename):
    with open(filename, 'r') as file:
        lines = file.readlines()
        return [line.strip() for line in lines]

def write_file(filename, data):
    with open(filename, 'w') as file:
        for line in data:
            file.write(f"{line}\n")

def generate_delay_measures(arcs, supply="1", v_out="out"):
    v_out = "f3_out" # placeholder
    measures = []
    
    prefix = ".measure trans delay_"
    trig_template = "\n+ trig v({}) val={}/2 td={}"
    targ_template = "\n+ targ v({}) val={}/2 td={}"

    for arc in arcs:
        v_in = f"v_in_{next(char for char in arc if char.isalpha())}"
        td = "1ns"

        trig = trig_template.format(v_in, supply, td)
        targ = targ_template.format(v_out, supply, td)

        low_high = f"{prefix}{arc}_lh{trig} fall=1{targ} rise=1"
        high_low = f"{prefix}{arc}_hl{trig} rise=1{targ} fall=1"

        measures.append(f"{low_high}\n{high_low}\n")

    return measures

def main():
    arcs_file = 'arcs.txt'
    measures_file = 'measures.txt'
    
    arcs = read_file(arcs_file)
    
    measures = generate_delay_measures(arcs)
    write_file(measures_file, measures)

if __name__ == '__main__':
    main()

