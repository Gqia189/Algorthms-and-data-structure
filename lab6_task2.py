
from lab6_functions import*

# task 2a: 
# --------
# 
# implementation of shortest path algorithm

# create an empty network object
network = Network()

# read the network
network.read_network('network.txt')

# determine the shortest path between first and last nodes
# 	** you will need to complete the function DIJKSTRA in lab2_functions.py **
destination = dijkstra(network, network.nodes[0], network.nodes[-1])

# asserts check the network algorithm passes
assert(destination.dist == 7)
assert(all([p1==p2 for p1,p2 in zip(destination.path, ['A','B','C','E','F'])]))


# task 2b: 
# --------
#
# sketch the network and consider the two paths A-B-C-E-F and A-B-C-D-F
# comment and identify a shortingcoming of your implementation of Dijkstra's method
