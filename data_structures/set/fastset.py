"""optimize with linear-time scans using dictionaries"""

import set


                                           # fastest.Set extends set.Set
class Set(set.Set):
    def __init__(self, value = []):
        self.data = {}                     # manages a local dictionary
        self.concat(value)                 # hashing: linear search times

    def intersect(self, other):
        res = {}
        for x in other:                    # other: a sequence or Set
            if x in self.data:             # use hash-table lookup; 3.X
                res[x] = None
        return Set(res.keys())             # a new dictionary-based Set

    def union(self, other):
        # res = {}                           # other: a sequence or Set
        # for x in other:                    # scan each set just once
        #     res[x] = None
        for x in other:         # '&' and '|' come back here
            self.data[x] = None                  # so they make new fastset's
        return Set(self.data.keys())

    def concat(self, value):
        for x in value: self.data[x] = None

    # inherit and, or, len
    def __getitem__(self, ix):
        return list(self.data.keys())[ix]            # 3.X: list()

    def __repr__(self):
        return '<Set:%r>' % list(self.data.keys())  # ditto


if __name__ == "__main__":
    users1 = Set(['Bob', 'Emily', 'Howard', 'Carol','Peeper'])
    users2 = Set(['Jerry', 'Howard', 'Carol', 'Smbat'])
    users3 = Set(['Emily', 'Carol', 'Howard'])
    print(users1 | users2)