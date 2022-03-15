"""find all paths from start to goal in graph"""


def search(start, goal, graph):
    solns = []
    generate([start], goal, solns, graph)  # collect paths
    solns.sort(key=lambda x: len(x))  # sort by path length
    return solns


def generate(path, goal, solns, graph):
    state = path[-1]
    if state == goal:  # found goal here
        solns.append(path)  # change solns in-place
    else:  # check all arcs here
        for arc in graph[state]:  # skip cycles on path
            if arc not in path:
                generate(path + [arc], goal, solns, graph)


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
