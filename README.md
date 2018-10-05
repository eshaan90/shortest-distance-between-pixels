# ImageProcessingProjects-Python
A collection of interesting projects I did in the Image processing domain. 


convolutions.py- This file implements the convolution of a predefined kernel with an image using numpy only. It also implements the padding operation on the image before it is convolved.  

Inputs: 
Image
Output Shape= ['same','valid','full']
Pad Types= ['constant', 'wrap' , 'edge', 'reflect']
Kernel options= {1:'sobel',2:'laplacian'}

Output: The filtered image along with the new dimensions of the image. 



pixel_shortest_path.py- Here we compute the shortest path between two pixels using three different distance measures, namely 4-adjacency, 8-adjacency, and m-adjacency measures.

