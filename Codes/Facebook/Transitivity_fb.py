import networkx as nx
import pandas as pd

df = pd.read_csv('facebook.csv')
Graphtype = nx.DiGraph()
G = nx.from_pandas_edgelist(df, source='Column1', target='Column2', create_using=Graphtype)

print("Transitivity of the graph: ", nx.transitivity(G))