from copy import copy
import numpy as np
from matplotlib import pyplot as plt
from matplotlib.patches import Polygon
from matplotlib.collections import PatchCollection
	
# classes used for Lab 6, do not modify:
# --- for linked lists
class ListNode(object):
	'''A class with methods for node object.
	'''
	def __init__(self, value, pointer):
		'''Initialise a new node with VALUE and POINTER
		'''
		self.value = value
		self.pointer = pointer
		
	def __repr__(self):
		return "nd: {}".format(self.value)
		
	def next(self):
		'''Returns the next node.
		'''
		return self.pointer
class LinkedList(object):
	'''A class with methods to implement linked list behavior.
	'''
	def __init__(self):
		'''Initialise an empty list.
		'''
		self.head = None
	def __repr__(self):
		'''Print out values in the list.
		'''
		# special case, the list is empty
		if self.head is None:
			return '[]'
		
		# print the head node
		ret_str = '['					   # open brackets
		node = self.head
		ret_str += '{}, '.format(node.value) # add value, comma and white space
		
		# print the nodes that follow, in order
		while node.pointer is not None:	 # stop looping when reach null pointer
			node = node.next()			  # get the next node
			ret_str += '{}, '.format(node.value)
		ret_str = ret_str[:-2] + ']'		# discard final white space and comma, close brackets
		return ret_str
	def append(self, value):
		'''Insert a new node with VALUE at the end of the list.
		'''
		# insert value at final index in list		
		self.insert(self.get_length(), value)
	def insert(self, index, value):
		'''Insert a new node with VALUE at position INDEX.
		'''
		# create new node with null pointer
		new_node = ListNode(value, None)
		
		# special case, inserting at the beginning
		if index == 0:
			# new node points to old head
			new_node.pointer = self.head
			# overwrite list head with new node
			self.head = new_node
			return
		
		# get the node immediately prior to index
		node = self.get_node(index-1)
		
		# logic to follow
		if node is None:					# special case, out of range
			print("cannot insert at index {:d}, list only has {:d} items".format(index, self.get_length()))
		elif node.next() is None:		   # special case, inserting as last node
			node.pointer = new_node
		else:
			# point new node to node after new node
			new_node.pointer = node.next()
			# node before new node points to new node
			node.pointer = new_node
	def pop(self, index):
		'''Delete node at INDEX and return its value.
		'''
		# special case, index == 0 (delete head)
		if index == 0:
			# popped value
			pop = self.head.value
			# set new head as second node
			self.head = self.head.next()
			return pop
		
		# get the node immediately prior to index
		node = self.get_node(index-1)
		
		# logic to follow
		if node is None:					# special case, out of range
			print("cannot access index {:d}, list only has {:d} items".format(index, self.get_length()))
			return None
		elif node.next() is None:		  # special case, out of range
			print("cannot access index {:d}, list only has {:d} items".format(index, self.get_length()))
			return None
		elif node.next().next() is None:  # special case, deleting last node
			# popped value
			pop = node.next().value
			
			# make prior node the last node
			node.pointer = None
		else:
			# popped value
			pop = node.next().value
			
			# set this nodes pointer so that it bypasses the deleted node
			node.pointer = node.next().next()
		
		return pop
	def delete(self,index):
		'''Delete node at INDEX.		
		'''
		# use pop method and discard output
		self.pop(index)
	def get_length(self):
		'''Return the length of the linked list.
		'''
		# special case, empty list
		if self.head is None:
			return 0
		
		# initialise counter
		length = 1
		node = self.head
		while node.pointer is not None:
			node = node.next()
			length += 1
			
		return length
	def print(self):
		print(self)
	def get_node(self, index):
		'''Return the node at INDEX.
		'''
		# special case: index = -1, retrieve last node
		if index == -1:
			# begin at head
			node = self.head
			
			# loop through until Null pointer
			while node.pointer is not None:
				node = node.next()
			return node
		
		# begin at head, use a counter to keep track of index
		node = self.head
		current_index = 0
		
		# loop through to correct index
		while current_index < index:
			node = node.next()
			if node is None:
				return node
			current_index += 1
			# optional screen output
		return node
	def get_value(self, index):
		'''Return the value at INDEX.
		'''
		# get the node at INDEX
		node = self.get_node(index)
		
		# return its value (special case if node is None)
		if node is None:
			return None
		else: 
			return node.value
# --- for networks
class Node(object):
	def __init__(self):
		self.name = None
		self.value = None
		self.arcs_in = []
		self.arcs_out = []
		self.path = None
		self.distance = None
	def __repr__(self):
		return "nd: {}".format(self.name)
class Arc(object):
	def __init__(self):
		self.weight=None
		self.to_node = None
		self.from_node = None
	def __repr__(self):
		if self.to_node is None:
			to_nd = 'None'
		else:
			to_nd = self.to_node.name
		if self.from_node is None:
			from_nd = 'None'
		else:
			from_nd = self.from_node.name
		return "arc: {}->{}".format(from_nd, to_nd)
class NetworkError(Exception):
	'''An error to raise when violations occur.
	'''
	pass
