#!/usr/bin/python

"""This program uses scipy to integrate and plot the results of a basic SIR model"""


from scipy import * 
from scipy.integrate import *
from pylab import *

#Define Constants
Beta=2.0
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
    y[0]=-Beta*x[0]*x[1]
    y[1]=Beta*x[0]*x[1]-gamma*x[1]
    y[2]=gamma*x[1]
    return(y)


r=odeint(derv, init, time)

plot(time, r[:,0], "r", time, r[:,1], "g", time, r[:,2], "b")
legend(("Susceptible","Infected","Recovered"), loc=0)
ylabel("Number of People")
xlabel("Time")
title("SIR Model")

show()
    
