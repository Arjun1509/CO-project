import sys

def error(ln_num, msg):
#prints error as per file
    print(f"error at line{ln_num} : {msg}" )
    sys.exit(0) 