import math
import function as f

#Binary coding of decimal numbers
def codeBinary(precision, numberForCoding, bottomBoundary, topBoundary):
    if(numberForCoding < bottomBoundary or numberForCoding > topBoundary):
        print("Number is out of boundaries!")
        return
    if(bottomBoundary > topBoundary):
        print("Invalid boundaries!")
        return
    #Calculate interval width
    intervalWidth = 1/(10^precision)
    #Calculate number of bits needed for coding
    numberOfBits = math.ceil(math.log(((topBoundary-bottomBoundary)*(pow(10, precision))+1),2))
    #Number of intervals needed to represent a number
    numberOfIntervals = math.floor(((numberForCoding-bottomBoundary) * pow(2,numberOfBits) - 1)/(topBoundary-bottomBoundary))
    #Convert to binary number
    binaryNumber = bin(numberOfIntervals)
    #Exclude 0b from the binary format 0b1010110
    binaryNumber = binaryNumber[2:]
    #Recalculate number
    x = bottomBoundary + (((topBoundary-bottomBoundary)/(pow(2,numberOfBits)-1))*numberOfIntervals)
    #Format output string to have exactly numberOfBits symbols
    if(len(binaryNumber)<11):
        difference = 11 - len(binaryNumber)
        while (difference):
            binaryNumber = "0" + binaryNumber
            difference -= 1
    return binaryNumber

#Transform one interval to another one
def transformToInterval(number, bottomOriginal, topOriginal, bottomNew, topNew):
    k = (topNew-bottomNew)/(topOriginal-bottomOriginal)
    n = (bottomNew*topOriginal-topNew*bottomOriginal)/(topOriginal-bottomOriginal)
    return (k*number + n)

#Transforms values of function to make them all positive
def functionTransformation(functionValuesList, extremum):
    translatedValues = []
    if (extremum == "max"):
        sortedList = sorted(functionValuesList)
        minimalValue = sortedList[0]
        for value in functionValuesList:
            #translate function
            translatedValues.append(value-minimalValue)
    elif (extremum == "min"):
        sortedList = sorted(functionValuesList, reverse=True)
        maximalValue = sortedList[0]
        for value in functionValuesList:
            #rotate function around an axis and translate
            translatedValues.append(maximalValue-value)
    return translatedValues


def populationFitnessScore(functionValuesList):
    #simply sum all the values
    sum = 0
    for value in functionValuesList:
        sum += value
    return sum



#Tests
#print(codeBinary(2, -9.3111, -10, 10))
#print(transformToInterval(1,0,1,-10,10))

#x = [-9.3111, -1.2251, -2.3688, 5.3103, 5.9040, -6.2625, -0.2047, -1.0883]