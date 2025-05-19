import networkx as nx
import matplotlib.pyplot as plt


G = nx.Graph()

# Add edges with weights (weight could be, e.g., NCC score)
G.add_edge('A', 'B', weight=3)
G.add_edge('A', 'D', weight=5)
G.add_edge('A', 'E', weight=9)
G.add_edge('B', 'C', weight=5)
G.add_edge('B', 'D', weight=4)
G.add_edge('B', 'E', weight=8)
G.add_edge('C', 'D', weight=7)
G.add_edge('C', 'G', weight=3)
G.add_edge('D', 'F', weight=8)
G.add_edge('D', 'G', weight=5)
G.add_edge('D', 'H', weight=6)
G.add_edge('E', 'F', weight=2)
G.add_edge('F', 'H', weight=10)
G.add_edge('G', 'I', weight=1)
G.add_edge('H', 'I', weight=3)

# Use networkx's minimum_spanning_tree method (Kruskal by default)
mst = nx.minimum_spanning_tree(G)

print("Edges in MST with weights:")
for u, v, data in mst.edges(data=True):
    print(f"{u} - {v}: {data['weight']}")
# Positions for all nodes (spring layout for nice spacing)
pos = nx.spring_layout(G, seed=42)  # fixed seed for reproducibility

plt.figure(figsize=(12, 6))

# Draw original graph in light gray
nx.draw(G, pos, with_labels=True, node_color='lightblue', node_size=600, edge_color='lightgray')

# Draw edge labels (weights)
edge_labels = nx.get_edge_attributes(G, 'weight')
nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)

# Highlight MST edges in red and thicker
nx.draw_networkx_edges(G, pos, edgelist=mst.edges(), edge_color='red', width=3)

plt.title("Graph with Minimum Spanning Tree (MST) Highlighted in Red")
plt.axis('off')
plt.show()