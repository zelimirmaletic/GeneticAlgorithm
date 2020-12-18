#Mathematic function for which we calculate maximum or minimum
import math as m 

UPPER_X = 10
LOWER_X = -10

def mathFunction(x):
    #define function
    y =(-1)*( x*x + 10*m.cos(x-5))
    return y

#Minimum of this function is at x=1.544 and it is y=-7.126

