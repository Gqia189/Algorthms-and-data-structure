# task 2b: 
# --------
#
# sketch the network and consider the two paths A-B-C-E-F and A-B-C-D-F
# comment and identify a shortingcoming of your implementation of Dijkstra's method

"""
A ------2----- B
 \            /\
  \          /  \
   \        /    \
    4      1      4
     \	  /        \
      \  /          \
       \/            \
        C -----2----- D
         \            /\
          \          /  \
           \        /    \
            1      2      2
             \    /        \
              \  /          \
               \/            \
                E -----4----- F

The path A-B-C-E-F has a distance of 2+1+1+3 = 7 
The path A-B-C-D-F has a distance of 2+1+2+2 = 7
From examining the network above, we can see that both paths listed above have the distance 7. Therefore, are both minimum paths from A to F.
However, in my implementation of the dijkstra's algorithm, only one of these paths will be returned. Namely only the path A-B-C-D-F will be returned.
This is because my goes through every node in the network in the order increasing distance away from source. And at every node it will chose to update
the dist and preceding_node attributes of the to_nodes that the arcs_out from the source points to. 
If to_node.dist is larger than the current_node.dist + arc.weight, then it will update to the new shortest distance, and also update the preceding node aswell.
However, if the distances are equal then it will not update, and dist and preceding_node attributes. 
This shortcoming in my implementation results in only one shortest path is returned when function is run. 

In my code, I also did some tests for edge cases. For these cases I have chosen
to return a distance of infinity and a empty path [], as this signifies that there is not path from the source to destination.  
Another shortcoming in my code is that I may have not considered every edge case possible. 

"""