from lab6_classes import*

#					-----------
def breadth_search(tree, value, verbose=False):
	''' Search TREE for integer VALUE using a breadth search.
		
		Parameters
		----------
		tree : Tree
		    The network structure to be searched.
		value : int
			Integer value to locate in the network.
			
		Returns
		-------
		node : Node
			Node object whose VALUE attribute contains the search item.
		checked : list
			Names of nodes checked up to successful search.
		
		Notes
		-----
		Index table for sort constructed by applying the same sort operations
		to INDS that are applied to A.
		
	'''
			
	# initialise the queue
	qu = LinkedList()
	qu.append(tree.head)          # first search item must be head of TREE
	
	# empty list to stored searched nodes
	checked = []
	
	# start the search
	keep_searching = True
	while keep_searching:
		# pop next node in queue (pop from the FRONT of the list)
		node = qu.pop(0)
		# update searched
		checked.append(node.name)
		
		# check if current node has VALUE
		# **hint: this is an if statement and a RETURN**
		# **see last line of function for inspiration writing your return**
		if node.value == value:
			return node, checked

		# add daughters to queue
		# **hint: use node.arcs_out attribute to find daughters**
		# **hint: the queue contains NODES, not NODE NAMES**
		else:
			for arc in node.arcs_out:
				qu.append(arc.to_node)
		

		if qu.get_length() == 0:
			keep_searching = False
	
	# if get to end of loop without finding search VALUE, return NONE
	return None, checked

#					-----------
def insertion_sort(A):
	''' Sort array A using insertion sort.
		
		Parameters
		----------
		A : array
		    Array of values to be sorted.
			
		Returns
		-------
		inds : array
			An index table for A.
		
		Notes
		-----
		Index table for sort constructed by applying the same sort operations
		to INDS that are applied to A.
		
	'''
	# initialise
	n = len(A)

	# create an array of indices corresponding to the original order of A
	inds = np.arange(n)
	
	# for each value in the array, beginning with the second 
	for j in range(1,n):
		# step - assign value to key
		# assign value to keyI
		key = A[j]
		keyI = inds[j]
		
		i = j-1
		while i> -1:
			# step - compare array values to left (of key) against key
			if not (A[i]> key):
				# condition to stop comparison
				break
			# step - shift value to the right
			# shift index to the right 
			A[i+1] = A[i]
			inds[i+1] = inds[i]
			i = i-1
		# step - insert key into new position
		# inset keyI into new position
		A[i+1] = key
		inds[i+1] = keyI
		
	return inds	

	

