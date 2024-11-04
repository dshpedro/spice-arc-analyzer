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
        polarity = arcs_map[arc]['polarity']
        
        # Define trigger edges based on polarity
        lh_trig_edge = "rise=1" if polarity == "D" else "fall=1"
        hl_trig_edge = "fall=1" if polarity == "D" else "rise=1"

        v_in = f"in_{literal}"

        trig = trig_template.format(v_in, supply, td)
        targ = targ_template.format(v_out, supply, td)

        low_high = f"{prefix}{arc}_lh{trig} {lh_trig_edge}{targ} rise=1"
        high_low = f"{prefix}{arc}_hl{trig} {hl_trig_edge}{targ} fall=1"

        measures.append(f"{low_high}\n{high_low}\n")

    return measures

def main():
    if len(sys.argv) < 2:
        print("Usage: py delay.py <arcs_file>")
        return

    arcs_file = sys.argv[1]
    polarized_arcs = read_file(arcs_file)
    arcs = [arc[:-1] for arc in polarized_arcs]

    arcs_map = map_arcs(polarized_arcs)
    measures = generate_delay_measures(arcs, arcs_map)

    output_filename = 'delay.meas'
    write_file(output_filename, measures)

if __name__ == '__main__':
    main()
