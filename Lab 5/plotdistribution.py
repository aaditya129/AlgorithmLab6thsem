
import matplotlib.pyplot as plt
import networkx as nx

G = nx.gnm_random_graph(50, 250)

def plot_degree_distribution(G):
    degrees = [G.degree(n) for n in G.nodes()]
    plt.hist(degrees, bins=50)
    plt.xlabel("Degree")
    plt.ylabel("Number of nodes")
    plt.title("Degree distribution")
    plt.show()

plot_degree_distribution(G)