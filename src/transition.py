#!/usr/bin/env python3

class Transition:
    
    def __init__(self, start_status=None):
        self._table = {}
        self.start_status = start_status

    def __iter__(self):
        for status in self._table:
            yield status

    def __setitem__(self, key, value):
        status,c = key
        if not self.start_status:
            self.start_status = status
        if not status in self._table:
            self._table[status] = {}
        self._table[status][c] = value

    def __getitem__(self, key):
        status,c = key
        return self._table[status][c]

    def get_chars(self, status):
        return [c for c in self._table[status]]

    def max_len_status(self):
        max_dim = 1
        for s in self._table:
            max_dim = max(max_dim, len(s))
            for c in self.get_chars(s):
                dest_s,_,_ = self[s,c]
                max_dim = max(max_dim,len(dest_s))
        return max_dim

    def __str__(self):
        max_dims = [1,1,5]
        for s in self._table:
            if max_dims[0] < len(str(s)):
                max_dims[0] = len(str(s))
            for c in self._table[s]:
                if max_dims[1] < len(str(c)):
                    max_dims[1] = len(str(c))
                t = self[s,c]
                if max_dims[2] < len(str(t)):
                    max_dims[2] = len(str(t))
        line_format = "{{0:^{}}} | {{1:^{}}} | {{2:^{}}} |".format(*max_dims)
        header = line_format.format("q", "s", "trans")
        separator = "-" * len(header)
        lines = [line_format.format(s,c,str(self[s,c]))\
                                                   for s in self._table\
                                                   for c in self._table[s]]
        return "\n".join([header, separator] + lines)


if __name__ == '__main__':

    t = Transition()
    t["q_0","#"] = ("q_1","a","-")
    print(t.get_chars("q_0"))
    for c in t.get_chars("q_0"):
        print(t["q_0",c])
    print(t)
