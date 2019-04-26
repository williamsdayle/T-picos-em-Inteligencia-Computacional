import matplotlib.pyplot as mt
import random as rd
from random import randint
from math import floor
import numpy as np
import Constantes as ct
import DEMethods as dem



def gerar_seed_aleatoria(pos):
    aleatorio = np.random.randint(9, size=(1, 9))
    return aleatorio[0][pos]



def verificar_valores_sub_matriz(lista):
    valores_faltantes = 0
    for values in lista:
        if values not in ct.VALORES_NECESSARIOS:
            valores_faltantes = valores_faltantes + 1
    return valores_faltantes



def verificar_valores_coluna(lista):
    valores_faltantes = 0
    for values in lista:
        if values not in ct.VALORES_NECESSARIOS:
            valores_faltantes = valores_faltantes + 1
    return valores_faltantes



def get_fitness(value):
    return 1/value



def create_chromossome_dificil():
    dificil = ct.DIFICIL
    i = 0
    j = 0
    lista_retorno = []
    lista = matrix_to_array(dificil)
    for values in lista:
        if values == 0:
            lista_retorno.append(gerar_seed_aleatoria(5))
        else:
            lista_retorno.append(values)
    return lista_retorno



def create_chromossome_medio():
    medio = ct.MEDIO
    i = 0
    j = 0
    lista_retorno = []
    lista = matrix_to_array(medio)
    for values in lista:
        if values == 0:
            lista_retorno.append(gerar_seed_aleatoria(3))
        else:
            lista_retorno.append(values)
    return lista_retorno


def create_chromossome_facil():
    facil = ct.FACIL
    i = 0
    j = 0
    lista_retorno = []
    lista = matrix_to_array(facil)
    for values in lista:
        if values == 0:
            lista_retorno.append(gerar_seed_aleatoria(3))
        else:
            lista_retorno.append(values)
    return lista_retorno


def matrix_to_array(matrix):
    i = 0
    j = 0
    lista = []
    for linhas in matrix:
        j = 0
        for colunas in matrix:
            lista.append(matrix[i][j])
            j = j + 1
        i = i + 1
    return lista



def create_generation(value, tamanho):
    if value == 1:
        geracao = []
        for i in range(tamanho):
            geracao.append(create_chromossome_facil())
        return geracao
    if value == 2:
        geracao = []
        for i in range(tamanho):
            matrix = create_chromossome_medio()
            geracao.append(matrix)
        return geracao
    if value == 3:
        geracao = []
        for i in range(tamanho):
            geracao.append(create_chromossome_dificil())
        return geracao



def get_sub_matrix(x, y, lista): #x e y são as cordenadas do jogo
    lista_valores_sub_matrix = []
    if y == 0 :
        if x == 0:
            lista_valores_sub_matrix.append(lista[0])#0
            lista_valores_sub_matrix.append(lista[1])#1
            lista_valores_sub_matrix.append(lista[2])#2
            lista_valores_sub_matrix.append(lista[9])#0
            lista_valores_sub_matrix.append(lista[10])#1
            lista_valores_sub_matrix.append(lista[11])#2
            lista_valores_sub_matrix.append(lista[18])#0
            lista_valores_sub_matrix.append(lista[19])#1
            lista_valores_sub_matrix.append(lista[20])#2
        elif x == 1:
            lista_valores_sub_matrix.append(lista[27])
            lista_valores_sub_matrix.append(lista[28])
            lista_valores_sub_matrix.append(lista[29])
            lista_valores_sub_matrix.append(lista[36])
            lista_valores_sub_matrix.append(lista[37])
            lista_valores_sub_matrix.append(lista[38])
            lista_valores_sub_matrix.append(lista[45])
            lista_valores_sub_matrix.append(lista[46])
            lista_valores_sub_matrix.append(lista[47])

        elif x == 2:
            lista_valores_sub_matrix.append(lista[54])
            lista_valores_sub_matrix.append(lista[55])
            lista_valores_sub_matrix.append(lista[56])
            lista_valores_sub_matrix.append(lista[63])
            lista_valores_sub_matrix.append(lista[64])
            lista_valores_sub_matrix.append(lista[65])
            lista_valores_sub_matrix.append(lista[72])
            lista_valores_sub_matrix.append(lista[73])
            lista_valores_sub_matrix.append(lista[74])

    elif y == 1 :
        if x == 0:
            lista_valores_sub_matrix.append(lista[3])#0
            lista_valores_sub_matrix.append(lista[4])#1
            lista_valores_sub_matrix.append(lista[5])#2
            lista_valores_sub_matrix.append(lista[12])#0
            lista_valores_sub_matrix.append(lista[13])#1
            lista_valores_sub_matrix.append(lista[14])#2
            lista_valores_sub_matrix.append(lista[21])#0
            lista_valores_sub_matrix.append(lista[22])#1
            lista_valores_sub_matrix.append(lista[23])#2
        elif x == 1:
            lista_valores_sub_matrix.append(lista[30])#0
            lista_valores_sub_matrix.append(lista[31])#1
            lista_valores_sub_matrix.append(lista[32])#2
            lista_valores_sub_matrix.append(lista[39])#0
            lista_valores_sub_matrix.append(lista[40])#1
            lista_valores_sub_matrix.append(lista[41])#2
            lista_valores_sub_matrix.append(lista[48])#0
            lista_valores_sub_matrix.append(lista[49])#1
            lista_valores_sub_matrix.append(lista[50])#2
        elif x == 2:
            lista_valores_sub_matrix.append(lista[57])#0
            lista_valores_sub_matrix.append(lista[58])#1
            lista_valores_sub_matrix.append(lista[59])#2
            lista_valores_sub_matrix.append(lista[66])#0
            lista_valores_sub_matrix.append(lista[67])#1
            lista_valores_sub_matrix.append(lista[68])#2
            lista_valores_sub_matrix.append(lista[75])#0
            lista_valores_sub_matrix.append(lista[76])#1
            lista_valores_sub_matrix.append(lista[77])#2

    elif y == 2 :
        if x == 0:
            lista_valores_sub_matrix.append(lista[6])#0
            lista_valores_sub_matrix.append(lista[7])#1
            lista_valores_sub_matrix.append(lista[8])#2
            lista_valores_sub_matrix.append(lista[15])#0
            lista_valores_sub_matrix.append(lista[16])#1
            lista_valores_sub_matrix.append(lista[17])#2
            lista_valores_sub_matrix.append(lista[24])#0
            lista_valores_sub_matrix.append(lista[25])#1
            lista_valores_sub_matrix.append(lista[26])#2
        elif x == 1:
            lista_valores_sub_matrix.append(lista[33])#0
            lista_valores_sub_matrix.append(lista[34])#1
            lista_valores_sub_matrix.append(lista[35])#2
            lista_valores_sub_matrix.append(lista[42])#0
            lista_valores_sub_matrix.append(lista[43])#1
            lista_valores_sub_matrix.append(lista[44])#2
            lista_valores_sub_matrix.append(lista[51])#0
            lista_valores_sub_matrix.append(lista[52])#1
            lista_valores_sub_matrix.append(lista[53])#2
        elif x == 2:
            lista_valores_sub_matrix.append(lista[60])#0
            lista_valores_sub_matrix.append(lista[61])#1
            lista_valores_sub_matrix.append(lista[62])#2
            lista_valores_sub_matrix.append(lista[69])#0
            lista_valores_sub_matrix.append(lista[70])#1
            lista_valores_sub_matrix.append(lista[71])#2
            lista_valores_sub_matrix.append(lista[78])#0
            lista_valores_sub_matrix.append(lista[79])#1
            lista_valores_sub_matrix.append(lista[80])#2
    return lista_valores_sub_matrix

