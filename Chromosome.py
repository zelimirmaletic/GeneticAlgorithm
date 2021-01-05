import random
import math as m 
import BinaryCoding as bin
import function as fun
import parameters as param 

class Chromosome:
    #Data
    xCoordinate = 0.0
    xDNA = ""
    yCoordinate = 0.0
    yDNA = ""

    fitnessValue = 0.0
    probability = 0.0
    rouletteBoundary = 0.0

    def __init__(self, xCoordinate, xDNA,yCoordinate, yDNA):
        self.xDNA = xDNA
        self.xCoordinate = xCoordinate
        self.yDNA = yDNA
        self.yCoordinate = yCoordinate
    #Getters
    def getDNASequenceX(self):
        return self.xDNA
    def getX(self):
        return self.xCoordinate
    def getDNASequenceY(self):
        return self.yDNA
    def getY(self):
        return self.yCoordinate

    def getFitnessValue(self):
        return self.fitnessValue
    def getProbability(self):
        return self.probability
    def getBoundary(self):
        return self.rouletteBoundary

    #Setters
    def setX(self, value):
        self.xCoordinate = value
    def setDnaSequenceX(self, sequence):
        self.xDNA = sequence
    def setDnaSequenceY(self, value):
        self.yCoordinate = value
    def setY(self, sequence):
        self.yDNA = sequence
 

    def setFitnessValue(self, fitnessValue):
        self.fitnessValue = fitnessValue
    def setProbability(self,probability):
        self.probability = probability
    def setRouletteBoundary(self, boundary):
        self.rouletteBoundary = boundary


    #Methond for recombining two chromosomes
    def recombine(self, otherChromosome):
        """X-coordinate"""
        #Choose a point on which we break DNA and interchange right parts
        randomNumber = random.uniform(0,1)
        #Transform random number to a segment [1 - len(DNA)]
        disectionPoint = m.floor(bin.transformToInterval(randomNumber,0,1,1,len(self.xDNA)))
        #Now disect both DNAs and get sequence right of disection point
        sequence1 = self.xDNA[disectionPoint:]
        sequence2 = (otherChromosome.getDNASequenceX())[disectionPoint:]
        #Interchange the parts of DNA right from disection point
        self.setDnaSequenceX(self.xDNA.replace(self.xDNA[disectionPoint:], sequence2))
        dna = otherChromosome.getDNASequenceX()
        otherChromosome.setDnaSequenceX(dna.replace(dna[disectionPoint:],sequence1))
        #Regenerate coordinates from new DNAs
        self.setX(bin.decodeBinary(self.getDNASequenceX(), fun.LOWER_X, fun.UPPER_X))
        otherChromosome.setX(bin.decodeBinary(otherChromosome.getDNASequenceX(), fun.LOWER_X, fun.UPPER_X))

        """Y-coordinate"""
        #Choose a point on which we break DNA and interchange right parts
        randomNumber = random.uniform(0,1)
        #Transform random number to a segment [1 - len(DNA)]
        disectionPoint = m.floor(bin.transformToInterval(randomNumber,0,1,1,len(self.yDNA)))
        #Now disect both DNAs and get sequence right of disection point
        sequence1 = self.yDNA[disectionPoint:]
        sequence2 = (otherChromosome.getDNASequenceY())[disectionPoint:]
        #Interchange the parts of DNA right from disection point
        self.setDnaSequenceY(self.yDNA.replace(self.yDNA[disectionPoint:], sequence2))
        dna = otherChromosome.getDNASequenceY()
        otherChromosome.setDnaSequenceY(dna.replace(dna[disectionPoint:],sequence1))
        #Regenerate coordinates from new DNAs
        self.setY(bin.decodeBinary(self.getDNASequenceY(), fun.LOWER_Y, fun.UPPER_Y))
        otherChromosome.setY(bin.decodeBinary(otherChromosome.getDNASequenceY(), fun.LOWER_Y, fun.UPPER_Y))



    #Method for mutating a chromosome
    def mutate(self):
        """X-coordinate"""
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
        self.setX(bin.decodeBinary(self.getDNASequenceX(), fun.LOWER_X, fun.UPPER_X))
        
        """Y-coordinate"""
        #Generate random number
        randomNumber = random.uniform(0,1)
        #Transform to interval [0, len(DNA)]
        index = m.floor(bin.transformToInterval(randomNumber,0,1,0,len(self.yDNA)))
        #Invert bit in DNA sequence
        dnaList = list(self.yDNA)
        if(dnaList[index]=='1'):
            dnaList[index]='0'
        else:
            dnaList[index]='1'
        self.setDnaSequenceY("".join(dnaList))
        #Regenerate coordinates from new DNAs
        self.setY(bin.decodeBinary(self.getDNASequenceY(), fun.LOWER_Y, fun.UPPER_Y))

    def printChromosome(self):
        print("Chromosome ")
        print("     X-coordinate: ",self.xCoordinate)
        print("     Y-coordinate: ",self.yCoordinate)
        print("     X-dna: ",self.xDNA)
        print("     Y-dna: ",self.yDNA)
        print("     fitness value: ",self.fitnessValue)
        print("     probability: ",self.probability)
        print("     roulette boundary: ", self.rouletteBoundary)
        print("------------")

    