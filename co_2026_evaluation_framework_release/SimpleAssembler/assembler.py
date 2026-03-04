import sys

def error(ln_num, msg):
#prints error as per file
    print(f"error at line{ln_num} : {msg}" )
    sys.exit(0)

def input_reader():
#reads the input 
    if len(sys.argv) != 3:
        print("Invalid arguments")
        sys.exit(0)

    ifile = sys.argv[1]
    ofile = sys.argv[2]

    with open(ifile, "r") as f:
        lines = [line.strip() for line in f if line.strip() != ""]

    return lines, ofile

def label_mapper(lines):
#it identifies the labels acc to file and assigns pc addresses to them
    label_table = {}
    pc = 0

    for i, line in enumerate(lines):
        if ":" in line:
            part = line.split(":")
            label = part[0].strip()

            if not label[0].isalpha():
                error(i+1, "Invalid label name")

            if label in label_table:
                error(i+1, "Duplicate label")

            label_table[label] = pc

            if part[1].strip() != "":
                pc += 4

        else:
            pc += 4

    return label_table
