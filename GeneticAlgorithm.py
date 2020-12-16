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
    Selection
    Crossover
    Mutation
    Compute fitness
UNTIL population has converged
STOP
"""

#Libraries
import random
import function as fun
import BinaryCoding as bin
import Chromosome as hrom

"""General algorithm parameters"""
RECOMBINARION_PROB = 0.15
MUTATION_PROB = 0.05
POPULATION_SIZE = 8
PRECISION = 2
EXTREMUM = "min" #can be min or max


""" Phase No.1 - Initialization Of The Population """
population = []
#Generate a population of random numbers
for i in range(POPULATION_SIZE):
    #generate a random number from [0,1] interval
    randomNumber = random.uniform(0,1)
    #Translate generated number into a point from function extremum interval
    point = bin.transformToInterval(randomNumber,0,1,fun.LOWER_X, fun.UPPER_X)
    #code point in binary
    binarySequence = bin.codeBinary(PRECISION, point, fun.LOWER_X, fun.UPPER_X )
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
fitnessValues = bin.functionTransformation(functionValues,EXTREMUM)
#Store fitness values to chromosomes
i = 0
for chromosome in population:
    chromosome.setFitnessValue(fitnessValues[i])
    i+=1
#Calculate population fitness score
populationFitnessScore = bin.populationFitnessScore(fitnessValues)

""" Phase No.3 - Selection """



