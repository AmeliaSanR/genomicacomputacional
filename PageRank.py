
import networkx as nx

# Crear un grafo dirigido
G = nx.DiGraph()

# Añadir nodos y aristas (metabolitos y reacciones)
G.add_edges_from([
    ('A', 'B'),  # Reacción de A a B
    ('B', 'C'),  # Reacción de B a C
    ('A', 'C'),  # Reacción de A a C
    ('C', 'D'),  # Reacción de C a D
    ('D', 'A'),  # Reacción de D a A
    ('C', 'E'),  # Reacción de C a E
])

# Calcular PageRank
pagerank_scores = nx.pagerank(G)

# Mostrar los resultados
for node, score in pagerank_scores.items():
    print(f"Node: {node}, PageRank Score: {score}")
