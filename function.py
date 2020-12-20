#Mathematic function for which we calculate maximum or minimum
import math as m 

LOWER_X = -10.00
UPPER_X = 10.00

def mathFunction(x):
    y =-(x*x + 10.0*m.cos(x-5.00))
    return y

#Minimum of this function is at x=1.544 and it is y=-7.126

