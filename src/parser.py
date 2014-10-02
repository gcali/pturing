#!/usr/bin/env python3

from tape import Tape, BLANK, RESP
from transition import Transition
import re

import sys

class NotRecognizedCharacterException(Exception):
    pass

class TokenList(list):
    pass

import string

alphabet = string.ascii_letters + string.digits + "#" + "»"

def tokenize(program:str) -> TokenList:
    [transition,tape] = program.split("---")
    transition_iter = map(lambda x: x[1:-1],re.findall(r"\(.*?\)", transition))
    return (transition_iter, tape.strip())

def parse_tape(tape_string:str) -> Tape:
    for c in tape_string:
        if c not in alphabet:
            raise NotRecognizedCharacterException("Character {} not valid in tape".format(c))
    return Tape(tape_string)    

def parse_transition(transition_iter:"iter") -> Transition:
    transition = Transition()
    for t in transition_iter:
        try:
            [sstatus,ssym,estatus,esym,direction] = t.split(",")
        except ValueError:
            raise ValueError(\
                "Number of elements of tuple wrong: {}".format(t))
        transition[sstatus,ssym] = (estatus,esym,direction)
    return transition


if __name__ == '__main__':
    
    args = sys.argv[1:]
    if args:
        with open(args[0]) as f:
            program = f.read()
    else:
        program = "(a,b,c,d,e) --- {}test".format(RESP)
    (tr,ta) = tokenize(program)
    transition = parse_transition(tr)
    tape = parse_tape(ta)
    print("Transition")
    print(transition)
    print("Tape")
    print(tape)
