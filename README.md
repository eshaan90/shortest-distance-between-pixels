# ImageProcessingProjects-Python
A collection of interesting projects I did in the Image processing domain. 

_____________________________________________________________________________________________________________________________
Convolutions with Padding- This project implements convolution of various filter kernels with an image using only numpy as dependency. It also implements the padding operation on the image before it is convolved.  


Inputs: 

Image
Output Shape= ['same','valid','full']

Pad Types= ['constant', 'wrap' , 'edge', 'reflect']

Kernel options= {1:'sobel',2:'laplacian'}

Output: The filtered image along with the new dimensions of the image. 


_____________________________________________________________________________________________________________________________
Shortest path b/w pixels- Here we compute the shortest path between two pixels using three different distance measures, namely 4-adjacency, 8-adjacency, and m-adjacency measures. 

The pixels are first mapped into undirected graphs where each pixels is a graph node and the connections are formed based on the type of adjacency measure selected. 

Thereafter, the shortest path between two pixels is found using Breadth First search algorithms. Other algorithms that can also be used for finding the shortest path are Djikstra's, A*, etc. 

