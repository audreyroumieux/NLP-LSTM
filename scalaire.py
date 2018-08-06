# -*- coding: utf-8 -*-
"""
Created on Fri Jun  1 11:11:02 2018
@author: audrey roumieux
Projet:
Description:
"""
import numpy as np


def my_scalar_product(u, v):
    # sum( [x * y for x, y in zip(u, v)] )
    if len(u) >= 2 :
        res = sum(u[0] * v[0], scalar_product(u[1:], v[1:]) )
    return  res

def scalar_product(u, v):
    return np.sum(u * v)

v = np.array([ 1, 1])
w = np.array([ -1, 1])

#print(my_scalar_product(v, w))
print(scalar_product(v, w))

w = np.array([ 2, 2])
print(scalar_product(v, w))




def norme(x):
    return (scalar_product(x, x)**0.5)

def cos_similiarite (u, v):
    #colinearite = np.linalg.norm(u) * np.linalg.norm(v)
    colinearite =  norme(u) * norme(v)
    return scalar_product(u, v) / colinearite

v = np.array([ 1, 1])
w = np.array([ -1, 1])
print(cos_similiarite(v, w))

v = np.array([ 1, 1, 1])
w = np.array([ 1, 1, 4])
cos_similiarite(v, w)