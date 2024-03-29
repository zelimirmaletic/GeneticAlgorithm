#Here are stored function which represent the consecutive phases of the genetic algorithm
#Libraries
import random
import math as m
import function as fun
import BinaryCoding as bin
import Chromosome as hrom
import parameters as param
import SavePopulation as save

""" POPULATION INITIALIZATION """
#Function for making an initial population
def initializePopulation():
    population = []
    #Generate a population of random numbers
    for i in range(param.POPULATION_SIZE):
        #generate a random number from [0,1] interval
        randomNumber1 = random.uniform(0,1)
        randomNumber2 = random.uniform(0,1)
        #Translate generated number into a point from function extremum interval
        if(param.PLANE_INTERSECTION):
            coordinateX = 0.0
        else:
            coordinateX = bin.transformToInterval(randomNumber1,0,1,fun.LOWER_X, fun.UPPER_X)
        coordinateY = bin.transformToInterval(randomNumber2,0,1,fun.LOWER_Y, fun.UPPER_Y)
        #code point in binary
        binarySequenceX = bin.codeBinary(param.PRECISION, coordinateX, fun.LOWER_X, fun.UPPER_X)
        binarySequenceY = bin.codeBinary(param.PRECISION, coordinateY, fun.LOWER_Y, fun.UPPER_Y)
        #make a new chromosome
        newChromosome = hrom.Chromosome(coordinateX, binarySequenceX, coordinateY, binarySequenceY)
        #add it to the population
        population.append(newChromosome)
    #save.savePopulation(population)
    #population = save.loadPopulation("Population.txt")
    #calculate initial fitness values
    coordinatesX = []
    coordinatesY = []
    for chrom in population:
        coordinatesX.append(chrom.getX())
        coordinatesY.append(chrom.getY())
    functionValues = []
    for x,y in zip(coordinatesX,coordinatesY):
        functionValues.append(fun.mathFunction(x,y))
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
        functionValues.append(fun.mathFunction(chromosome.getX(), chromosome.getY()))
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
        if(param.EXTREMUM == "min" and value < extremumValue):
            extremumValue = value
        elif(param.EXTREMUM == "max" and value > extremumValue):
            extremumValue = value
    return population,extremumValue

""" SELECTION """
def selection(population, selectionMethod):
    if(selectionMethod=="roulette"):
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
        return subPopulation

    elif(selectionMethod=="tournament"):
        #Make an empty subpopulation
        subPopulation = []
        for i in range(param.POPULATION_SIZE):
            #make a list of randomly selected chromosomes
            randomlySelectedChromosomes = []
            for i in range(param.TOURNAMENT_PRESSURE):
                randomNumber = random.uniform(0,1)
                index = int(bin.transformToInterval(randomNumber,0,1,0,param.TOURNAMENT_PRESSURE))
                randomlySelectedChromosomes.append(population[index])
            randomlySelectedChromosomes.sort(key=lambda e:e.fitnessValue, reverse=True)
            subPopulation.append(randomlySelectedChromosomes[0])
        return subPopulation

    elif(selectionMethod == "elite"):
        subPopulation = []
        sortedPopulation = population
        sortedPopulation.sort(key=lambda e:e.fitnessValue, reverse=True)
        for x in range(int(param.POPULATION_SIZE/2)):
            subPopulation.append(sortedPopulation[x])
            subPopulation.append(sortedPopulation[x])
        return subPopulation
    else:
        print("Selection method error!")

""" CROSSOVER/RECOMBINATION """
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

#When to change population?
def populationChangeCondition(localExtremum, globalExtremum, subPopulationScore, populationScore):
    if(param.EXTREMUM == "max"):
        if(localExtremum >= globalExtremum ):#and subPopulationScore >= populationScore):
            return True
    if(param.EXTREMUM == "min"):
        if(localExtremum <= globalExtremum):# and subPopulationScore >= populationScore):
            return True
    return False

