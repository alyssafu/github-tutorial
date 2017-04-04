#!/usr/bin/python

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


r=odeint(derv, init, time)

plot(time, r[:,0], "r", time, r[:,1], "g", time, r[:,2], "b")
legend(("Susceptible","Infected","Recovered"), loc=0)
ylabel("Number of People")
xlabel("Time")
title("SIR Model")

show()
    
