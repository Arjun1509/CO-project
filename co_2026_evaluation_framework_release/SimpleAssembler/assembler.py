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

#registers table
reg_table = {
    "zero": 0, "ra":1,
    "sp":2, "gp":3,
    "tp":4, "t0":5,
    "t1":6, "t2":7,
    "s0":8, "s1":9,
    "a0":10, "a1":11,
    "a2":12, "a3":13,
    "a4":14, "a5":15,
    "a6":16, "a7":17,
    "s2":18, "s3":19,
    "s4":20, "s5":21,
    "s6":22, "s7":23,
    "s8":24, "s9":25,
    "s10": 26, "s11":27,
    "t3":28, "t4":29,
    "t5":30, "t6":31
    }

#converts register num to binary 
def reg2bin(reg, line_num) :
    if reg not in reg_table:
        error(line_num, "Invalid register\n")
    return format(reg_table[reg], "05b")


#converts immediate value to binary
def imm2bin(value, bits, line_num):
    min_range = -(2**(bits-1))
    max_range = 2**(bits-1) - 1
    if (value < min_range or value > max_range):
        error(line_num, "Immediate value out of range")

    return format(value & (1<<bits)-1, f"0{bits}b")


#r type instruction set 
def encode_r(tokens, funct3, funct7, line_num):
    rd = reg_table(tokens[1], line_num)
    rs1 = reg_table(tokens[2], line_num)
    rs2 = reg_table(tokens[3], line_num)
    opcode = "0110011"

    return funct7 + rs2 + rs1 + funct3 + rd + opcode


#i type instruction set
def encode_i(tokens, funct3, opcode, line_num):
    rd = reg_table(tokens[1], line_num)
    rs1 = reg_table(tokens[2], line_num)
    imm = imm2bin(int(tokens[3], 12, line_num))

    return imm + rs1 + funct3 + rd + opcode
