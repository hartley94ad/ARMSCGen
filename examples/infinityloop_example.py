#!python

from TesterModule import *
import sys

def Run(argv):
    """infinityloop shellcode example

    Args: 
        argv(list): arugment(s)
    """
    if len(argv) > 0:
        fname = argv[0]
    else:
        fname = 'NeverMind'

    # ARMSCGen Thumb Class
    scgen = thumbSCGen()
    
    # generates chmod with options
    #   
    scode  = scgen.infinityloop()
    # never reach
    scode += scgen.exit(0)

    # compiles shellcode
    scode_binary = CompileSC(scode, isThumb=True)

    # make an encoder with XOR key and compiles
    xor_encoder_with_scode_binary = MakeXorShellcode( scode_binary )

    print printHex(xor_encoder_with_scode_binary)

if __name__ == '__main__':
    Run(sys.argv[1:])
