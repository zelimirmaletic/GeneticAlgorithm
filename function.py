#Mathematic function for which we calculate maximum or minimum
import math as m 

UPPER_X = 10
LOWER_X = -10

def mathFunction(x):
    #define function
    y = x*x + 10*m.cos(x-5)
    return y
