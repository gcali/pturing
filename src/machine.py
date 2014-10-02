#!/usr/bin/env python3

from tape import Tape, BLANK, RESP
from transition import Transition

class Machine:
    def __init__(self, transition, tape=None, start_status=None):
        if tape == None:
            tape = Tape()
        self.tape = tape
        self.transition = transition
        if start_status:
            self.status = start_status
        else:
            self.status = transition.start_status

    def step(self):
        if self.status == "h" or self.status == "":
            return
        try:
            q,c,d = self.transition[self.status,self.tape.curr_char]
        except KeyError:
            self.status = ""
            return
        self.status = q
        self.tape = self.tape.step(c,d)

    def execute(self):
        steps = 0
        print(self)
        while self.status != "h" and self.status != "":
            self.step()
            print(self)
            steps +=1
        print("Steps: {}".format(steps))

    def __str__(self):
        dim_status = self.transition.max_len_status()
        dim_string = len("string")
        dim_status = max(dim_status,len(self.status))
        dim_string = max(dim_string, len(str(self.tape)))
        line_format = "{{:^{}}}|{{:<{}}}".format(dim_status,dim_string)
        return line_format.format(self.status,str(self.tape))

            
if __name__ == '__main__':
    t = Transition()
    t["q_0", RESP] = ("q_0", RESP, "R")
    t["q_0", "1"] = ("q_0", "1", "R")
    t["q_0", "+"] = ("q_1", "1", "R")
    t["q_1", "1"] = ("q_1", "1", "R")
    t["q_1", BLANK] = ("q_2", BLANK, "L")
    t["q_2", "1"] = ("h", BLANK, "-")
    m = Machine(t, Tape(RESP + "11+1"), "q_0")
    print("Machine:\n")
    print(m)
    #while m.status != "h" and m.status != "":
    #    m.step()
    #    print(m)
    m.execute()
