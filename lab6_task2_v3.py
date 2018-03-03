
from lab6_functions import*

# task 2a: 
# --------
# 
# implementation of shortest path algorithm

# create an empty network object
network = Network()
network1 = Network()
network2 = Network()
# read the network
network.read_network('test.txt')
network1.read_network('test1.txt')
network2.read_network('network.txt')
# determine the shortest path between first and last nodes
# 	** you will need to complete the function DIJKSTRA in lab2_functions.py **
distance, shortest_path = dijkstra(network1, network1.nodes[-2], network1.nodes[0])
print(distance,shortest_path)
distance, shortest_path = dijkstra(network1, network1.nodes[-2], network1.nodes[1])
print(distance,shortest_path)
distance, shortest_path = dijkstra(network1, network1.nodes[-2], network1.nodes[2])
print(distance,shortest_path)
distance, shortest_path = dijkstra(network1, network1.nodes[-2], network1.nodes[3])
print(distance,shortest_path)
distance, shortest_path = dijkstra(network1, network1.nodes[-2], network1.nodes[4])
print(distance,shortest_path)
distance, shortest_path = dijkstra(network1, network1.nodes[-2], network1.nodes[5])
print(distance,shortest_path)
distance, shortest_path = dijkstra(network1, network1.nodes[-2], network1.nodes[6])
print(distance,shortest_path)



distance, shortest_path = dijkstra(network, network.nodes[0], network.nodes[-1])
print(distance,shortest_path)
distance, shortest_path = dijkstra(network, network.nodes[0], network.nodes[-2])
print(distance,shortest_path)
distance, shortest_path = dijkstra(network, network.nodes[0], network.nodes[-3])
print(distance,shortest_path)
distance, shortest_path = dijkstra(network, network.nodes[0], network.nodes[-4])
print(distance,shortest_path)
distance, shortest_path = dijkstra(network, network.nodes[0], network.nodes[-5])
print(distance,shortest_path)
distance, shortest_path = dijkstra(network, network.nodes[0], network.nodes[-6])
print(distance,shortest_path)
distance, shortest_path = dijkstra(network, network.nodes[0], network.nodes[-7])
print(distance,shortest_path)
# asserts check the network algorithm passes





distance, shortest_path = dijkstra(network2, network2.nodes[0], network2.nodes[-1])
print(distance,shortest_path)
assert(distance == 7)
assert(all([p1==p2 for p1,p2 in zip(shortest_path, ['A','B','C','E','F'])]))

print("assert true")

# task 2b: 
# --------
#
# sketch the network and consider the two paths A-B-C-E-F and A-B-C-D-F
# comment and identify a shortingcoming of your implementation of Dijkstra's method
