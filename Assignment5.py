


import numpy as np
from matplotlib import pyplot as pp


A = 10 #V/m
a = 2 #m
k = 0.4 #1/m
h = 0.5 #how big the steps are (delta x)
def pos(x):
    return A*np.cos(np.pi*x/a)*np.exp(-k*x)

def derfor(x):
    return (pos(x+h)-pos(x))/h

def dercen(x):
    return((pos(x+h)-pos(x-h))/(2*h))

def dercalc(x):
    return(-A*np.pi/a*np.sin(np.pi*x/a)*np.exp(-k*x)-k*A*np.cos(np.pi*x/a)*np.exp(-k*x))

# question 1
x = np.arange(0,20,0.1)
y = pos(x)
pp.figure()
pp.plot(x,y)
pp.xlabel('Position (m)')
pp.ylabel('Electric Field (V/m)')
pp.title('Electric Field vs. Position')
pp.savefig('question1.png')
pp.figure()
# question 2

#forward differencing
x = np.arange(0,20,0.1)
y = derfor(x)
pp.plot(x,y,color="red",label="forward differencing")

#central differening
x = np.arange(0,20,0.1)
y = dercen(x)
pp.plot(x,y,color="blue",label="central differencing")

#calculation
x = np.arange(0,20,0.1)
y = dercalc(x)
pp.plot(x,y,color="green",label="calculated derivative")

pp.xlabel('Position (m)')
pp.ylabel('dE/dx (V/m^2)')
pp.title('dE/dx vs. Position')
pp.legend()
pp.savefig('question2partC.png')

pp.figure()
#absolute error
error = np.abs(derfor(x) - dercalc(x))
pp.plot(x,error,label="forward")
error = np.abs(dercen(x) - dercalc(x))
pp.plot(x,error,label="central")
pp.yscale('log')
pp.xlabel('Position (m)')
pp.ylabel('Absolute Error')
pp.title('Absolute Error vs. Position (h=0.5)')
pp.legend()
pp.savefig('question2partD.png')

pp.figure()
h = 0.05
error = np.abs(derfor(x) - dercalc(x))
pp.plot(x,error,label="forward")
error = np.abs(dercen(x) - dercalc(x))
pp.plot(x,error,label="central")
pp.yscale('log')
pp.xlabel('Position (m)')
pp.ylabel('Absolute Error')
pp.title('Absolute Error vs. Position(h=0.05)')
pp.legend()
pp.savefig('question2partE.png')

#central differencing is more accurate

