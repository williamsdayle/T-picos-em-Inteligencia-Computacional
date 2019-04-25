import matplotlib.pyplot as mt
import random
from random import randint
from math import floor
import numpy as np

MIN = -5.12
MAX = 5.12
NP = 100
CR = 0.7
F = 0.63



def mutacao(schema, lista):
    alpha = 0.0
    beta = 0.0
    sigma = 0.0
    lista_U = []
    if schema == 1: #DE/RAND/1/BIN
        for cromo in lista:
            new_crom = []
            for crom in range(len(cromo)):
                alpha = randint(0, len(cromo)-1)
                beta = randint(0, len(cromo)-1)
                sigma = randint(0, len(cromo)-1)
                u = get_U(alpha, beta, sigma, cromo)
                if u > CR:
                    new_crom.append(crom)
                if u < CR:
                    new_crom.append(u)
            lista_U.append(new_crom)
        return lista_U

    elif schema == 2: #DE/RAND/2
        for i in lista:
            new_crom = []
            for crom in range(len(i)-4):
                u = get_U_schema(crom, crom+2, crom+1, crom+4, crom+3,i)
                if u > CR:
                    new_crom.append(crom)
                elif u < CR:
                    new_crom.append(u)
            lista_U.append(new_crom)
        return lista_U
    elif schema == 3: #DE/BEST/2
        for i in lista:
            new_crom = []
            for crom in range(len(i)-3):
                best = get_best_value(i)
                best_pos = get_best_post(best, i)
                u = get_U_schema(best_pos, crom+1, crom, crom+3, crom+2, i)
                if u > CR:
                    new_crom.append(crom)
                elif u < CR:
                    new_crom.append(u)
            lista_U.append(new_crom)
        return lista_U


def get_best_value(list_cromo):
    best = 0
    for crom in list_cromo:
        if crom > best:
            best = crom
    return best

def get_U(alpha, beta, gama, crom):
    value = crom[beta] - crom[gama]
    return crom[alpha] + F * value

def get_U_schema(alpha,beta,gama,x1,x2, crom):
    valuex = crom[beta] - crom[gama]
    valuey = crom[x1] - crom[x2]
    return crom[alpha] + F * valuex + F * valuey

def get_best_post(best, lista):
    for i in range(len(lista)):
        if lista[i] == best:
            return i
