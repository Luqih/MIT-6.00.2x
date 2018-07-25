#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jul 24 17:27:21 2018

@author: lucasjanon
"""
import random

def drawing_without_replacement_sim(numTrials):
    '''
    Runs numTrials trials of a Monte Carlo simulation
    of drawing 3 balls out of a bucket containing
    4 red and 4 green balls. Balls are not replaced once
    drawn. Returns a float - the fraction of times 3 
    balls of the same color were drawn in the first 3 draws.
    '''
    sameColor = 0
    differentColor = 0
    for trial in range(0, numTrials):
        balls = ['R','R','R','R','G','G','G','G']
        drawed = []
        for ball in range(0, 3):
            index = random.randint(0, 7 - ball)
            drawed.append(balls[index])
            del balls[index]
        if drawed[0] == drawed[1] and drawed[1] == drawed[2]:
            sameColor += 1
        else:
            differentColor += 1
    return sameColor / differentColor
        
print(drawing_without_replacement_sim(50000))