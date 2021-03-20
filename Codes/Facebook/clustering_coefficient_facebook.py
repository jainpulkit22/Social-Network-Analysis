import networkx as nx
import pandas as pd
from operator import itemgetter

df = pd.read_csv('facebook.csv')
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
print("Average Clustering For facebook Network:")
print(AvgClustering)
