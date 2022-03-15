def reverse(seq):
    if not seq:  # empty? (not always [])
        return seq  # the same seq type
    else:
        return reverse(seq[1:]) + seq[:1]  # add front item on the end


def ireverse(seq):
    res = seq[:0]  # empty, of same type
    for i in range(len(seq)):
        res = seq[i:i + 1] + res  # add each item to front
    return res


if __name__ == '__main__':
    lst = [1, 2, 3, 4]
    print(reverse("asd"))
