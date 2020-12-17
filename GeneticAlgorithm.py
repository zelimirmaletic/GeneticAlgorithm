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
import function as fun
import BinaryCoding as bin
import Chromosome as hrom
import parameters as param


""" Phase No.1 - Initialization Of The Population """
population = []
#Generate a population of random numbers
for i in range(param.POPULATION_SIZE):
    #generate a random number from [0,1] interval
    randomNumber = random.uniform(0,1)
    #Translate generated number into a point from function extremum interval
    point = bin.transformToInterval(randomNumber,0,1,fun.LOWER_X, fun.UPPER_X)
    #code point in binary
    binarySequence = bin.codeBinary(param.PRECISION, point, fun.LOWER_X, fun.UPPER_X )
    #make a new chromosome
    newChromosome = hrom.Chromosome(point, binarySequence)
    #add it to the population
    population.append(newChromosome)


""" Phase No.2 - Fitness Function """
#Make a list of chromosome x coordinates
xCoordinates = []
for chromosome in population:
    xCoordinates.append(chromosome.getX())
#Calculate function values in points
functionValues = []
for coordinate in xCoordinates:
    functionValues.append(fun.mathFunction(coordinate))
#Calculate fitness values for chromosomes
fitnessValues = bin.functionTransformation(functionValues,param.EXTREMUM)
#Store fitness values to chromosomes
i = 0
for chromosome in population:
    chromosome.setFitnessValue(fitnessValues[i])
    i+=1
#Calculate population fitness score
populationFitnessScore = bin.populationFitnessScore(fitnessValues)
print(populationFitnessScore)

finalPopulation = []

#If max then <=, if min then >=
while(populationFitnessScore != 0.0 ):
    """ Phase No.3 - Selection """
    #Roulette selection

    #calculate probabilities for every chromosome
    for chrom in population:
        chrom.setProbability(populationFitnessScore)

    #Define boundaries on the rulette propottional to probabilities
    sum = 0
    for chrom in population:
        sum += chrom.getProbability()
        chrom.setRouletteBoundary(sum)

    #Make a new empty population
    newPopulation = []
    #Spinning the roulette 
    for value in range(param.POPULATION_SIZE):
        rand = random.uniform(0,1)
        #see which chromosome is the chosen one
        for chrom in population:
            if(rand <= chrom.getBoundary()):
                #if seleted add it to a new population
                newPopulation.append(chrom)
                break

    """ Phase No.4 Recombination/Crossover """
    #Mix chromosomes in a generated population
    for x in range(param.NUMBER_OF_PAIRS):
        #generate two random numbers and tranform them to interval [0, populationNumber]
        first = m.floor(bin.transformToInterval(random.uniform(0,1),0,1,1,param.POPULATION_SIZE))
        second = m.floor(bin.transformToInterval(random.uniform(0,1),0,1,1,param.POPULATION_SIZE))
        #swap chromosomes in new population
        temp = newPopulation[first]
        newPopulation[first] = newPopulation[second]
        newPopulation[second] = temp
    #Do recombination on chromosomes based on a random number
    for x in range(int(param.POPULATION_SIZE/2)):
        #Generate random number
        randomNumber = random.uniform(0,1)
        if(randomNumber < param.RECOMBINARION_PROB):
            newPopulation[2*x].recombine(newPopulation[2*x+1])

    """ Phase No.5 Mutation """
    #Go over population, generate a random number which decides if chromosome is going to be mutated
    for x in range(param.POPULATION_SIZE):
        randomNumber = random.uniform(0,1)
        if(randomNumber < param.MUTATION_PROB):
            newPopulation[x].mutate()

    """ Phase No.6 (Re)Calculate Fitness """
    #Make a list of chromosome x coordinates
    xCoordinates = []
    for chromosome in newPopulation:
        xCoordinates.append(chromosome.getX())
    #Calculate function values in points
    functionValues = []
    for coordinate in xCoordinates:
        functionValues.append(fun.mathFunction(coordinate))
    #Calculate fitness values for chromosomes
    fitnessValues = bin.functionTransformation(functionValues,param.EXTREMUM)
    #Store fitness values to chromosomes
    i = 0
    for chromosome in population:
        chromosome.setFitnessValue(fitnessValues[i])
        i+=1
    #Calculate population fitness score
    populationFitnessScore = bin.populationFitnessScore(fitnessValues)
    print(populationFitnessScore)
    finalPopulation = newPopulation

for chrom in finalPopulation:
    chrom.printChromosome()