#                 ----------
# complete the build method to implement Step 2 "building the heap"
class Heap(Network):
	''' Derived class of NETWORK. A tree structure where each node has at most two daughters.
	'''
	# this method is complete, do not modify
	def get_node_with_value(self, value):
		''' Loops through the list of nodes and returns the one with VALUE.
		
			Returns None if node does not exist.
		'''
		for node in self.nodes:
			if node.value == value:
				return node
		
		raise NetworkError
	

	def initialise(self, A):
		''' Each of the unordered values in A is assigned as a new node in the network.
		'''
		# add first node to top of heap (head of the tree network and first item in queue)
		self.queue = LinkedList()			# use a queue to keep track of which nodes new daughters should be linked to
		self.add_node(name=0, value = A[0]) # name = node number, value = array value
		self.head = self.get_node(0)		# initialise head node
		self.queue.append(self.head)		# head node added to queue
		
		# counter to keep track of nodes added
		i = 1 								
		
		# loop to keep adding array values to the heap
		n = len(A) 	  			# length of array
		keep_adding = True		# boolean for while loop
		while keep_adding:
			# pull next node from queue: mother to (up to) two new daughter nodes
			mother = self.queue.pop(0)
			
			# add and link first daughter to the mother node
			self.add_node(name=i, value = A[i])D
			daughter = self.get_node(i)
			# join to parent
			self.join_nodes(mother, daughter, 1)
			# append the daughter to the queue
			self.queue.append(daughter)
			
			# assess stopping condition
			i += 1
			if i == n:
				keep_adding = False
				continue
  
			# add and link first daughter to mother node
			self.add_node(name=i, value = A[i])
			daughter = self.get_node(i)
			# join to parent
			self.join_nodes(mother, daughter, 1)
			# append the daughter to the queue
			self.queue.append(daughter)
			
			# assess stop condition
			i += 1
			if i == n:
				keep_adding = False
				continue


	def build(self):
		''' Completed build method.
		'''
		# loop backwards through node list, checking if demotion to daughter is warranted
		for node in self.nodes[::-1]:
			# skip node if it has no children
			if not node.arcs_out:
				continue
				
			# apply demotions
			# **hint: use a while loop to apply promotions and demotions**
			# **hint: read through the SORTED method and emulate aspects of that code**
			# Loop through and demotes to bottom
			keep_demoting = True
			while keep_demoting:
				node = self.demote(node)
				if not node:
					keep_demoting = False
			
	
	def demote(self, node):
		''' Implements iterative promotion-demotion of NODE.
		
			Parameters
			----------
			node : Node
				Node object to be demoted.
				
			Returns
			-------
			Promoted node or None.
		
			Notes
			-----
			Check node value against daughter values. If either daughter exceeds,
			the larger is promoted to NODE's position and NODE is demoted to the 
			daughter position.
		'''
		# initialise value to exceed as NODE value
		max_val = node.value
		if max_val is None:
			# if node has no value, assign exceedingly small value. Intent is to 
			# guarantee demotion of the node
			max_val = -1.e32
		# currently, not node is scheduled for promotion
		promote_node = None
		
		# check all arcs out of NODE
		for arc_out in node.arcs_out:
			# get daughter
			daughter = arc_out.to_node
			# if daughter has no value, not a candidate for promotion
			if daughter.value is None:
				continue
			# if daughter value larger than NODE or previous daughter
			if daughter.value > max_val:
				# update, new value to exceed for promotion
				max_val = copy(daughter.value)
				# schedule daughter for promotion
				promote_node = daughter
		
		# if no promotion occurs, indicate by returning False
		if promote_node is None:
			return False
		else:
			# NODE assigned value from promoted daughter, daughter assigned node value
			node.value, promote_node.value = promote_node.value, node.value
			# return promoted daughter for subsequent promotion-demotion checks
			return promote_node
	
	# this method is complete, do not modify	
	def sorted(self):
		''' Returns the sorted array by promoting values from the heap.
		
			Returns
			-------
			A sorted list of node values.
		'''
		# empty list to append sorted values
		A = []
		keep_promoting = True 					# while loop boolean
		while keep_promoting:
			# get head node
			node = self.head
			
			# condition to exit loop
			if node.value is None:
				keep_promoting = False
				continue
			
			# copy (promote) value from head node to list
			A.append(node.value)
			
			# head node value set to None and demoted
			node.value = None
			
			# loop to demote to bottom - calls DEMOTE method
			keep_demoting = True
			while keep_demoting:
				node = self.demote(node)
				if not node:
					keep_demoting = False
		
		# return sorted list
		return A
	
	def show(self):
		''' A rather long plotting method.
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
		
		gen = 1
		node = self.nodes[-1]
		keep_searching_up = True
		while keep_searching_up:
			if not node.arcs_in:
				keep_searching_up = False
			else:
				gen += 1
				node = node.arcs_in[0].from_node
		
		dx = 1./(2**gen)
		dy = 0.5
		
		still_looking=True
		current_generation = [self.head,]
		locs = {}
		generation_counter = -1
		while still_looking:
			next_generation = []
			generation_counter += 1
			xs = np.linspace(0,1,2**generation_counter+1)
			for node,x0,x1 in zip(current_generation,xs[:-1],xs[1:]):
					
				xm = 0.5*(x0+x1)
				poly = np.array([[xm-dx/2.,xm+dx/2.,xm+dx/2,xm-dx/2,xm-dx/2],[y-dy/2,y-dy/2,y+dy/2,y+dy/2,y-dy/2]]).T
				polygon = Polygon(poly, zorder=1)
				color = 'w'
				p = PatchCollection([polygon,], color = color, zorder = 1, edgecolor = 'k')
				ax.add_collection(p)
				nm = node.value
				if nm is None:
					nm = '-'
				ax.text(0.5*(x0+x1), y, '{}'.format(nm), ha='center',va='center',size=14)
				locs.update({node.name:[0.5*(x0+x1), y]})
				
				if len(node.arcs_in)>0:
					frm = node.arcs_in[0].from_node.name
					xa,ya = locs[frm]
					xb,yb = locs[node.name]
					ax.plot([xa,xb],[ya,yb],'k-', zorder = -1)
				
				# find next generation
				for arc in node.arcs_out:
					next_generation.append(arc.to_node)
				
			y = y-1
				
			if len(next_generation)>0:
				generations +=1
			else:
				still_looking = False
			
			current_generation = copy(next_generation)
			
		ax.axis('off')
		plt.show()
	

def dijkstra(network, source, destination):
	''' **description of function**
	
		Notes
		-----
		Node object has the attribute 'preceding_node', which is the preceding node in the shortest path.
	'''
	"""
	initialise 2 sets, one for solved nodes and one for unsolved nodes.
	assingn distance, d, that is a very large number, and eventually a predecessor. Except starting node

	From all nodes in unsolved set, choose node i with minimum distance d(i). Node i becomes a solved node now.In case of a tie, choose any
	list the unsolved nodes which can be reached by following a single arc out of node i.
	find the toal distance from the origin to each of the unsolved nodes j in step 2

	total distance = d(i) + weight of arc(i,j)
	if this total distance is smaller than the current distance d(j) update the distance and set predecessor of node j as node i
	stop when destination node has become solved
	"""

	# Initialise solved set
	solved = set()
	# Initialise unsolved set with all nodes in network starting in this set
	unsolved = set(network.nodes)
	# set shortest path to be infinity
	SP = float("Inf")

	# Test some edge cases
	# If source not in network
	if source not in unsolved:
		return float("Inf"), []
	# If destination not in network
	if destination not in unsolved:
		return float("Inf"), []
	# If source is not equal to destination
	# and such that there are no arcs going out of source
	# or there is no arcs going into destination
	if source != destination:
		if len(source.arcs_out) == 0:
			return float("Inf"), []
		if len(destination.arcs_in) == 0:
			return float("Inf"), []


	# loop through all nodes in network and assign starting attributes
	for node in unsolved:
		node.dist = float("Inf")
		node.preceding_node = None

	# Set base case 
	source.dist = 0
	source.preceding_node = None
	

	# loop through until destination node becomes solved
	while destination not in solved:

		# Set initial shortest path to infinity
		SP = float("Inf")

		# Code for function argmin, find closest node to source
		for nodes in unsolved:

			# Update min_node if node is closer to source
			if nodes.dist <= SP: 
				SP = nodes.dist
				min_node = nodes
		
		# Add min_node into solved set 
		solved.add(min_node)
		# Remove min_node out of unsolved set
		unsolved.remove(min_node)


		# For all arcs going out of min_node
		for arc in min_node.arcs_out:

			# If there is a shorter path to the node
			if arc.to_node.dist > min_node.dist + arc.weight:
				# Upadate predecessor
				arc.to_node.preceding_node = min_node
				# Update distance
				arc.to_node.dist = min_node.dist + arc.weight


	# Final Step: extract and return path information - don't modify this section of the code
	path = [destination,]
	while path[-1].name != source.name:
		path.append(path[-1].preceding_node)	
	return destination.dist, [node.name for node in path][::-1]
