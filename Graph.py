import networkx as nx
import matplotlib.pyplot as plt

def print_bipartite_graph(bipartite_graph):
    G = nx.Graph()

    # Add nodes from both sets
    G.add_nodes_from(bipartite_graph.keys(), bipartite=0)  # Bipartite attribute 0 for the row set
    G.add_nodes_from(set(v for neighbors in bipartite_graph.values() for v in neighbors), bipartite=1)  # Bipartite attribute 1 for the column set

    # Add edges
    for node, neighbors in bipartite_graph.items():
        G.add_edges_from((node, neighbor) for neighbor in neighbors)

    # Create a bipartite layout
    pos = {node: (0, i) for i, node in enumerate(bipartite_graph.keys())}
    pos.update({node: (1, i) for i, node in enumerate(set(v for neighbors in bipartite_graph.values() for v in neighbors))})

    # Print the bipartite graph
    print("Bipartite Graph:")
    print("Nodes:")
    print(G.nodes(data=True))
    print("Edges:")
    print(G.edges())
    
    # Draw and display the graph (optional)
    nx.draw(G, pos, with_labels=True, font_weight='bold')
    plt.show()

# Example usage:
matrix_example = [
    [1, 0, 0,0],
    [0, 0, 0,1],
    [0, 1, 0,0],
    [0 ,0 ,1,0]
]
def matrix_to_bipartite_graph(matrix):
    row_set = len(matrix)
    col_set = len(matrix[0])

    # Create two sets of vertices
    rows = set(range(row_set))
    cols = set(range(col_set))

    # Initialize an empty bipartite graph
    bipartite_graph = {i: [] for i in range(row_set)}

    # Iterate through the matrix and add edges to the bipartite graph
    for i in range(row_set):
        for j in range(col_set):
            if matrix[i][j] == 1:  # Assuming 1 represents the presence of an edge
                bipartite_graph[i].append(j)

    return bipartite_graph

bipartite_graph_example = matrix_to_bipartite_graph(matrix_example)
print_bipartite_graph(bipartite_graph_example)