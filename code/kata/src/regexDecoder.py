#!/usr/bin/env python3

import sys
import re


def decode(ciphertext):
    # Simple Regex
    regex = re.compile(r'((?P<varStart>[A-Z]).*?(?P=varStart))')
    # Final Regex
    # regex = re.compile(r'((?P<varStart>[A-Z]).*?[^0](?P=varStart))')

    matches = regex.findall(ciphertext)

    return [match[0] for match in matches]


def main(argv):
    print('Detecting variables in ciphertext: %s' % argv[0])
    print(decode(argv[0]))


if __name__ == "__main__":
    main(sys.argv[1:])
