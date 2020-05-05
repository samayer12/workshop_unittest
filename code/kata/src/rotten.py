#!/usr/bin/env python3

import sys
from string import ascii_lowercase, ascii_uppercase


# Sourced from https://eddmann.com/posts/implementing-rot13-and-rot-n-caesar-ciphers-in-python/
def rotN(cleartext, n):
    lookup = str.maketrans(ascii_lowercase + ascii_uppercase,
                           ascii_lowercase[n:] + ascii_lowercase[:n] +
                           ascii_uppercase[n:] + ascii_uppercase[:n])
    ciphertext = lambda s: s.translate(lookup)
    return ciphertext(cleartext)

# '0123456789'
# '0123456789'[n:] + '0123456789'[:n])

def main(argv):
    print('Initiating quantum-resistant crypto subroutine with cleartext: %s' % argv[0])
    print(rotN(argv[0], int(argv[1])))


if __name__ == "__main__":
    main(sys.argv[1:])
