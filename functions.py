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

def derv(x,t):
    """Computes the derv operator for the basic sir model"""

    y=zeros(3); 
    y[0]=-beta*x[0]*x[1]
    y[1]=beta*x[0]*x[1]-gamma*x[1]
    y[2]=gamma*x[1]
    return(y)


population_sizes=odeint(derv, init, time)

plot(time, population_sizes[:,0], "r", time, population_sizes[:,1], "g", time, population_sizes[:,2], "b")
legend(("Susceptible","Infected","Recovered"), loc=0)
ylabel("Number of People")
xlabel("Time")
title("SIR Model")

show()
    
