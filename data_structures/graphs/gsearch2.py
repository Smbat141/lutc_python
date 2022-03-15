"""graph search, using paths stack instead of recursion"""


def search(start, goal, graph):
    solns = generate(([start], []), goal, graph)
    solns.sort(key=lambda x: len(x))
    return solns


def generate(paths, goal, graph):  # returns solns list
    solns = []  # use a tuple-stack
    while paths:
        front, paths = paths  # pop the top path
        state = front[-1]
        if state == goal:
            solns.append(front)  # goal on this path
        else:
            for arc in graph[state]:  # add all extensions
                if arc not in front:
                    paths = (front + [arc]), paths
    return solns


if __name__ == '__main__':

    Graph = {'A': ['B', 'E', 'G'],
             'B': ['C'],  # a directed, cyclic graph
             'C': ['D', 'E'],  # stored as a dictionary
             'D': ['F'],  # 'key' leads-to [nodes]
             'E': ['C', 'F', 'G'],
             'F': [],
             'G': ['A']}

    for x in ['AG']:
        print(search(x[0], x[1], Graph))
