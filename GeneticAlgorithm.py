""" 
GENETIC ALGORITHM
Želimir Maletić 11125/18 
Faculty of Electrical Engineering Banja Luka
2020
"""

"""
START
Generate the initial population *
Compute fitness *
REPEAT
    Selection *
    Crossover *
    Mutation *
    Compute fitness *
UNTIL population has converged
STOP
"""

#Libraries
import random
import math as m

from numpy.lib.index_tricks import fill_diagonal

import function as fun
import BinaryCoding as bin
import Chromosome as hrom
import parameters as param
import matplotlib
import matplotlib.pyplot as plt
import numpy as np


"""Make main polot of function"""
# Data for plotting
t = np.arange(-10.0, 10.0, 0.1)
#s = 1 + np.sin(2 * np.pi * t)
s = -1*(pow(t,2)+10*np.cos(5-t))

fig, ax = plt.subplots()
ax.plot(t, s)

""" Phase No.1 - Initialization Of The Population """
#Make a population of chromosomes
initialPopulation = []
#Generate a population of random numbers
for i in range(param.POPULATION_SIZE):
    #generate a random number from [0,1] interval
    randomNumber = random.uniform(0,1)
    #Translate generated number into a point from function extremum interval
    coordinate = bin.transformToInterval(randomNumber,0,1,fun.LOWER_X, fun.UPPER_X)
    #code point in binary
    binarySequence = bin.codeBinary(param.PRECISION, coordinate, fun.LOWER_X, fun.UPPER_X )
    #make a new chromosome
    newChromosome = hrom.Chromosome(coordinate, binarySequence)
    #add it to the population
    initialPopulation.append(newChromosome)


""" Phase No.2 - Fitness Function """
#Calculate function values in points
functionValues = []
for chromosome in initialPopulation:
    functionValues.append(fun.mathFunction(chromosome.getX()))
#Calculate fitness values for chromosomes
fitnessValues = bin.fitnessFunction(functionValues,param.EXTREMUM)
#Store fitness values to chromosomes
i = 0
for chromosome in initialPopulation:
    chromosome.setFitnessValue(fitnessValues[i])
    i+=1
#Calculate population fitness score
initialPopulationFitnessScore = bin.populationFitnessScore(fitnessValues)
print("Initial population fitness score: ",initialPopulationFitnessScore)


finalPopulation = initialPopulation
finalPopulationFitnessScore = initialPopulationFitnessScore

#If max then <=, if min then >=
for x in range(param.NUMBER_OF_ITERATIONS):
    """ Phase No.3 - SELECTION """
    #Roulette selection
    """
    #calculate probabilities for every chromosome
    for chrom in finalPopulation:
        chrom.setProbability(finalPopulationFitnessScore)

    #Define boundaries on the rulette propottional to probabilities
    sum = 0
    for chrom in finalPopulation:
        sum += chrom.getProbability()
        chrom.setRouletteBoundary(sum)

    #Make a new empty sub population
    newSubPopulation = []
    #Spinning the roulette 
    for value in range(param.POPULATION_SIZE):
        randomNumber = random.uniform(0,1)
        #see which chromosome is the chosen one
        for chrom in finalPopulation:
            if(randomNumber <= chrom.getBoundary()):
                #if selected add it to a new population
                newSubPopulation.append(chrom)
                break
    """
    #Elitist selection
    newSubPopulation = []
    #Sort chromosomes by fitness value based on EXTREMUM parameter
    if(param.EXTREMUM == "min"):
        finalPopulation.sort(key=lambda e:e.fitnessValue)
        for x in range(int(param.POPULATION_SIZE /2)):
            newSubPopulation.append(finalPopulation[x])
            newSubPopulation.append(finalPopulation[x])
    if(param.EXTREMUM == "max"):
        finalPopulation.sort(key=lambda e:e.fitnessValue, reverse=True)
        for x in range(int(param.POPULATION_SIZE /2)):
            newSubPopulation.append(finalPopulation[x])
            newSubPopulation.append(finalPopulation[x])

    print("Sub population size: ", len(newSubPopulation))



    """ Phase No.4 Recombination/Crossover """
    #Mix chromosomes in a generated sub-population
    for x in range(param.NUMBER_OF_PAIRS):
        #generate two random numbers and tranform them to interval [0, populationNumber]
        first = m.floor(bin.transformToInterval(random.uniform(0,1),0,1,0,param.POPULATION_SIZE-1))
        second = m.floor(bin.transformToInterval(random.uniform(0,1),0,1,0,param.POPULATION_SIZE-1))
        #swap chromosomes in new population
        temp = newSubPopulation[first]
        newSubPopulation[first] = newSubPopulation[second]
        newSubPopulation[second] = temp
    #Do recombination on chromosomes based on a random number
    for x in range(int(param.POPULATION_SIZE/2)):
        #Generate random number
        randomNumber = random.uniform(0,1)
        if(randomNumber < param.RECOMBINARION_PROB):
            newSubPopulation[2*x].recombine(newSubPopulation[2*x+1])

    """ Phase No.5 Mutation """
    #Go over population, generate a random number which decides if chromosome is going to be mutated
    for x in range(param.POPULATION_SIZE):
        randomNumber = random.uniform(0,1)
        if(randomNumber < param.MUTATION_PROB):
            newSubPopulation[x].mutate()

    for chrom in newSubPopulation:
        ax.scatter(chrom.getX(), fun.mathFunction(chrom.getX()),c="red")

    """ Phase No.6 (Re)Calculate Fitness """
    #Make a list of chromosome x coordinates
    xCoordinates = []
    for chromosome in newSubPopulation:
        xCoordinates.append(chromosome.getX())
    #Calculate function values in points
    functionValues = []
    for coordinate in xCoordinates:
        functionValues.append(fun.mathFunction(coordinate))
    #Calculate fitness values for chromosomes
    fitnessValues = bin.fitnessFunction(functionValues,param.EXTREMUM)
    #Store fitness values to chromosomes
    i = 0
    for chromosome in newSubPopulation:
        chromosome.setFitnessValue(fitnessValues[i])
        i+=1
    #Calculate population fitness score
    newSubPopulationFitnessScore = bin.populationFitnessScore(fitnessValues)
    print(newSubPopulationFitnessScore)
    if(newSubPopulationFitnessScore<=finalPopulationFitnessScore ):
        finalPopulation = newSubPopulation
        finalPopulationFitnessScore = newSubPopulationFitnessScore
    print(newSubPopulationFitnessScore)
    if (newSubPopulationFitnessScore == 0):
        break

finalPopulation.sort(key=lambda e : e.fitnessValue)
finalPopulation[0].printChromosome()
for chrom in finalPopulation:
    chrom.printChromosome()



for chrom in initialPopulation:
    ax.scatter(chrom.getX(), fun.mathFunction(chrom.getX()),c="red")

finalPopulation.sort(key=lambda e: e.fitnessValue,reverse=True)
ax.scatter(finalPopulation[0].getX(), fun.mathFunction(finalPopulation[0].getX()),c="green")


ax.set(xlabel='x-axis', ylabel='y-axis',
       title='Genetic Algotithm f(x) = x^2 + 10*cos(5-x)')
ax.grid()

plt.show()
