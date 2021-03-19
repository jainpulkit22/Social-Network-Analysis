import networkx as nx
import pandas as pd

df = pd.read_csv('facebook.csv')
Graphtype = nx.Graph()
G = nx.from_pandas_edgelist(df, source='Column1', target='Column2', create_using=Graphtype)

# group
C= [150,151,152]

# H subgraph
arr = []
for x in range(501):
	arr.append(x)
H = G.subgraph(arr)

print("Group betweenness: ", nx.group_betweenness_centrality(H,C))