import networkx as nx
import matplotlib.pyplot as plt

# Load the network data
G = nx.gnm_random_graph(50, 250)

# Draw the graph
nx.draw(G, with_labels=True)
plt.show()

# Compute network properties
def compute_properties(G):
    # Number of nodes and edges
    n_nodes = G.number_of_nodes()
    n_edges = G.number_of_edges()
    print(f"Number of nodes: {n_nodes}")
    print(f"Number of edges: {n_edges}")

    # Average degree
    avg_degree = 2 * n_edges / n_nodes
    print(f"Average degree: {avg_degree}")

    # Density
    density = 2 * n_edges / (n_nodes * (n_nodes - 1))
    print(f"Density: {density}")

    # Diameter
    diameter = nx.diameter(G)
    print(f"Diameter: {diameter}")

    # Clustering coefficient
    clustering_coefficients = nx.clustering(G)
    avg_clustering_coefficient = sum(clustering_coefficients.values()) / n_nodes
    print(f"Average Clustering Coefficient: {avg_clustering_coefficient}")

compute_properties(G)
