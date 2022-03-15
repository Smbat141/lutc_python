def sort(list, field):
    res = []                                     # always returns a list
    for x in list:
        i = 0
        for y in res:
            if x[field] <= y[field]: break       # list node goes here?
            i += 1
        res[i:i] = [x]                           # insert in result slot
        # res.insert(i,x)                        # or this way

    return res


if __name__ == '__main__':
    table = [{'name': 'john', 'age': 25}, {'name': 'doe', 'age': 32}, {'name': 'doe', 'age': 50},
             {'name': 'doe', 'age': 3}]
    print(sort(table, 'age'))
    # print(sort(table, 'name'))
    # table = [ ('john', 25), ('doe', 32) ]
    # print(sort(table, 0))
    # print(sort(table, 1))
