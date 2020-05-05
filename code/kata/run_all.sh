#!/bin/bash
# from directory `unittest/code/kata` execute:

# FizzBuzz
python -m unittest test/test_fizzbuzz.py
python src/fizzbuzz.py 10
    Expect output ['FizzBuzz', 1, 2, 'Fizz', 4, 'Buzz', 'Fizz', 7, 8, 'Fizz']

# Regex Decoder
python -m unittest test/test_regexDecoder.py
    # Expect two failing tests if you aren't using "Final Regex"
python src/regexDecoder.py AuAZ0ZZ
    # Expect output ['AUA', 'Z0Z'] if you are using "Simple Regex"
    # Expect output ['AUA', 'Z0ZZ'] if you are using "Final Regex"

# ROT-N
python -m unittest test/test_rotten.py
    # Expect one failing test if you haven't added integer support
python src/rotten.py Words 1
    # Expect output "Xpset"
