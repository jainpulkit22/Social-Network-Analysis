import networkx as nx
import pandas as pd
from operator import itemgetter

df = pd.read_csv('p2p.csv')
Graphtype1 = nx.Graph()
G = nx.from_pandas_edgelist(df, source='Column1', target='Column2', create_using=Graphtype1)

#----------------------------------------Local Clustering Coefficient-----------------------------------

LocalClustering = nx.clustering(G)
sorted_localClustering = sorted(LocalClustering.items(),key=itemgetter(1), reverse=True)

print("Top 10 nodes with heighest Local Clustering value:")
for x in sorted_localClustering[:10]:
    print(x)

#--------------------------------------Average Clustering Coefficient-----------------------------------

AvgClustering = nx.average_clustering(G)
print("Average Clustering For p2p Network:")
print(AvgClustering)

#--------------------------------------Global Clustering Coefficient-----------------------------------

Graphtype2 = nx.DiGraph()
H = nx.from_pandas_edgelist(df, source='Column1', target='Column2', create_using=Graphtype2)

number_of_triangles = sum(nx.triangles(G).values())
number_of_triads = len(list(nx.all_triads(H)))

GlobalClustering = 3*(number_of_triangles)/number_of_triads
print("Global Clustering for p2p Network:")
print(GlobalClustering)
