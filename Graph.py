INDIRECTED GRAPH:

import networkx as nx
g = nx.Graph()
h = nx.Graph()
g.add_nodes_from(range(1,4))
h.add_nodes_from(range(4,8))
g.add_nodes_from(g)
g.add_edges_from([(1,2),(2,3),(3,1)])
h.add_edges_from([(4,5),(5,6),(6,7),(4,7),(1,4),(3,5)])
g.add_edges_from(h.edges())
nx.draw_networkx(g)

DIRECTED GRAPH:

import networkx as nx
g = nx.DiGraph()
g.add_nodes_from(range(1,6))
g.add_edges_from([[1,2],[2,3],[2,4],[2,5],[3,4],[4,5]])
color=['y','g','b','m','r']
shape='*'
l={1:'Start',2:'',3:'',4:'',5:'End'}
nx.draw_networkx(g,node_color=color,node_shape=shape,node_size=2000,with_labels=T
m1 = nx.adjacency_matrix(g)
print(m1)
m2 = m1.todense()
print(m2)