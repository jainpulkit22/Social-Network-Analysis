import networkx as nx
import pandas as pd

df = pd.read_csv('p2p.csv')
Graphtype = nx.DiGraph()
G = nx.from_pandas_edgelist(df, source='Column1', target='Column2', create_using=Graphtype)

print("Reciprocity of the graph: ", nx.reciprocity(G))