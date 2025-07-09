def greedy_labeling(graph, order):
    k = 0
    f = {}
    Pro = {}
    possible_labeling = []
    n = len(order)

    for i in range(0, ((2*n)-1)):
        possible_labeling.append(i)

    for i in order:
        f[i] = -1

    for i in order:
        Pro[i] = []
        for neighbor in graph.neighbors(i):
            if (f[neighbor] != -1):
                Pro[i].append(f[neighbor])
                Pro[i].append(f[neighbor] - 1)
                Pro[i].append(f[neighbor] + 1)
            for neighbors_neighbor in graph.neighbors(neighbor):
                if (f[neighbors_neighbor] != -1):
                    Pro[i].append(f[neighbors_neighbor])
        f[i] = min([x for x in possible_labeling if x not in Pro[i]])

        k = max(f[i], k)
    return k