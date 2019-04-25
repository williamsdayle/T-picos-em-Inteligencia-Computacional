from random import randint
import methods as mtd
import random
from datetime import datetime as dt
import operator
import csv
import matplotlib.pyplot as mt
import Cromossomo as cr
import math
T = 0.434526842


def crossOverNormalizado(lista):
    a = 0
    aux = cr.obj("",0)
    retorno  = []
    for h in range(len(lista) - 1):
        listaPaia = []
        listaPaib = []
        mutChar = ''
        cromossomoA = mtd.roleta(normalizacao(lista)).getBits()
        cromossomoB = mtd.roleta(normalizacao(lista)).getBits()
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
        filhoA = cr.obj(cromossomoA, mtd.avaliar_cromossomo(cromossomoA))
        filhoB = cr.obj(cromossomoB, mtd.avaliar_cromossomo(cromossomoB))
        retorno.append(filhoA)
        retorno.append(filhoB)
        h = h + 1
    return retorno

def mutacaoNormalizada (lista, n): #MUTAÇÃO DE UMA POSIÇÃO ESPECIFICA PASSADA COMO PARAMETRO
    retorno = []
    if n <= 9:
        for h in range(len(lista) - 1):
            listaPaia = []
            listaPaib = []
            mutChar = ''
            cromossomoA = mtd.roleta(normalizacao(lista)).getBits()
            cromossomoB = mtd.roleta(normalizacao(lista)).getBits()
            for i in range(len(cromossomoA)):
                listaPaia.append(cromossomoA[i])
            for i in range(len(cromossomoB)):
                    listaPaib.append(cromossomoB[i])
            mutChar = listaPaib[n]
            listaPaib[n] = listaPaia[n]
            listaPaia[n] = mutChar
            cromossomoA = "".join(listaPaia)
            cromossomoB = "".join(listaPaib)
            filhoA = cr.obj(cromossomoA, mtd.avaliar_cromossomo(cromossomoA))
            filhoB = cr.obj(cromossomoB, mtd.avaliar_cromossomo(cromossomoB))
            retorno.append(filhoA)
            retorno.append(filhoB)
            h = h + 1
    return retorno

def normalizacao(lista):
    lista = sorted(lista, key = cr.obj.getFitness)
    best = lista[0]
    for i in range(1,len(lista)):
        lista[i].setFitness(lista[i-1].getFitness() - T)
    return lista




def media(i,lista):
    aux = 0
    for j in range(i):
        aux = aux + lista[j].getFitness()
    if len(lista) > 0:
        return aux/len(lista)
    else:
        return 0

def desvioPadrao(i,lista):
    listaAuxiliar = []
    for j in range(i):
        listaAuxiliar.append(lista[j])
    med = media(i, listaAuxiliar)
    dp = 0
    desvio = 0
    for valores in listaAuxiliar:
        dp = dp + (valores.getFitness() - med)**2
    if len(listaAuxiliar) > 0:
        desvio = math.sqrt(round(dp,5))/len(listaAuxiliar)
    return abs(desvio)

def escalonamentoSigma(lista):
    list_prob = []
    ind = cr.obj("",0)
    for i in range(len(lista)):
        desv = desvioPadrao(i,lista)
        if desv == 0:
            for elements in lista:
                list_prob.append(1)
                break
        elif desv !=0:
            for elements in lista:
                t = ((lista[i].getFitness() - media(i, lista))/2*desvioPadrao(i,lista))
                valor = 1 + round(t,5)
                list_prob.append(valor)
    return list_prob

def roleta_normalizada(lista,lista_prob):
    r = random.random()
    selected_ind = lista[0]
    i = 0
    for ind in lista:
        if lista_prob[i] > r:
            break
        selected_ind = ind
        i = i + 1

    return selected_ind

def getMelhorCromossomo(lista):
    bestCr = cr.obj("",0)
    for elements in lista:
        if elements.getFitness() > bestCr.getFitness():
            bestCr.setFitness(elements.getFitness())
            bestCr.setBits("".join(elements.getBits()))
    return bestCr
