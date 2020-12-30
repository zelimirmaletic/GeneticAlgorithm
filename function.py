#Mathematic function for which we calculate maximum or minimum
import math as m 

LOWER_X = -3.00
UPPER_X = 3.00

LOWER_Y = -4.00
UPPER_Y = 4.00

def mathFunction(x,y):
    #y =x*x + 10.0*m.cos(x-5.00)
    #Minimum of this function is at x=1.544 and it is y=-7.126

    a = -(x*x+pow((y+1),2))
    b = -(x*x+y*y)
    c = -(pow((x+2),2)+y*y)
    z = 3*pow((1-x),2)*pow(m.e,a) - 7*(x/5 - pow(x,3) - pow(y,5))*pow(m.e,b)-(1/3)*pow(m.e,c)
    return z



