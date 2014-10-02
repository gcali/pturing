#!/usr/bin/env python3

import sys
from parser import *
from tape import Tape
from transition import Transition
from machine import Machine

def process_start_trans_tape(start_status, transition, tape):
    print("Transition:")
    print(transition)
    print("Tape:")
    print(tape)
    if not start_status:
        machine = Machine(transition,tape)
    else:
        machine = Machine(transition,tape,start_status)
    print("Execution:")
    machine.execute()

def process_program(program:str):
    token_header,token_transition,token_tape = tokenize(program)
    if token_header:
        start_status = parse_header(token_header)["start"]
    else:
        start_status = None
    transition = parse_transition(token_transition)
    tape = parse_tape(token_tape)
    return process_start_trans_tape(start_status,transition,tape)

def process_file(name:str):
    print("Processing {}".format(name))
    with open(name) as f:
        program = f.read()
        process_program(program)
    print()

if __name__ == '__main__':
    args = sys.argv[1:]
    if len(args) == 1:
        process_file(args[0])
        sys.exit(0)
    elif args:
        pass
    else:
        print("Please give at least a file to process as an argument", file=sys.stderr)
        sys.exit(1)
