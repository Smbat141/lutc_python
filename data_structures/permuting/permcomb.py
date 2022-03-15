"""permutation-type operations for sequences"""


def permute(sequence):
    if not sequence:                                        # shuffle any sequence
        return [sequence]                                   # empty sequence
    else:
        res = []
        for i in range(len(sequence)):
            rest = sequence[:i] + sequence[i+1:]            # delete current node
            for x in permute(rest):                         # permute the others
                res.append(sequence[i:i+1] + x)             # add node at front
        return res


def subset(sequence, size):
    if size == 0 or not sequence:                            # order matters here
        return [sequence[:0]]                                # an empty sequence
    else:
        result = []
        for i in range(len(sequence)):
            pick = sequence[i:i+1]                           # sequence slice
            rest = sequence[:i] + sequence[i+1:]                 # keep [:i] part
            for x in subset(rest, size-1):
                result.append(pick + x)
        return result


def combo(sequence, size):
    if size == 0 or not sequence:                            # order doesn't matter
        return [sequence[:0]]                                # xyz == yzx
    else:
        result = []
        for i in range(0, (len(sequence) - size) + 1):       # iff enough left
            pick = sequence[i:i+1]
            rest = sequence[i+1:]                            # drop [:i] part
            for x in combo(rest, size - 1):
                result.append(pick + x)
        return result


if __name__ == '__main__':
    lst = [1, 2, 3, 4]
    print(permute(lst))
