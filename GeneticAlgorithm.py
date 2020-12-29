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
from AlgorithmPhaseFunctions import initializePopulation, populationChangeCondition
import random
import math as m
import function as fun
import AlgorithmPhaseFunctions as phase
import BinaryCoding as bin
import Chromosome as hrom
import parameters as param
import matplotlib
import matplotlib.pyplot as plt
import numpy as np


"""Make main polot of function"""
# Data for plotting
x = np.arange(fun.LOWER_X,fun.UPPER_X, 0.1)
y=[]
for value in x:
    y.append(fun.mathFunction(value))
fig, ax = plt.subplots()
ax.plot(x, y)

globalExtremum = 0.0

""" Phase No.1 - Initialization Of The Population """
#Make a population of chromosomes
initialPopulation = phase.initializePopulation()
#plot initial population
for chrom in initialPopulation:
    ax.scatter(chrom.getX(), fun.mathFunction(chrom.getX()),c="red",label="initial",marker=8)
""" Phase No.2 - Fitness Function """
population,globalExtremum = phase.fitnessEvaluation(initialPopulation)
populationFitnessScore = bin.calculatePopulationFitnessScore(population)
print("Initial population fitness score: ", populationFitnessScore)

#Make a new subpopulation
subPopulation = []

for x in range(param.NUMBER_OF_ITERATIONS):
    """ Phase No.3 - SELECTION """
    subPopulation = phase.selection(population, param.SELECTION_METHOD)
    """ Phase No.4 Recombination/Crossover """
    subPopulation = phase.crossover(subPopulation)
    """ Phase No.5 Mutation """
    subPopulation = phase.mutation(subPopulation)
    """ Phase No.6 (Re)Calculate Fitness """
    #Make a list of chromosome x coordinates
    subPopulation,localExtremum = phase.fitnessEvaluation(subPopulation)
    subPopulationFitnessScore = bin.calculatePopulationFitnessScore(subPopulation)
    print("SubPopulation fitness score: ",subPopulationFitnessScore)
    #plot subpopulation
    for chrom in subPopulation:
        ax.scatter(chrom.getX(), fun.mathFunction(chrom.getX()),c="blue",label="subgeneration",marker=9)
    if(populationChangeCondition(localExtremum,globalExtremum,subPopulationFitnessScore,populationFitnessScore)):
        population = subPopulation
        populationFitnessScore = subPopulationFitnessScore
        globalExtremum=localExtremum
        print("POPULATION CHANGE")

print("Final population fitness score: ", populationFitnessScore)
population.sort(key=lambda e: e.fitnessValue, reverse=True)
ax.scatter(population[0].getX(), fun.mathFunction(population[0].getX()),c="green",label="best")
print("SOLUTION: ", fun.mathFunction(population[0].getX()))

ax.set(xlabel='x-axis', ylabel='y-axis',
       title='Genetic Algotithm f(x) = x^2 + 10*cos(5-x)')
ax.grid()
plt.show()
