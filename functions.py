#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Tue Apr  4 10:53:33 2017

@author: zhihuixie
"""

def countPrimes(self, n):
    """
    :type n: int
    :rtype: int
    """
    if n < 3:
        return 0
    arr = [True]*n
    arr[0] = arr[1] = False
    # optimization - any number can be divide by i*(i+n) is not a primer
    for i in xrange(2, int(n**0.5) + 1):
        if arr[i]:
            arr[i*i : n : i] = [False]*len(arr[i*i : n : i])
    return sum(arr)