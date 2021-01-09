""" 
GENETIC ALGORITHM
Želimir Maletić 11125/18 
Faculty of Electrical Engineering Banja Luka
2020
"""

"""
Pseudo-code:
START
Generate the initial population
Compute fitness 
REPEAT
    Selection 
    Crossover 
    Mutation 
    Compute fitness
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
#Axis
x = np.linspace(fun.LOWER_X, fun.UPPER_X, 50)
if(param.PLANE_INTERSECTION):
    y = np.linspace(0, 0.0000000001, 50)
else:
    y = np.linspace(fun.LOWER_Y, fun.UPPER_Y, 50)
#Ploting initial graph
X,Y = np.meshgrid(x,y)
Z = fun.mathFunction(X,Y)
figure = plt.figure(figsize=(10,10))
ax = plt.axes(projection='3d')
ax.plot_surface(X,Y,Z, rstride=1, cstride=1, alpha=0.5 ,cmap='viridis',edgecolor='none')
#ax.contour3D(X, Y, Z, 50, cmap='binary')
if(param.PLANE_INTERSECTION):
    ax.view_init(0, 0)
ax.set(xlabel='x-osa', ylabel='y-osa', zlabel='z-osa')
ax.set_title('Genetički algoritam', fontsize=14)

#Set a global extremum to an initial value
globalExtremum = 0.0

""" Phase No.1 - Initialization Of The Population """
#Make a population of chromosomes
initialPopulation = phase.initializePopulation()
#Plot initial population
ax.scatter(0.0,0.0,0.0,c="red",label="Inicijalna populacija",marker=9)
for chrom in initialPopulation:
    ax.scatter(chrom.getX(),chrom.getY() , fun.mathFunction(chrom.getX(),chrom.getY()),c="red",marker=8)

""" Phase No.2 - Fitness Function """
population, globalExtremum = phase.fitnessEvaluation(initialPopulation)
#Calculate population fitness score
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
    if(subPopulationFitnessScore == 0):
        break
    #print("SubPopulation fitness score: ",subPopulationFitnessScore)
    if(populationChangeCondition(localExtremum,globalExtremum,subPopulationFitnessScore,populationFitnessScore)):
        population = subPopulation
        populationFitnessScore = subPopulationFitnessScore
        globalExtremum = localExtremum
        print("POPULATION CHANGED")

#plot final population
ax.scatter(0.0,0.0,0.0,c="green",label="Finalna populacija",marker=8)
for chrom in population:
    ax.scatter(chrom.getX(), chrom.getY(), fun.mathFunction(chrom.getX(),chrom.getY()),c="green",marker=9)
print("Final population fitness score: ", populationFitnessScore)
#Sort population by fitness value
population.sort(key = lambda e: e.fitnessValue, reverse = True)
#Plot the best solution as a blue dot
x = population[0].getX()
y = population[0].getY()
z = fun.mathFunction(population[0].getX(),population[0].getY())
ax.scatter(x, y, z, c="blue", label="x = "+str(x)+"\ny = "+str(y)+"\nz = " + str(z))
print("==> SOLUTION: x= ",x," y= ",y," z= ", z)

#Show the plot
ax.legend(loc='upper right')
ax.grid()
plt.show()
