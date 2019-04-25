import methods as mt
import operator
import Cromossomo as cr
import normalize_methods as nm

lista = []
ind = cr.obj("",0)
cond = int(input("1 - Avaliação simples\n2 - Avaliação com normalização\n"))
if cond == 1:
    lista_x_grafico = []
    lista_y_grafico = []
    pop = int(input("Digite o numero da população "))
    iter = int(input("Digite o numero de iterações "))
    lista = mt.create_generation(pop)
    for i in range(iter):
        lista_y_grafico.append(i)
        if i == 0:
            mut = mt.mutacao(lista, 4)
            cross = mt.cross_over(mut)
            best = mt.get_melhor_cromossomo(cross)
            lista_x_grafico.append(best.getFitness())
        elif i > 0:
            pmut = mt.mutacao(cross,7)
            listcross = mt.cross_over(pmut)
            best = mt.get_melhor_cromossomo(listcross)
            lista_x_grafico.append(best.getFitness())
    mt.gerarGrafico(lista_x_grafico,lista_y_grafico)


elif cond == 2:
    lista_x_grafico = []
    lista_y_grafico = []
    pop = int(input("Digite o numero da população "))
    iter = int(input("Digite o numero de iterações "))
    lista = mt.create_generation(pop)
    for i in range(iter):
        lista_y_grafico.append(i)
        if i == 0:
            mut = nm.mutacaoNormalizada(lista, 8)
            cross = nm.crossOverNormalizado(mut)
            best = nm.getMelhorCromossomo(cross)
            lista_x_grafico.append(best.getFitness())
        elif i > 0:
            pmut = nm.mutacaoNormalizada(cross,4)
            listcross = nm.crossOverNormalizado(pmut)
            best = nm.getMelhorCromossomo(listcross)
            lista_x_grafico.append(best.getFitness())
    mt.gerarGrafico(lista_x_grafico,lista_y_grafico)





