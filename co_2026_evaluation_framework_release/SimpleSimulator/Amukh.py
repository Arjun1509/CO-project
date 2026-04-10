from Arjun import get_bits, sext

def decode_instr(instr):
    op = get_bits(instr,6,0)
    rd = get_bits(instr,11,7)
    func3 = get_bits(instr,14,12)
    rs1 = get_bits(instr,19,15)
    rs2 = get_bits(instr,24,20)
    func7 = get_bits(instr,31,25)
    #i Type
    imm_i = sext(get_bits(instr,31,20),12)
    #s Type
    imm_s= sext((get_bits(instr,31,25)<<5)|get_bits(instr,11,7),12)
    #b Type
    b12 = get_bits(instr,31,31)
    b11= get_bits(instr,7,7)
    b10_5 = get_bits(instr,30,25)
    b4_1 =get_bits(instr,11,8)
    imm_b= sext((b12<<12)|(b11<<11)|(b10_5<<5)|(b4_1<<1),13)
    #u Type
    imm_u = sext(get_bits(instr,31,12)<<12,32)
    #j Type
    j20 = get_bits(instr,31,31)
    j19_12=get_bits(instr,19,12)
    j11 = get_bits(instr,20,20)
    j10_1 =get_bits(instr,30,21)
    imm_j= sext((j20<<20)|(j19_12<<12)|(j11<<11)|(j10_1<<1),21)

    return op,rd,func3,rs1,rs2,func7, imm_i,imm_s,imm_b,imm_u,imm_j