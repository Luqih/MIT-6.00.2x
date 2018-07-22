#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jul 11 22:29:49 2018

@author: lucasjanon
"""

def stdDev(SL):
    if not len(SL):
        return float('NaN')
    L = list(map(lambda x: len(x), SL))
    mean = sum(L) / len(L)
    sDev = 0.00
    for e in L:
        sDev += (e - mean)**2
    sDev = (sDev / len(L))**0.5
    return sDev

def stdDevInt(L):
    if not len(L):
        return float('NaN')
    mean = sum(L) / len(L)
    sDev = 0.00
    for e in L:
        sDev += (e - mean)**2
    sDev = (sDev / len(L))**0.5
    print(sDev / mean)
    return sDev

stdDevInt([10, 4, 12, 15, 20, 5])
