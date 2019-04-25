from random import randint
class obj(object):
    def __init__(self,bits,fitness):
        self.bits = bits
        self.fitness = fitness
    def getBits(self):
        return self.bits
    def getFitness(self):
        return round(self.fitness,2)
    def setBits(self,bits):
        self.valor = bits
    def setFitness(self,fitness):
        self.fitness = fitness



    



    


    
    

