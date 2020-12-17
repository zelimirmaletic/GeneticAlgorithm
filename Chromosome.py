import random
import math as m 
import BinaryCoding as bin
import function as fun
import parameters as param 

class Chromosome:
    #Data
    xCoordinate = 0.0
    xDNA = ""
    fitnessValue = 0.0
    probability = 0.0
    rouletteBoundary = 0.0

    def __init__(self, xCoordinate, xDNA):
        self.xDNA = xDNA
        self.xCoordinate = xCoordinate
    #Getters
    def getDNASequenceX(self):
        return self.xDNA
    def getX(self):
        return self.xCoordinate
    def getFitnessValue(self):
        return self.fitnessValue
    def getProbability(self):
        return self.probability
    def getBoundary(self):
        return self.rouletteBoundary
    #Setters
    def setX(self, value):
        self.xCoordinate = value
    def setFitnessValue(self, fitnessValue):
        self.fitnessValue = fitnessValue
    def setProbability(self, populationFitnessScore):
        self.probability = self.fitnessValue / populationFitnessScore
    def setRouletteBoundary(self, boundary):
        self.rouletteBoundary = boundary
    def setDnaSequenceX(self, sequence):
        self.xDNA = sequence

    #Methond for recombining two chromosomes
    def recombine(self, otherChromosome):
        #Choose a point on which we break DNA and interchange right parts
        randomNumber = random.uniform(0,1)
        #Transform random number to a segment [1 - len(DNA)]
        disectionPoint = m.floor(bin.transformToInterval(randomNumber,0,1,1,len(self.xDNA)))
        #Now disect both DNAs and get sequence right of disection point
        sequence1 = self.xDNA[disectionPoint:]
        sequence2 = (otherChromosome. getDNASequenceX())[disectionPoint:]
        #Interchange the parts of DNA right from disection point
        self.setDnaSequenceX(self.xDNA.replace(self.xDNA[disectionPoint:], sequence2))
        dna = otherChromosome.getDNASequenceX()
        otherChromosome.setDnaSequenceX(dna.replace(dna[disectionPoint:],sequence1))
        #Regenerate coordinates from new DNAs
        self.setX(bin.decodeBinary(param.PRECISION, self.getDNASequenceX(), fun.LOWER_X, fun.UPPER_X))
    
    #Method for mutating a chromosome
    def mutate(self):
        #Generate random number
        randomNumber = random.uniform(0,1)
        #Transform to interval [0, len(DNA)]
        index = m.floor(bin.transformToInterval(randomNumber,0,1,0,len(self.xDNA)))
        #Invert bit in DNA sequence
        dnaList = list(self.xDNA)
        if(dnaList[index]=='1'):
            dnaList[index]='0'
        else:
            dnaList[index]='1'
        self.setDnaSequenceX("".join(dnaList))
        #Regenerate coordinates from new DNAs
        self.setX(bin.decodeBinary(param.PRECISION, self.getDNASequenceX(), fun.LOWER_X, fun.UPPER_X))



    def printChromosome(self):
        print("Chromosome ")
        print(self.xCoordinate)
        print(self.xDNA)
        print(self.fitnessValue)
        print(self.probability)
        print(self.rouletteBoundary)
        print("------------")

    