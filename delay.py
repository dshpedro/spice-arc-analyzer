import sys
from utils import map_arcs, read_file, write_file

def generate_delay_measures(arcs, arcs_map, supply="1", v_out="out"):
    v_out = "f3_out" # placeholder
    measures = []
    
    prefix = ".measure tran delay_"
    trig_template = "\n+ trig v({}) val={}/2 td={}"
    targ_template = "\n+ targ v({}) val={}/2 td={}"

    for arc in arcs:
        literal = arcs_map[arc]['literal']
        td = f"{arcs_map[arc]['td']}ns"

        v_in = f"in_{literal}"

        trig = trig_template.format(v_in, supply, td)
        targ = targ_template.format(v_out, supply, td)

        low_high = f"{prefix}{arc}_lh{trig} fall=1{targ} rise=1"
        high_low = f"{prefix}{arc}_hl{trig} rise=1{targ} fall=1"

        measures.append(f"{low_high}\n{high_low}\n")

    return measures

def main():
    if len(sys.argv) < 2:
        print("Usage: py delay.py <arcs_file>")
        return

    arcs_file = sys.argv[1]
    arcs = read_file(arcs_file)
    
    arcs_map = map_arcs(arcs)
    measures = generate_delay_measures(arcs, arcs_map)

    output_filename = 'measures.txt'
    write_file(output_filename, measures)

if __name__ == '__main__':
    main()