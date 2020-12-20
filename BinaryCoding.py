import math
import function as f
import parameters as param

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

def decodeBinary(numberForDecoding, bottomBoundary, topBoundary):
    numberOfBits = len(numberForDecoding)
    numberOfIntervals = 0
    for bit,i in zip(reversed(numberForDecoding),range(numberOfBits)):
        if (bit == '1'):
            numberOfIntervals += math.pow(2, i)
    #Recalculate number
    x = bottomBoundary + (((topBoundary-bottomBoundary)/(pow(2,numberOfBits)-1))*numberOfIntervals)
    return x

#Transform one interval to another one
def transformToInterval(number, bottomOriginal, topOriginal, bottomNew, topNew):
    k = (topNew-bottomNew)/(topOriginal-bottomOriginal)
    n = (bottomNew*topOriginal-topNew*bottomOriginal)/(topOriginal-bottomOriginal)
    return (k*number + n)

#Transforms values of function to make them all positive
def fitnessFunction(functionValuesList, extremum):
    translatedValues = []
    if (extremum == "max"):
        sortedList = sorted(functionValuesList)
        minimalValue = sortedList[0]
        for value in functionValuesList:
            #translate function
            translatedValues.append(value-minimalValue)
    elif (extremum == "min"):
        #sortedList = sorted(functionValuesList, reverse=True)
        #maximalValue = sortedList[0]
        #for value in functionValuesList:
            #rotate function around an axis and translate
        #    translatedValues.append(maximalValue-value)
        for value in functionValuesList:
            translatedValues.append(-value)
    return translatedValues

def calculateProbabilities(fitnessValues):
    populationFitnessScore = 0.0
    for x in fitnessValues:
        populationFitnessScore+=x
    probabilities = []
    for x in fitnessValues:
        probabilities.append(x/populationFitnessScore)
    return probabilities

def calculatePopulationFitnessScore(population):
    #simply sum all the values
    populationFitnessScore = 0.0
    for chrom in population:
        populationFitnessScore += chrom.getFitnessValue()
    return populationFitnessScore

