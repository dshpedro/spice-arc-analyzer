import subprocess

def main():
    arcs_file = 'polarized_arcs.txt'
    subprocess.run(['python', 'delay.py', arcs_file])
    subprocess.run(['python', 'power.py', arcs_file])

if __name__ == '__main__':
    main()

