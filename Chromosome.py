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

    def setY(self, value):
        self.yCoordinate = value
    def setDnaSequenceY(self, sequence):
        self.yDNA = sequence
    

    def setFitnessValue(self, fitnessValue):
        self.fitnessValue = fitnessValue
    def setProbability(self,probability):
        self.probability = probability
    def setRouletteBoundary(self, boundary):
        self.rouletteBoundary = boundary


    #Methond for recombining two chromosomes
    def recombine(self, otherChromosome):
        #Single-point recombination
        if(param.RECOMBINARION_METHOD == 1):
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
        #Swap x coordinates recombination
        elif(param.RECOMBINARION_METHOD == 2):
            #Simply swap y coordinates in chromosomes
            y1 = self.getY()
            y2 = otherChromosome.getY()
            #Set new coordinates 
            self.setY(y2)
            self.setDnaSequenceY(bin.codeBinary(param.PRECISION,y2,fun.LOWER_Y,fun.UPPER_Y))
            otherChromosome.setY(y1)
            otherChromosome.setDnaSequenceY(bin.codeBinary(param.PRECISION,y1,fun.LOWER_Y,fun.UPPER_Y))
        #Swap y coordinates recombination
        elif(param.RECOMBINARION_METHOD == 3):
            #Simply swap x coordinates in chromosomes
            x1 = self.getX()
            x2 = otherChromosome.getX()
            #Set new coordinates
            self.setX(x2)
            self.setDnaSequenceX(bin.codeBinary(param.PRECISION,x2,fun.LOWER_X,fun.UPPER_X))
            otherChromosome.setX(x1)
            otherChromosome.setDnaSequenceX(bin.codeBinary(param.PRECISION,x1,fun.LOWER_X,fun.UPPER_X))
        #Uniform recombination
        elif(param == 4):
            """X-coordinate"""
            binarySequence1 = self.getDNASequenceX()
            binarySequence2 = otherChromosome.getDNASequenceX()
            newSequence1 = ""
            newSequence2 = ""
            flip = True
            for gene1,gene2 in zip(binarySequence1,binarySequence2):
                if(flip):
                    newSequence1 += gene1
                    newSequence2 += gene2
                else:
                    newSequence1 += gene2
                    newSequence2 += gene1
                flip = not flip
            self.setDnaSequenceX(newSequence1)
            self.setX(bin.decodeBinary(newSequence1,fun.LOWER_X,fun.UPPER_X))
            otherChromosome.setDnaSequenceX(newSequence2)
            otherChromosome.setX(bin.decodeBinary(newSequence2,fun.LOWER_X,fun.UPPER_X))

            """Y-coordinate"""
            binarySequence1 = self.getDNASequenceY()
            binarySequence2 = otherChromosome.getDNASequenceY()
            newSequence1 = ""
            newSequence2 = ""
            flip = True
            for gene1,gene2 in zip(binarySequence1,binarySequence2):
                if(flip):
                    newSequence1 += gene1
                    newSequence2 += gene2
                else:
                    newSequence1 += gene2
                    newSequence2 += gene1
                flip = not flip
            self.setDnaSequenceY(newSequence1)
            self.setY(bin.decodeBinary(newSequence1,fun.LOWER_Y,fun.UPPER_Y))
            otherChromosome.setDnaSequenceY(newSequence2)
            otherChromosome.setY(bin.decodeBinary(newSequence2,fun.LOWER_Y,fun.UPPER_Y))

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

