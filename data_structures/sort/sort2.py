def sort(seq, func=(lambda x,y: x <= y)):             # default: ascending
    res = seq[:0]                                     # return seq's type
    for j in range(len(seq)):
        i = 0
        for y in res:
            if func(seq[j], y): break
            i += 1
        res = res[:i] + seq[j:j+1] + res[i:]          # seq can be immutable
    return res


if __name__ == '__main__':
    # table = ({'name': 'a'}, {'name': 'd'}, {'name': 'b'}, {'name': 'c'}, {'name': 'e'}, {'name': 'f'})

    # print(sort(list(table), (lambda x, y: x['name'] > y['name'])))

    # print(sort(tuple(table), (lambda x, y: x['name'] <= y['name'])))
    print(sort('axbyzc'))
    print(sort([[1], [55], [312], [34], [23]], (lambda x, y: x[0] > y[0])))