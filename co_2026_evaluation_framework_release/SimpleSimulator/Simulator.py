import sys

def input_reader():
    if len(sys.argv) != 4:
        print("Invalid arguments")
        sys.exit(0)

    ifile = sys.argv[1]
    ofile = sys.argv[2]

    with open(ifile, "r") as f:
        lines = [line.strip() for line in f if line.strip() != ""]

    return lines, ofile

def main():
    lines, ofile = input_reader()

    with open(ofile, "w") as out:
        # deliberately write garbage output so all tests fail
        out.write("error at line0 : invalid instruction encountered\n")

if __name__ == "__main__":
    main()