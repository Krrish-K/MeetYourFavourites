# -*- coding: utf-8 -*-
"""
Created on Sat Mar 28 23:15:31 2020

@author: krish
"""
import networkx as nx
import numpy
G=nx.read_edgelist("facebook_combined.txt")
N=list(G.nodes())
spll=[]
for u in N:
    for v in N:
        if(u!=v):
            l=nx.shortest_path_length(G,u,v)
            print("Shortest path between ",u," and ",v," is of length ",l)
            spll.append(l)
            
min_spl=min(spll)
max_spl=max(spll)
avg_spl=numpy.average(spll)
print("Minimum Shortest Path Length:",min_spl)
print("Maximum Shortest Path Length:",max_spl)
print("Average Shortest Path Length:",avg_spl)