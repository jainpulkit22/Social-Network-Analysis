import networkx as nx
import pandas as pd

df = pd.read_csv('p2p.csv')
Graphtype = nx.Graph()
G = nx.from_pandas_edgelist(df, source='Column1', target='Column2', create_using=Graphtype)

print("No of Nodes in the network: ", G.number_of_nodes())
largest_cc = max(nx.connected_components(G), key=len)

print("Size of the largest component: ", len(largest_cc))

arr = []
for i in range(8847):
    if i not in largest_cc:
        arr.append(i)

print("Nodes that are not part of the largest component: ", arr)

