"""General algorithm parameters"""
RECOMBINARION_PROB = 0.25
MUTATION_PROB = 0.05
POPULATION_SIZE = 300
PRECISION = 2
#We have different recombination methods: 
# 1 - single point recombinatin
# 2 - swap y coordinates recombination 
# 3 -swap x coordinates recombination 
# 4 - uniform recombination 
RECOMBINARION_METHOD = 1
EXTREMUM = "min" #can be min or max
NUMBER_OF_PAIRS = int(POPULATION_SIZE/2)
NUMBER_OF_ITERATIONS = 25
#Three selection methods are implemented: roulette, tournament and elite
SELECTION_METHOD = "tournament"
#For tournament selection we define a constant which determines
#the selection pressure
TOURNAMENT_PRESSURE = 2
#Intersect surface area with a plane
PLANE_INTERSECTION = False

#Setters are defined for the purpose of dynamicliy changing parameters in Simulation.py
