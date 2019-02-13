# Interpreting Image as Graphs and computing the shortest distance between pixels 

Here we compute the shortest path between two pixels using three different distance measures, namely 4-adjacency, 8-adjacency, and m-adjacency measures. 

The pixels are first mapped into undirected graphs where each pixels is a graph node and the connections are formed based on the type of adjacency measure selected. 

Thereafter, the shortest path between two pixels is found using Breadth First search algorithms. Other algorithms that can also be used for finding the shortest path are Djikstra's, A*, etc. 



#Dependencies used: 
#numpy: to load the image segment 
#opencv(cv2): needed only if image needs to be imported. 
#time: to record the time taken to find the shortest path.

## How To Run:

To load an image or change the image segment, head over down to the main function block and change the value of pixel_arr.

To change the start and end locations of the pixels, again, change p and q values (location of the two pixels) respectively in the main function block. Same goes for changing the predefined set V. 
