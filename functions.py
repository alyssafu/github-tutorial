
#!/usr/bin/python
def islandPerimeter(grid):
    """
    The solution to today's leetcode challenge.
    :type grid: List[List[int]]
    :rtype: int
    """
    
    leni = len(grid)
    lenj = len(grid[0])

    def countCell(i,j):
        if not grid[i][j]:
            return 0
        borders = 4
        if i>0 and grid[i-1][j]: borders -= 1
        if i<(leni-1) and grid[i+1][j]: borders -= 1
        if j<(lenj-1) and grid[i][j+1]: borders -= 1
        if j>0 and grid[i][j-1]: borders -= 1
        return borders
    
    return sum([countCell(i,j) for i in range(leni) for j in range(lenj)])


"""This program uses scipy to integrate and plot the results of a basic SIR model"""


from scipy import * 
from scipy.integrate import *
from pylab import *

#Define Constants
beta=2.0
gamma=.8
init=array([0.95,0.05,0.0])
finalTime=20.0
time=arange(0,finalTime, 0.01)


# mdh function - leet code problem
class MDH(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        indices = []
        for i in xrange(len(nums)):
            if (i != len(nums)+1) and (len(indices) !=2):
                #print i, len(nums),len(indices)
                for j in xrange(len(nums[i+1:])):
                    #print i,j,i+j,nums[i],nums[j],nums[i+j]
                    if nums[i+j+1] + nums[i] == target:
                        indices = [i,i+j+1]
                        break
        return indices




def derv(x,t):
    """Computes the derv operator for the basic sir model"""

    y=zeros(3); 
    y[0]=-beta*x[0]*x[1]
    y[1]=beta*x[0]*x[1]-gamma*x[1]
    y[2]=gamma*x[1]
    return(y)


r=odeint(derv, init, time)

plot(time, r[:,0], "r", time, r[:,1], "g", time, r[:,2], "b")
legend(("Susceptible","Infected","Recovered"), loc=0)
ylabel("Number of People")
xlabel("Time")
title("SIR Model")

show()

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
