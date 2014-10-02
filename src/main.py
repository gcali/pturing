#!/usr/bin/env python3

import sys
from parser import *
from tape import Tape
from transition import Transition
from machine import Machine

def process_file(name:str):
    print("Processing {}".format(name))
    with open(name) as f:
        program = f.read()
        token_transition,token_tape = tokenize(program)
        transition = parse_transition(token_transition)
        print("Transition:")
        print(transition)
        tape = parse_tape(token_tape)
        print("Tape:")
        print(tape)
        machine = Machine(transition,tape)
        print("Execution:")
        machine.execute()
    print()

if __name__ == '__main__':
    args = sys.argv[1:]
    if args:
        for name in args:
            process_file(name)
        sys.exit(0)
    else:
        print("Please give at least a file to process as an argument", file=sys.stderr)
        sys.exit(1)
