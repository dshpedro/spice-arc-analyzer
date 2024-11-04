import sys
from utils import map_arcs, read_file, write_file

def generate_power_measures(arcs, arcs_map, v_source="v2", node="vdd2"):
    measures = []
    
    prefix = ".measure tran static_consumption_"
    sufix_template = "avg(i({})*-v({})) from={:.2f}ns to={}ns"

    for arc in arcs:
        td = arcs_map[arc]['td']
        from_hl = td + 0.97
        to_hl = td + 1
        from_lh = td + 1.97
        to_lh = td + 2

        sufix = sufix_template.format(v_source, node, from_hl, to_hl)
        high_low = f"{prefix}{arc}_hl {sufix}"
        
        sufix = sufix_template.format(v_source, node, from_lh, to_lh)
        low_high = f"{prefix}{arc}_lh {sufix}"

        measures.append(f"{high_low}\n{low_high}\n")

    return measures

def main():
    if len(sys.argv) < 2:
        print("Usage: py power.py <arcs_file>")
        return

    arcs_file = sys.argv[1]
    arcs = read_file(arcs_file)
    
    arcs_map = map_arcs(arcs)
    measures = generate_power_measures(arcs, arcs_map)

    output_filename = 'measures_power.txt'
    write_file(output_filename, measures)

if __name__ == '__main__':
    main()

