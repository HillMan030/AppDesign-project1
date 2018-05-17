# -*- coding: utf-8 -*-
"""
Created on Fri Jan 12 23:09:12 2018

@author: USER
"""
test ='1'
text = 1
#c = text - 1
#x = str(c) +'.txt'
#f = open(x) 
#print(f.read())


if test=="推":
    f = open('Output1.txt','r')
    print (f.read())

elif int(test) in range(0,127):
    x = str(test) +'.txt'
    f = open(x) 
    print(f.read())
                    
                        #count=True