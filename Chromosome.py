class Chromosome:
    #Data
    xCoordinate = 0.0
    xDNA = ""
    fitnessValue = 0.0

    def __init__(self, xCoordinate, xDNA):
        self.xDNA = xDNA
        self.xCoordinate = xCoordinate
    #Getters
    def getDNASequenceX(self):
        return self.xDNA
    def getX(self):
        return self.xCoordinate
    def getFitnessValues(self):
        return self.fittnessValue
    #Setters
    def setFitnessValue(self, fitnessValue):
        self.fitnessValue = fitnessValue

    def printChromosome(self):
        print("Chromosome")
        print(self.xCoordinate)
        print(self.xDNA)
        print(self.fitnessValue)
        print("------------")




    