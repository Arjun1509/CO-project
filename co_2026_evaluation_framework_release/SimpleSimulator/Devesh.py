from Arjun import to_unsigned32, error, dmem_base, dmem_words, to_bin32

def mem_read(mem, addr):
    return mem.get(addr & ~3, 0)

def mem_write(mem,addr, val):
    mem[addr & ~3] = to_unsigned32(val)

#convrts binary lines into a list of instructions
def load_prog(lines):
    prog = []
    for ln in lines:
        prog.append(int(ln.strip(),2))
    return prog



def fetch_instr(prog, pc):
    idx = pc // 4
    if(idx < 0 or idx >= len(prog)):
        error(0, f"pc 0x{pc:08X} out of bounds")
    return prog[idx]

#print memory locations after halt
def mem_dump(mem):
    out_lines = []
    for i in range(dmem_words):
        addr =dmem_base + i * 4
        val  = mem.get(addr, 0)
        out_lines.append(f"0x{addr:08X}:{to_bin32(val)}")
        
    return out_lines
