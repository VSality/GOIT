
import numpy as np
import networkx as nx

G = nx.Graph()
# G = nx.DiGraph()

# G.add_node('A')
# G.add_nodes_from(['B', 'C', 'D'])
# G.add_edge('A', "B")
G.add_edges_from([("A", "C"), ("B", "C"), ("B", "D"), ("C", "B"), ("A", "F"), ('F', "G"), ('A', "G")])

# G.remove_node('A')
# G.remove_nodes_from(['B', 'C'])
# G.remove_edges_from([("A", "C")])

G.add_edge('A', 'B', weight=2.5, label='l1')

pos = nx.shell_layout(G)
labels = nx.get_edge_attributes(G, 'weight')
nx.draw(G, pos, with_labels=True)
nx.draw_networkx_edge_labels(G, pos, edge_labels=labels)

graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B', 'F'],
    'F': ['C', 'E']
}

G = nx.Graph(graph)

nx.draw(G, with_labels=True)