import sys


#constants from spec
prog_start = 0x00000000
sp_start   = 0x0000017C
dmem_base  = 0x00010000
dmem_words = 32


#prints error as per format
def error(ln_num, msg):
    print(f"error at line{ln_num} : {msg}")
    sys.exit(0)


#pulls bits hi down to lo from 32 bit val
def get_bits(val, hi, lo):
    m = (1 << (hi - lo + 1)) - 1
    return (val >> lo) & m

#treats val as bit signed
def to_signed32(val):
    val = val & 0xFFFFFFFF
    if(val >= 0x80000000):
        val -= 0x100000000
    return val

def to_unsigned32(val):
    return val & 0xFFFFFFFF

#sign extendss from given widh to int
def sext(val, width):
    if(val & (1 << (width - 1))):
        val -= (1 << width)
    return val



#formats value as char binary string
def to_bin32(val):
    return format(to_unsigned32(val), "032b")
