#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct  3 23:07:58 2018

@author: MyReservoir
"""

#Dependencies used: 
#numpy: to load the image segment 
#opencv(cv2): needed only if image needs to be imported. 
#time: to record the time taken to find the shortest path.

#The main function block is at the bottom of this code, from where the code execution starts.
#To load an image or change the image segment, head over down to the main function block and 
#change the value of pixel_arr.

#To change the start and end locations of the pixels, again, change p and q values respectively 
#in the main function block.
#Same goes for changing the predefined set V. 

#To print the graph, uncomment the print line in the sp function. You should see the graph 
#connections printed out.



import numpy as np
import time
import cv2

class PixelNode(object):
    def __init__(self,x,y,intensity):
        self.intensity=intensity
        self.x=x
        self.y=y
    
    def getx(self):
        return self.x
    def gety(self):
        return self.y
    def getIntensity(self):
        return self.intensity

    def __str__(self):
        return '('+str(self.x)+','+str(self.y)+'):'+str(self.intensity)
    
class Edge(object):
    def __init__(self,src,dest):
        self.src=src
        self.dest=dest
    def getSource(self):
        return self.src
    def getDestination(self):
        return self.dest

    
class Digraph(object):
    def __init__(self):
        self.nodes=[]
        self.edges={}
    
    def addNode(self,node):
        if node in self.nodes:
            raise ValueError('Duplicate Node')
        else:
            self.nodes.append(node)
            self.edges[node]=[]
    
    def addEdge(self,edge):
        src=edge.getSource()
        dest=edge.getDestination()
        if not(src in self.nodes and dest in self.nodes):
            raise ValueError('Node not in graph')
        self.edges[src].append(dest)
    
    def childrenOf(self,node):
        return self.edges[node]
    
    def __str__(self):
        result=''
        for src in self.nodes:
            for dest in self.edges[src]:
                result = result + '('+str(src.getx())+','+str(src.gety())+') ->' + \
                '('+ str(dest.getx())+','+str(dest.gety())+')\n'
        return result[:-1]

class Graph(Digraph):
    def addEdge(self,edge):
        Digraph.addEdge(self,edge)
        rev=Edge(edge.getDestination(),edge.getSource())
        Digraph.addEdge(self,rev)
        
def printPath(path):
    result=''
    for i in range(len(path)):
        result=result +str(path[i])
        if i != len(path)-1:
            result=result + ' -> '
    return result


def BFS(graph,start,end):
    initPath=[start]
    pathQueue=[initPath]
    while len(pathQueue) !=0:
        tmpPath = pathQueue.pop(0)
        lastNode = tmpPath[-1]
        if lastNode ==end:
            return tmpPath
        neighbors=graph.childrenOf(lastNode)
        for nextNode in neighbors:
            if nextNode not in tmpPath:
                newPath = tmpPath + [nextNode]
                pathQueue.append(newPath)
    return None


def sp_4adj(g,nodes,V):
    for i in range(len(nodes)):
        j=i+1
        count=0
        src_row=nodes[i].getx()
        src_col=nodes[i].gety()
        src_intensity=nodes[i].getIntensity()
        N4=[[src_row,src_col+1],
           [src_row,src_col-1],
           [src_row-1,src_col],
           [src_row+1,src_col]]
        while j<len(nodes) or count==4:
            dest_row=nodes[j].getx()
            dest_col=nodes[j].gety()
            dest_intensity=nodes[j].getIntensity()
            if src_intensity in V and dest_intensity in V:
                for point in N4:
                    if point[0]==dest_row and point[1]==dest_col:
                        g.addEdge(Edge(nodes[i],nodes[j]))
                        count+=1
            j+=1                    
    return g


def sp_8adj(g,nodes,V):
    for i in range(len(nodes)):
        j=i+1
        count=0
        src_row=nodes[i].getx()
        src_col=nodes[i].gety()
        src_intensity=nodes[i].getIntensity()
        N8=[[src_row,src_col+1],
           [src_row,src_col-1],
           [src_row-1,src_col],
           [src_row+1,src_col],
           [src_row+1,src_col+1],
           [src_row-1,src_col+1],
           [src_row+1,src_col-1],
           [src_row-1,src_col-1]]

        while j<len(nodes) or count==8:
            dest_row=nodes[j].getx()
            dest_col=nodes[j].gety()
            dest_intensity=nodes[j].getIntensity()
            if src_intensity in V and dest_intensity in V:
                for point in N8:
                    if point[0]==dest_row and point[1]==dest_col:
                        g.addEdge(Edge(nodes[i],nodes[j]))
                        count+=1
            j+=1  
    return g


def sp_madj(g,nodes,V):
    for i in range(len(nodes)):
        j=i+1
        src_row=nodes[i].getx()
        src_col=nodes[i].gety()
        src_intensity=nodes[i].getIntensity()
        src_N4=[[src_row,src_col+1],
                [src_row,src_col-1],
                [src_row-1,src_col],
                [src_row+1,src_col]]
        while j<len(nodes):
            dest_row=nodes[j].getx()
            dest_col=nodes[j].gety()
            dest_intensity=nodes[j].getIntensity()
            a=0
            b=0
            if src_intensity in V and dest_intensity in V:
                for point in src_N4:
                    if point[0]==dest_row and point[1]==dest_col:
                        g.addEdge(Edge(nodes[i],nodes[j]))
                        a=1
                if a!=1:
                    src_ND=[[src_row+1,src_col+1],
                            [src_row-1,src_col+1],
                            [src_row+1,src_col-1],
                            [src_row-1,src_col-1]]
                    q_N4=[[dest_row,dest_col+1],
                             [dest_row,dest_col-1],
                             [dest_row-1,dest_col],
                             [dest_row+1,dest_col]]
                    for p in src_ND:
                        if p[0]==dest_row and p[1]==dest_col:
                            b=1
                    if b==1:
                        intersection=[]
                        for src in src_N4:
                            if src in q_N4:
                                intersection.append(src)
                        l=len(intersection)
                        count=0
                        while len(intersection)!=0:
                            tmp_node=intersection.pop(0)
                            for node in nodes:
                                x=node.getx()
                                y=node.gety()
                                if tmp_node[0]==x and tmp_node[1]==y:
                                    intensity=node.getIntensity()
                                    if intensity not in V:
                                        count+=1

                        if count==l:
                            g.addEdge(Edge(nodes[i],nodes[j]))
            j+=1  
    return g


    
def create_pixel_map(pixel_arr,p,q,path_type,V):
    size=pixel_arr.shape
    nodes=[]
    start=None
    end=None
    #Create Nodes out of the coordinates
    for row in range(size[0]):
        for col in range(size[1]):
            nodes.append(PixelNode(row,col,pixel_arr[row,col]))
            if row==p[0] and col==p[1]:
                start=nodes[-1]
            if row==q[0] and col==q[1]:
                end=nodes[-1]
            
            

    #Create Undirected Edges for different path types    
    g=Graph()
    for n in nodes:
        g.addNode(n)
      
    if path_type=='4':
        return (sp_4adj(g,nodes,V),start,end)
    elif path_type=='8':
        return (sp_8adj(g,nodes,V),start,end)
    elif path_type=='m':
        return (sp_madj(g,nodes,V),start,end)
    else:
        return (None,None,None)

def sp(pixel_arr,p,q,V,path_type):
    
    (g,start,end)=create_pixel_map(pixel_arr, p, q, path_type, V)
    if g==None:
        print('\n Incorrect Path Type entered.')
        return None
    if start==None or end ==None:
        print('\n Incorrect Start or End coordinates entered.')
        return None
    print("\nPath Type:{} ".format(path_type))
#    print("Graph: \n",g)
    sp=BFS(g,start,end)
    if sp==None:
        print('No path Found.')
    else:
        print("Path Exists.")
        print("Length of Shortest Path: ", len(sp)-1)
        print("Shortest Path: ", printPath(sp))
    

def main():
    #img=cv2.imread('lena-gray.bmp',0)
    pixel_arr=np.array([[3, 1, 2, 1],
                        [2, 2, 0, 2],
                        [1, 2, 1, 1],
                        [1, 0, 1, 2]])   
    p=[3,0]
    q=[0,3]
    V=[0,1]
    path_type='m'
    starttime=time.time()
    sp(pixel_arr,p,q,V,path_type)
    endtime=time.time()
    print('Time Taken in milli-seconds: ',(endtime-starttime)*1000)
    
    
if __name__ == '__main__':
    main()
