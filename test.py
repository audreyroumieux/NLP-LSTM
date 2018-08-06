# -*- coding: utf-8 -*-
"""
Created on Fri Jun  1 10:38:18 2018
@author: audrey roumieux
Projet:
Description:
"""
# TEST Unitaire
import numpy as np
from scalaire import scalar_product
from scalaire import norme
from scalaire import cos_similiarite


def test_answer_scalar_product():
    u = np.array([ 1, 1])
    v = np.array([ -1, 1])
    assert scalar_product(u, v) == 0


def test_ampty_scalar_product():
    u = np.array([])
    v = np.array([])
    return scalar_product(u, v) 
    
def test_taille_vector():
    u = np.array([1])
    v = np.array([ -1, 1])
    assert len(u) == len(v)
    
def test_type_scalar_product():
    u = np.array(['toto', '1'])
    v = np.array([ -1, 1])
    return scalar_product(u, v) 


def test_answer_norme():
    x = np.array([ 1, 0])
    assert norme(x) == 1
    

def test_answer_cos_similiarite():
    u = np.array([ 1, 1])
    v = np.array([ -1, 1])
    assert cos_similiarite(u, v) == 0
    
    

def test_divide_by0_cos_similiarite():
    u = np.array([ 1, 1])
    v = np.array([ -1, 1])
    assert norme(u) * norme(v) > 0