#!/usr/bin/env python3

BLANK = '#'
RESP = '»'
DIR = { "R" : 1, "L" : -1, "-" : 0, ">" : 1, "<" : -1}

from color import Color


class Tape:
    def __init__(self, content=RESP, current=0):
        if content[0] != RESP:
            raise ValueError("The first character of the tape must be " +\
                             RESP)
        self._content = content
        self.current = current

    def __str__(self):
        if self.current < len(str(self._content)):
            string = str(self._content)
        else:
            string = str(self._content) + BLANK * (self.current + 1 - len(str(self._content)))
        return string[:self.current] +\
               Color.UNDERLINE + Color.BOLD +\
                    string[self.current] +\
               Color.END +\
               string[self.current+1:]

    def __getitem__(self, key):
        try:
            return self._content[key]
        except IndexError:
            return BLANK

    def __delitem__(self,key):
        raise TypeError("Tape is immutable")

    def __setitem__(self,key,value):
        raise TypeError("Tape is immutable")

    @property
    def curr_char(self):
        return self[self.current]

    def step(self, new_c, direction):
        new_content = self._content[:self.current] + new_c +\
                      self._content[self.current + 1:]
        direction = direction.upper()
        i = len(new_content) - 1
        while new_content[i] == '#' and i > self.current:
            i -= 1
        new_content = new_content[:i+1]
        return Tape(new_content, self.current + DIR[direction])

if __name__ == '__main__':
    t = Tape(RESP + BLANK + BLANK + "a")
    try :
        Tape(BLANK)
        print("Shouldn't be here")
    except ValueError:
        print("First c must be RESP")
    print(t)
    try:
        t.step("a", "R")
        print("Shouldn't be here")
    except ValueError:
        print("ok")
    t = t.step(RESP, "R")
    t = t.step("a", "R")
    t.current = 10
    print(t)
