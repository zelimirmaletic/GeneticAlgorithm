#Here are stored function which represent the consecutive phases of the genetic algorithm
#Libraries
import random
import math as m
import function as fun
import BinaryCoding as bin
import Chromosome as hrom
import parameters as param

""" POPULATION INITIALIZATION """
#Function for making an initial population
def initializePopulation():
    population = []
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
        population.append(newChromosome)
    #calculate initial fitness values
    coordinates = []
    for chrom in population:
        coordinates.append(chrom.getX())
    functionValues = []
    for x in coordinates:
        functionValues.append(fun.mathFunction(x))
    fitnessValues = bin.fitnessFunction(functionValues,param.EXTREMUM)
    #Store fitness values to chromosomes
    i = 0
    for chromosome in population:
        chromosome.setFitnessValue(fitnessValues[i])
        i+=1
    return population

""" FITNESS EVALUATION """
def fitnessEvaluation(population):
    #Calculate function values in points
    functionValues = []
    for chromosome in population:
        functionValues.append(fun.mathFunction(chromosome.getX()))
    #Calculate fitness values for chromosomes
    fitnessValues = bin.fitnessFunction(functionValues,param.EXTREMUM)
    #Store fitness values to chromosomes
    i = 0
    for chromosome in population:
        chromosome.setFitnessValue(fitnessValues[i])
        i+=1
    #Determine minimal/maximal function value
    extremumValue = functionValues[0]
    for value in functionValues:
        if(param.EXTREMUM=="min" and value<extremumValue):
            extremumValue=value
        elif(param.EXTREMUM=="max" and value>extremumValue):
            extremumValue = value
    return population,extremumValue

""" SELECTION """
def selection(population):
    #Roulette selection
    #calculate probabilities for every chromosome
    fitnessValues = []
    for chrom in population:
        fitnessValues.append(chrom.getFitnessValue())
    probabilities = bin.calculateProbabilities(fitnessValues)
    #set probabilities
    for value,chrom in zip(probabilities,population):
        chrom.setProbability(value)
    #Define boundaries on the rulette propottional to probabilities
    sum = 0.0
    for chrom in population:
        sum += chrom.getProbability()
        chrom.setRouletteBoundary(sum)
    #Make a new empty subpopulation
    subPopulation = []
    #Spinning the roulette 
    for value in range(param.POPULATION_SIZE):
        randomNumber = random.uniform(0,1)
        #see which chromosome is the chosen one
        for chrom in population:
            if(randomNumber <= chrom.getBoundary()):
                #if selected add it to a new population
                subPopulation.append(chrom)
                break
    #print("Sub population size: ", len(subPopulation))
    return subPopulation

""" CROSSOVER """
def crossover(population):
    #Mix chromosomes in a generated sub-population
    for x in range(param.NUMBER_OF_PAIRS):
        #generate two random numbers and tranform them to interval [0, populationNumber]
        first = m.floor(bin.transformToInterval(random.uniform(0,1),0,1,0,param.POPULATION_SIZE-1))
        second = m.floor(bin.transformToInterval(random.uniform(0,1),0,1,0,param.POPULATION_SIZE-1))
        #swap chromosomes in new population
        temp = population[first]
        population[first] = population[second]
        population[second] = temp
    #Do recombination on chromosomes based on a random number
    for x in range(int(param.POPULATION_SIZE/2)):
        #Generate random number
        randomNumber = random.uniform(0,1)
        if(randomNumber < param.RECOMBINARION_PROB):
            population[2*x].recombine(population[2*x+1])
    return population

""" MUTATION """
def mutation(population):
    #Go over population, generate a random number which 
    #decides if chromosome is going to be mutated
    for x in range(param.POPULATION_SIZE):
        randomNumber = random.uniform(0,1)
        if(randomNumber < param.MUTATION_PROB):
            population[x].mutate()
    return population