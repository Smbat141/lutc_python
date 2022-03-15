"""build graph with objects that know how to search"""


class Graph:
    def __init__(self, label, extra=None):
        self.name = label  # nodes=inst objects
        self.data = extra  # graph=linked objs
        self.arcs = []

    def __repr__(self):
        return self.name

    def search(self, goal):
        Graph.solns = []
        self.generate([self], goal)
        Graph.solns.sort(key=lambda x: len(x))
        return Graph.solns

    def generate(self, path, goal):
        if self == goal:  # class == tests addr
            Graph.solns.append(path)  # or self.solns: same
        else:
            for arc in self.arcs:
                if arc not in path:
                    arc.generate(path + [arc], goal)


if __name__ == '__main__':

    "build class-based graph and run test searches"

    # this doesn't work inside def in 3.1: B undefined
    for name in "ABCDEFG":  # make objects first
        exec("%s = Graph('%s')" % (name, name))  # label=variable-name

    A.arcs = [B, E, G]
    B.arcs = [C]  # now configure their links:
    C.arcs = [D, E]  # embedded class-instance list
    D.arcs = [F]
    E.arcs = [C, F, G]
    G.arcs = [A]

    print(A.search(G))
    print(C.search(A))

    # for (start, stop) in [(E, D), (A, G), (G, F), (B, A), (D, A)]:
    #     print(start.search(stop))
