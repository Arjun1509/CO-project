from Arjun import to_signed32, to_unsigned32, error, prog_start, sp_start, to_bin32
from Amukh import decode_instr
from Devesh import mem_read, mem_write, fetch_instr

def run_instr(instr, reg, mem, pc):
    op, rd, funct3, rs1, rs2, funct7, imm_i, imm_s, imm_b, imm_u, imm_j = decode_instr(instr)
    isHalt = ( op == 0b1100011 and funct3 == 0 and rs1 == 0 and rs2 == 0 and imm_b == 0)


    nextPc = pc + 4
    #r type 

    if(op == 0b0110011):
        sA = to_signed32(reg[rs1])
        sB = to_signed32(reg[rs2])
        uA = to_unsigned32(reg[rs1])
        uB = to_unsigned32(reg[rs2])
        shift = reg[rs2] & 0x1F

        if funct3 == 0b000:
            if(funct7 == 0b0000000):
                result = sA + sB
            else:
                result = sA- sB
        elif(funct3 == 0b001):
            result = uA <<shift
        elif(funct3 == 0b010):
            if (sA < sB):
                result = 1
            else:
                result = 0

        elif(funct3 ==0b011):
            if uA < uB:
                result = 1
            else:
                result = 0

        elif(funct3 == 0b100 ):
            result = uA^uB

        elif(funct3 == 0b110):
            result = uA | uB
        elif(funct3 == 0b101):
            result = uA >> shift
        elif funct3 == 0b111:
            result = uA&uB
        else:
            error(0, "Invalid r type instruction")
        
        if(rd != 0):
            reg[rd] = to_unsigned32(result)
    

    #i type 
    elif (op == 0b0010011):
        sA = to_signed32(reg[rs1])
        uA = to_unsigned32(reg[rs1])

        if(funct3 == 0b000):
            result=  sA+ imm_i
        elif(funct3 == 0b011):
            if uA < to_unsigned32(imm_i):
                result = 1
            else:
                result = 0
        else:
            error(0, "Invvalid i type instruction")

        if(rd != 0):
            reg[rd] = to_unsigned32(result)
    

    #lw
    elif(op == 0b0000011):
        addr = to_unsigned32(to_signed32(reg[rs1]) + imm_i)
        if rd != 0:
            reg[rd] = mem_read(mem, addr)

    #sw 
    elif op == 0b0100011:
        addr = to_unsigned32(to_signed32(reg[rs1]) + imm_s)
        mem_write(mem, addr, reg[rs2])
    
    #b type
    elif(op == 0b1100011):
        sA = to_signed32(reg[rs1])
        sB = to_signed32(reg[rs2])
        uA = to_unsigned32(reg[rs1])
        uB = to_unsigned32(reg[rs2])

        taken = False

        if(funct3 == 0b000):
            taken = (sA == sB)
        elif(funct3 == 0b001):
            taken = (sA != sB )
        elif(funct3 == 0b100):
            taken = (sB > sA)
        elif(funct3 == 0b101):
            taken = (sA >= sB)
        elif(funct3 == 0b110):
            taken = (uA < uB)
        elif(funct3 == 0b111):
            taken = (uA >= uB)

        if taken:
            nextPc = pc + imm_b
    
    #jal
    elif(op== 0b1101111):

        if(rd!=0):
            reg[rd] = to_unsigned32(pc + 4)
        nextPc = pc + imm_j

    #jalr
    elif(op == 0b1100111):
        target = to_unsigned32(to_signed32(reg[rs1])+ imm_i) & ~1
        if(rd!= 0):
            reg[rd]= to_unsigned32(pc+4)
        nextPc = target

    
    #lui
    elif(op == 0b0110111):
        if(rd != 0):
            reg[rd] = to_unsigned32(imm_u)
    
    #auipc
    elif( op == 0b0010111):
        if(rd != 0):
            reg[rd] = to_unsigned32(pc + imm_u)
       

    else:
        error(0, f"Invalid instruction at pc {pc}")
    
    reg[0] = 0
    return nextPc, isHalt

def simulate(prog, mem):
    reg = [0] * 32
    reg[2] = sp_start

    pc = prog_start
    outLines = []

    for x in range(100000000):
        instr = fetch_instr(prog, pc)
        nextPc, isHalt = run_instr(instr, reg, mem, pc)

        if isHalt:
            snapPc = pc
        else:
            snapPc = nextPc

        regStr = " ".join(to_bin32(r) for r in reg) + " "
        outLines.append(to_bin32(snapPc) + " " + regStr)
        
        pc = nextPc
        if isHalt:
            break
    else:
        error(0, "too many steps, prob infinite loop")

    return outLines
