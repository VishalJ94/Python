# -*- coding: utf-8 -*-
"""
Created on Fri Dec 17 19:11:31 2021

@author: 
"""
# def input_numbers():
#     a=int(input("Kindly provide first number:"))
#     b=int(input("Kindly provide second number:"))
#     n=0
#     while (n<b):
#         print(a)
#         a=a+1
#         n=n+1
        
# input_numbers()


a=int(input("Kindly provide first number:"))
b=int(input("Kindly provide second number:"))
n=[i for i in range(0,(a+(b*2)+1)) if i%2==0]
print(n)

# def evennumber():
#     for i in n:
#         if i>=a:
#             return i        
    
# def printtype():
#     for i in range(0,b):
#         print(evennumber())

#print this line.
def nexteven():
    for i in n:
        if i>=a:
            print(i)

nexteven()


#this is the line1
            
        
        
    
