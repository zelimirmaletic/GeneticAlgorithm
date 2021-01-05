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
from mpl_toolkits.mplot3d import axes3d
import numpy as np


"""Make main polot of function"""
# Axis
x = np.linspace(fun.LOWER_X, fun.UPPER_X, 50)
y = np.linspace(fun.LOWER_Y, fun.UPPER_Y, 50)
#Ploting
X,Y = np.meshgrid(x,y)
Z = fun.mathFunction(X,Y)
figure = plt.figure()
ax = plt.axes(projection='3d')
ax.plot_surface(X,Y,Z, rstride=1, cstride=1, cmap='viridis',edgecolor='none')
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_zlabel('z')




globalExtremum = 0.0

""" Phase No.1 - Initialization Of The Population """
#Make a population of chromosomes
initialPopulation = phase.initializePopulation()
for chrom in initialPopulation:
    chrom.printChromosome()
#plot initial population
for chrom in initialPopulation:
    ax.scatter(chrom.getX(),chrom.getY() , fun.mathFunction(chrom.getX(),chrom.getY()),c="red",label="initial",marker=8)
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
        ax.scatter(chrom.getX(), chrom.getY(), fun.mathFunction(chrom.getX(),chrom.getY()),c="blue",label="subgeneration",marker=9)
    if(populationChangeCondition(localExtremum,globalExtremum,subPopulationFitnessScore,populationFitnessScore)):
        population = subPopulation
        populationFitnessScore = subPopulationFitnessScore
        globalExtremum=localExtremum
        print("POPULATION CHANGE")

print("Final population fitness score: ", populationFitnessScore)
population.sort(key=lambda e: e.fitnessValue, reverse=True)
ax.scatter(population[0].getX(),population[0].getY(), fun.mathFunction(population[0].getX(),population[0].getY()),c="green",label="best")
print("SOLUTION: ", fun.mathFunction(population[0].getX(),population[0].getY()))

ax.set(xlabel='x-axis', ylabel='y-axis',
       title='Genetic Algotithm')
ax.grid()
plt.show()