def get_valor_mesma_coluna(x, y, lista):
    lista_valores_mesma_coluna = []
    for i in range(9):
        y = 0
        y = y + i
        for j in range(9):
            lista_valores_mesma_coluna.append(lista[y])
            y = y + 9
    return lista_valores_mesma_coluna



def get_best_individuo(geracao):
    best = 0
    for crom in geracao:
        sub_matrix = 0
        valores_colunas = 0
        for i in range(3):
            for j in range(3):
                sub_matrix = sub_matrix + verificar_valores_sub_matriz(get_sub_matrix(i, j, crom))
                valores_colunas = valores_colunas + verificar_valores_coluna(get_valor_mesma_coluna(0, 0, crom))
        if get_fitness(sub_matrix + valores_colunas) > best:
            best = get_fitness(sub_matrix + valores_colunas)

    return best

def cross_over_aritmetico(geracao):
    lambdaA = 0.3
    lambdaB = 0.5
    new_generation = []
    for values in geracao:
        new_values = []
        for i in range(len(values) - 1):
            cromossomoA = roleta(geracao)
            cromossomoB = roleta(geracao)
            filhoA = cromossomoA*lambdaA + (1 - lambdaA) * cromossomoB
            filhoB = cromossomoB*lambdaB + (1 - lambdaB) * cromossomoA
            new_values.append(filhoA)
            new_values.append(filhoB)
        new_generation.append(new_values)
    return new_generation


def mutacao_DE(schema,lista):
   return dem.mutacao(schema,lista)



def gerarGrafico(fitness,valores):
    mt.title("Valores de Fitness da geração")
    mt.plot(fitness, valores)
    mt.xlabel("Melhor valor na geração")
    mt.ylabel("Numero da geração")
    mt.show()


def roleta(geracao):
    for ind in geracao:
        fitness_sum = sum([values for values in ind])
        probability_offset = 0
        prob = []
        i = 0
    for ind in geracao:
        for values in ind:
            prob.append(probability_offset + (calculo_fitness(ind) / fitness_sum))
            probability_offset = probability_offset + prob[i]
        i = i + 1
    r = rd.random()
    selected_ind = geracao[0]
    i = 0
    for ind in geracao:
        for values in ind:
            if prob[i] > r:
                break
            selected_ind = values
            i = i + 1

    return selected_ind


def calculo_fitness(crom):
    valor_fitness = 0
    sub_matrix = 0
    valores_colunas = 0
    for i in range(3):
        for j in range(3):
            sub_matrix = sub_matrix + verificar_valores_sub_matriz(get_sub_matrix(i, j, crom))
            valores_colunas = valores_colunas + verificar_valores_coluna(get_valor_mesma_coluna(0, 0, crom))
    valor_fitness = get_fitness(sub_matrix + valores_colunas)
    return valor_fitness






































