#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct  3 01:18:03 2018

@author: MyReservoir
"""
#Dependencies used: 
#numpy: to perform convolution
#opencv(cv2): to read and display images

#The main function block is at the bottom of this code, from where the code execution starts.
#The program asks the user to input the type of padding, the desired output shape, 
#and the desired filter kernel to be used. 

#Available options:
#Output Shape= ['same','valid','full']
#Pad Types= ['constant', 'wrap' , 'edge', 'reflect']
#Kernel options= {1:'sobel',2:'laplacian'}


#To change the filter kernel, change the kernel variable in the main block and change 
#available_kernels variable in the get_desired_input() function if needed. 

#If incorrect options are entered, the code gives an error information and exits. 


import cv2
import numpy as np


def pad_width(img,shape,f):        
    if shape=='valid':
        p=0
    elif shape=='same': 
        p=int((f-1)/2)
    else:
        p=f-1
        
    return p

def output_size(img,f,p):
    size=img.shape
    v_dim=size[0]+2*p-f+1
    h_dim=size[1]+2*p-f+1
    output_img=np.zeros((v_dim,h_dim))
    
    return output_img

def img2patch(pad_img,convolved_img,kernel):
    dim=pad_img.shape
    for h in range(0,dim[0]-2):
        for w in range(0,dim[1]-2):
            img_patch=pad_img[h:h+3,w:w+3]
            convolved_img[h,w]=convolution_operation(img_patch,kernel)
            
    return convolved_img


def convolution_operation(img_patch,kernel):
    b=np.multiply(img_patch,kernel)
    return int(np.sum(b))

def print_dimensions(img,pad_img,convolved_img):
    print("\nOriginal Shape: ",img.shape)
    print("Padded Image Shape: ",pad_img.shape)
    print("Output shape: ",convolved_img.shape)    


def get_desired_input():
    shape=['same','valid','full']
    print('\nEnter the output shape(same,valid,full): ')
    desired_shape=input()
    if desired_shape not in shape:
        print("\nError: Incorrect Shape Entered.")
        return (None,None,None)
    
    pad_type=['constant', 'wrap' , 'edge', 'reflect']
    print('\nEnter the padding type (constant, wrap , edge, reflect): ')
    desired_pad_type=input()
    if desired_pad_type not in pad_type:
        print("\nError: Incorrect Pad Type Entered.")
        return (None,None,None)
    
    print('\nEnter 1 to select Sobel kernel(3x3) or enter 2 to select Laplacian kernel(3x3):')
    sel_kernel=int(input())
    available_kernels={1:'sobel',2:'laplacian'}
    if sel_kernel not in available_kernels:
        print("\nError: Incorrect kernel number entered.")
        return (None,None,None)
    return (desired_shape,desired_pad_type,sel_kernel)


def apply_filter(img,out_shape,mode,kernel):
    f=kernel.shape[0]
    p=pad_width(img,out_shape,f)
    padded_img=np.pad(img,p,mode)
    output_img=output_size(img,f,p)
    print_dimensions(img,padded_img,output_img)
    filtered=img2patch(padded_img,output_img,kernel)
    return filtered
    
    
def main():
    (out_shape,mode,sel_kernel)=get_desired_input()
    if out_shape==None or mode==None or sel_kernel==None:
        return None
    
    img=cv2.imread('lena-gray.bmp',0)
    cv2.imshow("Original",img)
    
    if sel_kernel==1:
        kernel=np.array([[-1,-2,-1],
                         [0, 0, 0],
                         [1, 2, 1]])
        filtered=apply_filter(img,out_shape,mode,kernel)
        cv2.imshow('Vertical Sobel Filter',filtered)
        cv2.imwrite("Vertical Sobel Filter.png",filtered)



        kernel=np.array([[-1,0,1],
                         [-2, 0, 2],
                         [-1, 0, 1]])
        filtered=apply_filter(img,out_shape,mode,kernel)
        cv2.imshow('Horizontal Sobel Filter',filtered)
        cv2.imwrite("Horizontal Sobel Filter.png",filtered)


    elif sel_kernel==2:
        kernel=np.array([[0,-1,0],
                         [-1,4,-1],
                         [0,-1,0]])
        filtered=apply_filter(img,out_shape,mode,kernel)
        cv2.imshow('Laplacian Filtered Image',filtered)
        cv2.imwrite("Laplacian Filtered Image.png",filtered)

 
    
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    

if __name__ == '__main__':
    main()

