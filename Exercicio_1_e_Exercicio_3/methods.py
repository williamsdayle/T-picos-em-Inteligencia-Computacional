from random import randint
import random
from datetime import datetime as dt
import operator
import csv
import matplotlib.pyplot as mt
import imp
cr = imp.load_source('util', '../Exercicio_1_e_Exercicio_3/Cromossomo.py')
import math
T = 3.33
listaValor = []


def get_decimal(n): #TRANSFORMAR EM DECIMAL OS VALORES BINARIOS GERADOS
    x = 0
    y = 0
    w = 0
    if len(n) > 6:
        xx = n[0],n[1],n[2]
        yy = n[3], n[4]
        ww = n[5],n[6],n[7],n[8],n[9]
        for i in range(len(xx)):
            if xx[i] == "1":
                x = x + 2**i
        for i in range(2):
            if yy[i] == "1":
                y = y + 2**i
        for i in range(len(ww)):
            if ww[i] == "1"	:
                w = w + 2**i
        return str(x)+"/"+ str(y)+"/"+ str(w)




def mutacao (lista, n): #MUTAÇÃO DE UMA POSIÇÃO ESPECIFICA PASSADA COMO PARAMETRO
    retorno = []
    if n <= 9:
        for h in range(len(lista) - 1):
            listaPaia = []
            listaPaib = []
            mutChar = ''
            cromossomoA = roleta(lista).getBits()
            cromossomoB = roleta(lista).getBits()
            for i in range(len(cromossomoA)):
                listaPaia.append(cromossomoA[i])
            for i in range(len(cromossomoB)):
                    listaPaib.append(cromossomoB[i])
            mutChar = listaPaib[n]
            listaPaib[n] = listaPaia[n]
            listaPaia[n] = mutChar
            cromossomoA = "".join(listaPaia)
            cromossomoB = "".join(listaPaib)
            filhoA = cr.obj(cromossomoA, avaliar_cromossomo(cromossomoA))
            filhoB = cr.obj(cromossomoB, avaliar_cromossomo(cromossomoB))
            retorno.append(filhoA)
            retorno.append(filhoB)
            h = h + 1
    return retorno



def cross_over(lista):
    a = 0
    aux = cr.obj("",0)
    retorno  = []
    for h in range(len(lista) - 1):
        listaPaia = []
        listaPaib = []
        mutChar = ''
        cromossomoA = roleta(lista).getBits()
        cromossomoB = roleta(lista).getBits()
        for i in range(len(cromossomoA)):
            listaPaia.append(cromossomoA[i])
        for i in range(len(cromossomoB)):
            listaPaib.append(cromossomoB[i])
        left = randint(0,9)
        right = randint(0,9)
        if(left > right):
            p = right
            right = left
            left = p
        for i in range(left,right):
             mutChar = listaPaib[i]
             listaPaib[i] = listaPaia[i]
             listaPaia[i] = mutChar
        cromossomoA = "".join(listaPaia)
        cromossomoB = "".join(listaPaib)
        filhoA = cr.obj(cromossomoA, avaliar_cromossomo(cromossomoA))
        filhoB = cr.obj(cromossomoB, avaliar_cromossomo(cromossomoB))
        retorno.append(filhoA)
        retorno.append(filhoB)
        h = h + 1
    return retorno

def avaliar(valor):
    a = 52
    return (valor * 100)/a


def get_melhor_cromossomo(lista):
    bestCr = cr.obj("",0)
    for elements in lista:
        if elements.getFitness() > bestCr.getFitness():
            bestCr.setFitness(elements.getFitness())
            bestCr.setBits("".join(elements.getBits()))
    return bestCr
    


def gerarGrafico(fitness,valores):
    mt.title("Valores de Fitness da geração")
    mt.plot(fitness,valores)
    mt.xlabel("Maior valor na geração")
    mt.ylabel("Numero da geração")
    mt.show()
            


def avaliar_cromossomo(cromossomo):
    decimalCod = get_decimal(cromossomo)
    decimal = decimalCod.split("/")
    a = decimal[0]
    b = decimal[1]
    c = decimal[2]
    x = int(a)
    y = int(b)
    w = int(c)
    valor = 2*x + y**2 + w;
    fitness = avaliar(valor)
    if fitness > 100:
        return 0
    return fitness




def create_generation(tam):
        listaObj = []
        aux = ""
        for i in range(tam):
            for j in range(10):
                aux+=str(randint(0,1))
            listaObj.append(cr.obj(aux, avaliar_cromossomo(aux)))
            aux = ""
        return listaObj


def roleta(lista):
    fitness_sum = sum([ind.getFitness() for ind in lista])
    probability_offset = 0
    prob = []
    i = 0
    for ind in lista:
        prob.append(probability_offset + (ind.getFitness() / fitness_sum))
        probability_offset = probability_offset + prob[i]
        i = i + 1
    r = random.random()
    selected_ind = lista[0]
    i = 0
    for ind in lista:
        if prob[i] > r:
            break
        selected_ind = ind
        i = i + 1

    return selected_ind






