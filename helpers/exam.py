#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jul 10 15:26:55 2018

@author: lucasjanon
"""
import random
import unittest

def rollDice():
    return random.randint(1, 6)

def rollUntilResult():
    tries = 0
    rolled1 = 0
    rolled2 = 0
    rolled3 = 0
    while((not (rolled1 == 6 and rolled2 == 6)) and (not (rolled2 == 6 and rolled3 == 6)) and (not (rolled1 == 6 and rolled3 == 6))):
        rolled1 = rollDice()
        rolled2 = rollDice()
        rolled3 = rollDice()
        tries += 1
    return tries

def getProb(amount):
    total = 0
    for roll in range(amount):
        total += rollUntilResult()
    return total / amount

def greedySum(L, s):
    """ input: s, positive integer, what the sum should add up to
               L, list of unique positive integers sorted in descending order
        Use the greedy approach where you find the largest multiplier for 
        the largest value in L then for the second largest, and so on to 
        solve the equation s = L[0]*m_0 + L[1]*m_1 + ... + L[n-1]*m_(n-1)
        return: the sum of the multipliers or "no solution" if greedy approach does 
                not yield a set of multipliers such that the equation sums to 's'
    """
    multipliers = []
    difference = s
    total = 0
    for item in L:
        multiplier = int(difference / item)
        multipliers.append(multiplier)
        total += item * multiplier
        difference -= item * multiplier
    if difference != 0:
        return 'no solution'
    return sum(multipliers)
    
def max_contig_sum(L):
    """ L, a list of integers, at least one positive
    Returns the maximum sum of a contiguous subsequence in L """
    maxSum = 0
    for index, item in enumerate(L):
        if item > maxSum:
            maxSum = item
        total = item
        for subItem in L[index + 1:]:
            total += subItem
            if total > maxSum:
                maxSum = total
    return maxSum


class TestGreedySum(unittest.TestCase):

    def test_noSolution(self):
        self.assertEqual(greedySum([15, 14, 13, 12, 11], 100), 'no solution')

    def test_solution(self):
        self.assertEqual(greedySum([15, 10], 100), 7)
        self.assertEqual(greedySum([10, 5, 1], 14), 5)
    
    if __name__ == '__main__':
        unittest.main()
        
class TestMaxContigSum(unittest.TestCase):
    def test_solution(self):
        self.assertEqual(max_contig_sum([-1, 5, 15, 10]), 30)
        self.assertEqual(max_contig_sum([-1, 10, -5, 10, -100, 10, 4]), 15)
    
    if __name__ == '__main__':
        unittest.main()

def solveit(test):
    """ test, a function that takes an int parameter and returns a Boolean
        Assumes there exists an int, x, such that test(x) is True
        Returns an int, x, with the smallest absolute value such that test(x) is True 
        In case of ties, return any one of them. 
    """
    num = 0
    while (test(num) != True and test(-num) != True):
        num += 1
    return num if test(num) else -num
        

#### This test case prints 49 ####
def f(x):
    return (x+15)**0.5 + x**0.5 == 15
print(solveit(f))

def f(x):
    return x == -1
print(solveit(f))

#### This test case prints 0 ####
def f(x):
    return x == 0
print(solveit(f))
