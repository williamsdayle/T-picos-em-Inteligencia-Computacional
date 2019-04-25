import matplotlib.pyplot as mt
import DEMethods as demt
import random
from random import randint
from math import floor
import numpy as np

MIN = -5.12
MAX = 5.12


#NUMEROS REAIS

def create_chromossome(tamanho):
    return [random.uniform(MIN, MAX) for x in range(tamanho)]

def de_jong_function(cromossomo):
    return sum([pow(x, 2) for x in cromossomo])

def avaliar_cromossomo_value(cromossomo):
    return (1/(de_jong_function(cromossomo) + 1))*1/100

def create_generation(tamanho):
    geracao = []
    for i in range(tamanho):
        geracao.append(create_chromossome(15))
    return geracao


def mutacao_real(lista):
    value_return = []
    for crom in lista:
        new_values = []
        pos = randint(0, 14)
        for i in range(len(crom)):
            value_mutate = random.random()
            crom[pos] = value_mutate
            new_values.append(crom[i])
        value_return.append(new_values)
    return value_return


def get_best_crom(lista):
    best_positive = 0.0
    best_negative = 0.0
    for crom in lista:
        for i in range(len(crom)):
            if crom[i] > 0:
                if crom[i] > best_positive:
                    best_positive = crom[i]
        for i in range(len(crom)):
            if crom[i] > 0:
                if crom[i] < best_positive:
                    best_positive = crom[i]
        for i in range(len(crom)):
            if crom[i] < 0:
                if crom[i] < best_negative:
                    best_negative = crom[i]
        for i in range(len(crom)):
            if crom[i] < 0:
                if crom[i] > best_negative:
                    best_negative = crom[i]
    if abs(best_negative) > best_positive:
        return best_positive
    else:
        return best_negative


def cross_over_aritmetico(geracao):
    lambdaA = 0.3
    lambdaB = 0.5
    new_generation = []
    for values in geracao:
        new_values = []
        for i in range(len(values) - 1):
            cromossomoA = values[i]
            cromossomoB = values[i+1]
            filhoA = cromossomoA*lambdaA + (1 - lambdaA) * cromossomoB
            filhoB = cromossomoB*lambdaB + (1 - lambdaB) * cromossomoA
            new_values.append(filhoA)
            new_values.append(filhoB)
        new_generation.append(new_values)
    return new_generation


def gerarGrafico(fitness,valores):
    mt.title("Valores de Fitness da geração")
    mt.plot(fitness, valores)
    mt.xlabel("Melhor valor na geração")
    mt.ylabel("Numero da geração")
    mt.show()


def mutacao_DE(schema,lista):
   return demt.mutacao(schema,lista)

