# Código realizado no Colab
# Usar o NetworkX para construir um grafo do andar do prédio em que ocorre essa aula.

import networkx as nx
import matplotlib.pyplot as plt
import numpy as np

G = nx.Graph()

# O primeiro andar do bloco A vai da sala 17 a 36
G.add_nodes_from([17, 36])

edges_lists = [
    (17, 18), (18, 19), (19, 20), (20, 21), (21, 22), (22, 23), (23, 24), (24, 25), 
     (25, 26), (26, 27), (27, 28), (28, 29), (29, 30), (30, 31), (31, 32), (32, 33),
     (33, 34), (34, 35), (35, 36), (17, 36)
    ]

G.add_edges_from(edges_lists)

V = list(G.nodes)
print("V = "+ str(V))

A = list(G.edges)
print("A = " + str(A))

nx.draw(G, with_labels=True)
plt.show()