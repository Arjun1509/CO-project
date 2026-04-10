import sys
from Devesh import load_prog, mem_dump
from Anand import simulate


def input_reader():

    if len(sys.argv) != 4:
        print("Invalid arguments")
        sys.exit(0)

    ifile = sys.argv[1]
    ofile = sys.argv[2]
    # sysargv is the read trace output file it is not used by simulator

    with open(ifile, "r") as f:
        lines = [line.strip() for line in f if line.strip() != ""]

    return lines, ofile



def main():
    lines, ofile = input_reader()

    mem  = {}
    prog = load_prog(lines)
    out_lines = simulate(prog, mem)
    mem_lines = mem_dump(mem)

    with open(ofile, "w") as out:
        for ln in out_lines + mem_lines:
            out.write(ln + "\n")


if __name__ == "__main__":
    main()