
# imports
from lab6_functions import*
from collections import OrderedDict as OD

# task 1a: implement breadth search using Linked List as a queue
# --------
#
# complete the function BREADTH_SEARCH in lab6_functions.py
# and ensure you pass the assert below
	
# define a tree (same as in combinatorics Jupyter notebook)
tree_tuple = ('A',(
				('B',(
					('D',None),
					('E',None),
					('F',None)
						)
					),
				('C',(
					('G',None),
					('H',None)
						)
					)
				)
			)
	
tree=Tree()
tree.build(tree_tuple)

# assign values to the tree
tree_vals = {'A':2,'B':-1,'D':3,'E':0,'F':-2,'C':1,'G':-3,'H':4}
tree.assign_values(tree_vals)

# this command prints a picture of the TREE
#tree.show()

# call breadth search
node, checked_order = breadth_search(tree, value = -3)

# assert to pass
assert(all([a==b for a,b in zip(checked_order, ['A','B','C','D','E','F','G'])]))





# task 1b: modify insertion sort to output an index table
# --------
#
# modify the function INSERTION_SORT in lab6_functions.py
# and ensure you pass the asserts below

# define an unsorted list
A = [5, 3, 7, 1, 2]
A1 = copy(A)
A3 = np.sort(A) 		# sort the list using Python built-ins

# call insertion sort method and return index table
inds = insertion_sort(A1)

# use index table to sort second copy of the list
A2 = list(np.array(A)[inds])

# asserts to pass
assert(all([a1==a2 for a1,a2 in zip(A1,A2)]))
assert(all([a1==a3 for a1,a3 in zip(A1,A3)]))





# task 1c: implement a heap search
# --------
#
# complete the BUILD method as part of the HEAP class in lab6_functions.py 
# and ensure you pass the assert below

# list to sort in descending order
A = [2,4,3,6,7,9,8,1,5,10]
A1 = np.flipud(np.sort(A)) 	 	# sort using Python built-ins

# construct heap and initialise with unsorted list
heap = Heap()                             
heap.initialise(A)

# this command prints a picture of the HEAP
#heap.show()

# build the heap, you need to complete this method
heap.build() 

# this command prints a picture of the HEAP
#heap.show()


# extract the sorted list
A2 = heap.sorted()

# assert to pass
assert(all([a1==a2 for a1,a2 in zip(A1,A2)]))
	
	
