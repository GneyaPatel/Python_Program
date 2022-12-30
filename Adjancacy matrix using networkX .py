import networkx as nx
G = nx.cycle_graph(5)
A = nx.adjacency_matrix(G)
print(A.todense())
nx.draw_networkx(G)