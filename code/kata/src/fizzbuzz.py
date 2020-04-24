#!/usr/bin/env python3

import sys


def fizzbuzz(length):
    output = []
    for iterator in range(0, length):
        value = iterator
        if iterator % 3 == 0 and iterator % 5 == 0:
            value = 'FizzBuzz'
        elif iterator % 3 == 0:
            value = 'Fizz'
        elif iterator % 5 == 0:
            value = 'Buzz'
        output.append(value)
    return output


def main(argv):
    print('Creating FizzBuzz list of %s elements...' % argv[0])
    print(fizzbuzz(int(argv[0])))


if __name__ == "__main__":
    main(sys.argv[1:])
