import networkx as nx
import matplotlib.pyplot as plt
import random

N = 100

G = nx.scale_free_graph(N)

nx.draw_random(G, with_labels = True)
plt.savefig("fig1.png")


def getProbabilityMatrix():
    probability_matrix = [ [ 0 for i in range(N) ] for j in range(N) ]
    for node in G.nodes():
        outedges = G.out_edges(node)
        neighbor = {}
        sum = 0
        for j in outedges:
            if (j[0] != j[1] and probability_matrix[node][j[1]] == 0):
                x = random.random()
                sum = sum + x
                neighbor[j[1]] = x
                probability_matrix[node][j[1]] = -1
        for key in neighbor:
            probability_matrix[node][key] = float(neighbor[key]/sum)
    return probability_matrix

def getRandomSeedSet(k):
    seed_set = list()
    for i in range(k):
        seed_set.append(random.randint(0,N-1))
    return seed_set

def ICM_util(seed_set, probability_matrix):
    queue = []
    res = []
    for i in seed_set:
        queue.append(i)
        res.append(i)
    t = 0
    while queue:
        new_q = []
        while queue:
            x = queue.pop(0)
            for j in G.out_edges(x):
                visited = list()
                if (j[0] != j[1] and not j[1] in visited and not j[1] in res and not j[1] in new_q):
                    visited.append(j[1])
                    p = random.random()
                    if p <= probability_matrix[x][j[1]]:
                        new_q.append(j[1])
        if not new_q:
            break
        queue = new_q
        t = t + 1
        for e in new_q:
            res.append(e)
    print("Activated Nodes - " + str(res))
    print("Number of Steps - " + str(t))
    return t


def ICM(seq):
    seed_set = getRandomSeedSet(random.randint(5,20))
    probability_matrix = getProbabilityMatrix()
    print("Seed Set " + str(seq+1) + " - " + str(seed_set))
    max_steps = ICM_util(seed_set, probability_matrix)

for i in range(5):
    ICM(i)
    print("\n")
