#importing the libraries 
import pandas as pd
import networkx as nx
import matplotlib.pyplot as plt
import random
import numpy as np
#reading the excel file 
df = pd.read_excel('modified.xlsx')
nodes = df.iloc[:, 0].tolist()
edges = []
for index, row in df.iterrows():
    #getting the source node
    source_node = row.iloc[0]
    #iterating through the rows of the dataframe
    for i in range(1, len(row)):
        #getting the target node
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
def random_walk(graph):
    #taking the number of steps as 1000000 and initializing the start node as None 
    numsteps=1000000
    startnode=None
    #if the startnode is none then we are choosing a random node from the list of nodes
    if startnode is None:
        startnode = random.choice(list(graph.nodes()))
    currentnode = startnode
    #initializing the nodecounts dictionary with the nodes as keys and 0 points as values
    nodecounts = {node: 0 for node in graph.nodes()}
    #iterating through the number of steps
    for _ in range(numsteps):
        #getting the neighbors of the current node
        neighbors = list(graph.successors(currentnode))
        #if the length of the neighbors is not 0 then we are choosing a random node from the neighbors
        #if the random number is less than or equal to 0.85 then we are choosing a random node from the neighbors
        if neighbors and random.uniform(0, 1) <= 0.85:
            nextnode = random.choice(neighbors)
        else:
            nextnode = random.choice(list(graph.nodes()))
        #incrementing the points of the next node by 1
        nodecounts[nextnode] += 1
        currentnode = nextnode
    #calculating the values for the nodes in this pagerank    
    pagerank = {node: count / numsteps for node, count in nodecounts.items()}
    return pagerank
#calling the random_walk function
RWpoints=random_walk(G)
#sorting the dictionary in descending order
RWsorted=sorted(RWpoints.items(),key=lambda x:x[1], reverse=True)
ll=[]
for i in RWsorted:
    ll.append(i[0])
#printing the list of nodes in descending order of their points    
print(ll)
 


