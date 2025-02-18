# Código realizado no Colab
# Crie um gráfico baseado na imagem do material com pelo menos 15 pontos do grafo

# Bibliotecas
import networkx as nx
import matplotlib.pyplot as plt
import numpy as np

G = nx.Graph()

nodes_list = [
    "Reboleira", "Alfornelos", "Amadora-Este", "Pontinha", "Camide", "Colégio Militar",
    "Alto dos Moinhos", "Jardim Zoológico", "Laranjeiras", "Praça da Espanha", "São Sebastião",
    "Saldanha", "Parque", "Avenida", "Restauradores", "Picoas", "Ratos"
    ]

G.add_nodes_from(nodes_list)

edges_lists = [
    ("Reboleira", "Alfornelos"), ("Alfornelos", "Amadora-Este"), ("Amadora-Este", "Pontinha"),
    ("Pontinha", "Camide"), ("Camide", "Colégio Militar"), ("Colégio Militar", "Alto dos Moinhos"),
    ("Alto dos Moinhos", "Laranjeiras"), ("Laranjeiras", "Jardim Zoológico"), ("Jardim Zoológico", "Praça da Espanha"),
    ("Praça da Espanha", "São Sebastião"), ("São Sebastião", "Saldanha"), ("São Sebastião", "Parque"),
    ("Parque", "Avenida"), ("Avenida", "Restauradores")
]

G.add_edges_from(edges_lists)

V = list(G.nodes)
print("V = "+ str(V))

A = list(G.edges)
print("A = " + str(A))

nx.draw(G, with_labels=True)
plt.show()