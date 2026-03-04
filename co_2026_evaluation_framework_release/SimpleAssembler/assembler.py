import sys

def error(ln_num, msg):
#prints error as per file
    print(f"error at line{ln_num} : {msg}" )
    sys.exit(0)

def input_reader():
#reads the input 
    if len(sys.argv) != 3:
        print("invalid arguments")
        sys.exit(0)

    ifile = sys.argv[1]
    ofile = sys.argv[2]

    with open(ifile, "r") as f:
        lines = [line.strip() for line in f if line.strip() != ""]

    return lines, ofile

