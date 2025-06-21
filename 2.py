import numpy as np
import networkx as nx
import matplotlib.pyplot as plt
import pandas as pd
import random
df = pd.read_excel('modified.xlsx')
nodes = df.iloc[:, 0].tolist()
edges = []
for index, row in df.iterrows():
    source_node = row.iloc[0]
    for i in range(1, len(row)):
        target_node = row.iloc[i]
        if pd.notnull(target_node) and source_node != target_node:
            edges.append((source_node, target_node))

#creating a digraph
G = nx.DiGraph()
#adding nodes from the list of nodes
G.add_nodes_from(nodes)

#adding edges from the list of edges
G.add_edges_from(edges)

num_nodes = G.number_of_nodes()
num_edges = G.number_of_edges()
#adj_matrix_numpy is a numpy array of zeros with the shape of num_nodes*num_nodes
adj_matrix_numpy = np.zeros((num_nodes, num_nodes))
node_numbers = {}
#iterating through the nodes of the graph
for i, node in enumerate(G.nodes()):
    node_numbers[node] = i
#iterating through the edges of the graph 
for edge in G.edges():
    #if the edge is from node i to node j then we are setting the value of adj_matrix_numpy[i][j] to 1
    adj_matrix_numpy[node_numbers[edge[0]]][node_numbers[edge[1]]] = 1
for i in range(num_nodes):
    for j in range(num_nodes):
        #if the value of adj_matrix_numpy[i][j] is 1 and adj_matrix_numpy[j][i] is 0 then we are setting the value of adj_matrix_numpy[j][i] to -1
        if adj_matrix_numpy[i][j] == 1 and adj_matrix_numpy[j][i] == 0:
            adj_matrix_numpy[j][i] = -1
pf = pd.DataFrame(adj_matrix_numpy)
file_path = "adjacency_matrix.xlsx"

adj_matrix_3=adj_matrix_numpy.copy()
for i in range(num_nodes):
    for j in range(num_nodes):
        #if the value of adj_matrix_numpy[i][j] is 0 and i is not equal to j then we are copying the adj_matrix_numpy to adj_matrix_2
        if adj_matrix_numpy[i][j] == 0 and i!=j:
            adj_matrix_2=adj_matrix_numpy.copy()
            #deleting the ith row and jth column from the adj_matrix_2
            A1 = np.delete(adj_matrix_2, i, 0)
            y=A1[:,j]
            A2 = np.delete(A1, j, 1)
            B=np.delete(adj_matrix_2[i,:],j)
            #solving the linear equation Ax=B
            x=np.linalg.lstsq(A2,B,rcond=None)[0]
            score=np.dot(x,y)
            adj_matrix_3[i][j]=score
           
#iterating over the matrix to check if the value is less than or equal to threshold value
for i in range(num_nodes):
    for j in range(num_nodes):
        if adj_matrix_3[i][j]<=0.4:
            adj_matrix_numpy[i][j]=0
        else:
            adj_matrix_numpy[i][j]=1
#swapping the keys and values of the dictionary node_numbers
node_numbers = {v: k for k, v in node_numbers.items()}
G1=nx.DiGraph()
#adding nodes from the values of the dictionary node_numbers
G1.add_nodes_from(node_numbers.values())
for i in range(num_nodes):
    for j in range(num_nodes):
        #if the value of adj_matrix_numpy[i][j] is 1 then we are adding an edge from node assigned value i to node assigned value j
        if adj_matrix_numpy[i][j]==1:
            G1.add_edge(node_numbers[i],node_numbers[j])
#printing the adjacency matrix for the graph with missing links            
print(adj_matrix_numpy)            
#drawing the graph G1            
nx.draw(G1, with_labels=True, node_size=1000, node_color='skyblue', font_size=12, arrowsize=20)
#displaying the title of the graph
plt.title('Directed Graph from Excel Sheet (Ignoring Edges to Itself or NaN)')
#displaying the graph
plt.show()
        
                