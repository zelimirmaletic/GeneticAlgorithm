import Chromosome as chrom
import BinaryCoding as bin

def savePopulation(population):
    stream = open('Population.txt','w+')
    for chrom in population:
        stream.write(str(chrom.getX()))
        stream.write(" ")
        stream.write(str(chrom.getY()))
        stream.write("\n")
    stream.close()

def loadPopulation(fileName):
    stream = open(fileName,'r+')
    population = []
    for line in stream:
        coordinates = str.split(line)
        coordinateX = float(coordinates[0])
        coordinateY = float(coordinates[1])
        newChromosome = chrom.Chromosome(coordinateX, bin.codeBinary(2,coordinateX,-3,3),coordinateY, bin.codeBinary(2,coordinateY,-4,4))
        population.append(newChromosome)
    return population