class Network(object):
	''' Basic network class.
	'''
	def __init__(self):
		self.nodes = []
		self.arcs = []
	
	def __repr__(self):
		return ("ntwk(" + ''.join([len(self.nodes)*'{},'])[:-1]+")").format(*[nd.name for nd in self.nodes])
	
	def add_node(self, name, value=None):
		'''Adds a Node with NAME and VALUE to the network.
		'''
		# check node names are unique
		network_names = [nd.name for nd in self.nodes]
		if name in network_names:
			raise NetworkError
		
		# new node, assign values, append to list
		node = Node()
		node.name = name
		node.value = value
		self.nodes.append(node)
		
	def join_nodes(self, node_from, node_to, weight):
		'''Adds an Arc joining NODE_FROM to NODE_TO with WEIGHT.
		'''
		# new arc
		arc = Arc()
		arc.weight = weight
		arc.to_node = node_to
		arc.from_node = node_from
		# append to list
		self.arcs.append(arc)
		# make sure nodes know about arcs
		node_to.arcs_in.append(arc)
		node_from.arcs_out.append(arc)

	def read_network(self, filename):
		'''Read data from FILENAME and construct the network.
		'''
		# **to do**
		fp = open(filename, 'r')
		
		# get first line
		ln = fp.readline().strip()
		while ln is not '':
			# node name
			ln2 = ln.split(',')
			from_node_name = ln2[0]
			arcs = ln2[1:]
			# if node doesn't exist, add to network
			try:
				self.get_node(from_node_name)
			except NetworkError:
				self.add_node(from_node_name)
			# get from node
			from_node = self.get_node(from_node_name)
			
			# read arcs
			for arc in arcs:
				to_node_name, weight = arc.split(';')
				weight = int(weight)
				
				# check if to_node defined
				try:
					self.get_node(to_node_name)
				except NetworkError:
					self.add_node(to_node_name)
				
				# get to node
				to_node = self.get_node(to_node_name)
				
				# add arc
				self.join_nodes(from_node, to_node, weight)
			
			# get next line
			ln = fp.readline().strip()
			
		fp.close()
	
	def get_node(self, name):
		''' Loops through the list of nodes and returns the one with NAME.
		
			Returns None if node does not exist.
		'''
		for node in self.nodes:
			if node.name == name:
				return node
		
		raise NetworkError
class Tree(Network):
	''' Derived class of NETWORK. There is one head node, which has daughter nodes.
		Each daughter node may have its own daughter nodes.
	'''
	def build(self, tree_tuple):
		''' Build the tree from recursive TREE_TUPLE
		
			Tuple pairs contain node name first and then either None (indicating no 
			daughters) or another tuple of the same structure.
		'''
		# check that top generation has only one member
		assert(len(tree_tuple)==2)
		
		# build a network tree recursively
		k = tree_tuple[0]
		self.add_daughter(k,tree_tuple[1],None)
		self.head = self.get_node(k)
	def add_daughter(self,name,daughters,mother):
		''' Add new node NAME, link to MOTHER, recursively add DAUGHTERS.
		'''
		# adding the new node, link to mother (unless head node)
		self.add_node(name)
		if mother is not None:
			self.join_nodes(self.get_node(mother), self.get_node(name), 1)
			
		# if additional generation information, recursively add new daughters
		if daughters is not None:
			for daughter in daughters:
				self.add_daughter(daughter[0], daughter[1], name)
	def assign_values(self, val_dict):
		''' Assigns values to nodes from VAL_DICT.
		
			Keys of VAL_DICT are node names.
		'''
		for k in val_dict.keys():
			self.get_node(k).value=val_dict[k]
	def show(self, highlight = []):
		''' Don't worry about these rather involved plotting commands.
		
			They are here to give you visual feel of the tree structure.
		'''
		# count generations
		generations = 1
		still_looking = True
		current_generation = [self.head,]
			
		while still_looking:
			next_generation = []
			for node in current_generation:
				for arc in node.arcs_out:
					next_generation.append(arc.to_node)
				
			if len(next_generation)>0:
				generations +=1
			else:
				still_looking = False
			
			current_generation = copy(next_generation)
		
		f,ax = plt.subplots(1,1)
		
		f.set_size_inches(8,generations)
		
		ax.set_xlim([0,1])
		ax.set_ylim([0,generations])
		
		y = generations-0.5
		x = [0,1]
		
		props0 = dict(boxstyle='round', facecolor='white', alpha=1.0)
		still_looking=True
		current_generation = [self.head,]
		locs = {}
		while still_looking:
			next_generation = []
			xnew = []
			for node,x0,x1 in zip(current_generation,x[:-1],x[1:]):
				# plot
				props = copy(props0)
				if node.name in highlight:
					props['facecolor']=[1,0.8,1]
					
				ax.text(0.5*(x0+x1), y, '{}: {}'.format(node.name, node.value), ha='center',va='center',bbox=props,size=14)
				locs.update({node.name:[0.5*(x0+x1), y]})
				
				if len(node.arcs_in)>0:
					frm = node.arcs_in[0].from_node.name
					xa,ya = locs[frm]
					xb,yb = locs[node.name]
					ax.plot([xa,xb],[ya,yb],'k-')
				
				# find next generation
				for arc in node.arcs_out:
					next_generation.append(arc.to_node)
				
				xnew += list(np.linspace(x0,x1,len(node.arcs_out)+1))[:-1]
				
			y = y-1
			xnew += [x1,]
				
			if len(next_generation)>0:
				generations +=1
			else:
				still_looking = False
			
			current_generation = copy(next_generation)
			x = copy(xnew)
			
		ax.axis('off')
		plt.show()