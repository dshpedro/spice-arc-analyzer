import subprocess

def main():
    arcs_file = 'arcs.txt'
    subprocess.run(['python', 'delay.py', arcs_file])

if __name__ == '__main__':
    main()

