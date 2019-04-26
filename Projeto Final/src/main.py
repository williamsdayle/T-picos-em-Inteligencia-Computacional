import methods as mt
dificuldade = int(input("1 - FÁCIL\n2 - MÉDIO\n3 - DIFÍCIL\n"))
if dificuldade == 1:
    grafic_x_values = []
    grafic_y_values = []
    pop = int(input("Tamanho da população a resolver o problema\n"))
    iter = int(input("Numero de iterações\n"))
    schema = int(input("1 - Schema DE/RAND/1/BIN\n2 - Schema DE/RAND/2\n3 - Schema DE/BEST/2\n"))
    geracao = mt.create_generation(dificuldade, pop)
    cross = mt.cross_over_aritmetico(geracao)
    if schema == 1:
        grafic_y_values.append(1)
        grafic_x_values.append(mt.get_best_individuo(cross))
        mut = mt.mutacao_DE(1,cross)
        for i in range(iter):
            cross = mt.cross_over_aritmetico(mut)
            mut = mt.mutacao_DE(1,cross)
            grafic_y_values.append(i+1)
            grafic_x_values.append(mt.get_best_individuo(mut))
    mt.gerarGrafico(grafico_x_values,grafico_y_values)

    if schema == 2:
        grafic_y_values.append(1)
        grafic_x_values.append(mt.get_best_individuo(cross))
        mut = mt.mutacao_DE(2,cross)
        for i in range(iter):
            cross = mt.cross_over_aritmetico(mut)
            mut = mt.mutacao_DE(2,cross)
            grafic_y_values.append(i+1)
            grafic_x_values.append(mt.get_best_individuo(mut))
    mt.gerarGrafico(grafico_x_values,grafico_y_values)

    if schema == 3:
        grafic_y_values.append(1)
        grafic_x_values.append(mt.get_best_individuo(cross))
        mut = mt.mutacao_DE(3,cross)
        for i in range(iter):
            cross = mt.cross_over_aritmetico(mut)
            mut = mt.mutacao_DE(3,cross)
            grafic_y_values.append(i+1)
            grafic_x_values.append(mt.get_best_individuo(mut))
    mt.gerarGrafico(grafico_x_values,grafico_y_values)






elif dificuldade == 2:
    grafic_x_values = []
    grafic_y_values = []
    pop = int(input("Tamanho da população a resolver o problema\n"))
    iter = int(input("Numero de iterações\n"))
    schema = int(input("1 - Schema DE/RAND/1/BIN\n2 - Schema DE/RAND/2\n3 - Schema DE/BEST/2\n"))
    geracao = mt.create_generation(dificuldade, pop)
    cross = mt.cross_over_aritmetico(geracao)
    if schema == 1:
        grafic_y_values.append(1)
        grafic_x_values.append(mt.get_best_individuo(cross))
        mut = mt.mutacao_DE(1,cross)
        for i in range(iter):
            cross = mt.cross_over_aritmetico(mut)
            mut = mt.mutacao_DE(1,cross)
            grafic_y_values.append(i+1)
            grafic_x_values.append(mt.get_best_individuo(mut))
    mt.gerarGrafico(grafico_x_values,grafico_y_values)

    if schema == 2:
        grafic_y_values.append(1)
        grafic_x_values.append(mt.get_best_individuo(cross))
        mut = mt.mutacao_DE(2,cross)
        for i in range(iter):
            cross = mt.cross_over_aritmetico(mut)
            mut = mt.mutacao_DE(2,cross)
            grafic_y_values.append(i+1)
            grafic_x_values.append(mt.get_best_individuo(mut))
    mt.gerarGrafico(grafico_x_values,grafico_y_values)

    if schema == 3:
        grafic_y_values.append(1)
        grafic_x_values.append(mt.get_best_individuo(cross))
        mut = mt.mutacao_DE(3,cross)
        for i in range(iter):
            cross = mt.cross_over_aritmetico(mut)
            mut = mt.mutacao_DE(3,cross)
            grafic_y_values.append(i+1)
            grafic_x_values.append(mt.get_best_individuo(mut))
    mt.gerarGrafico(grafico_x_values,grafico_y_values)





elif dificuldade == 3:
    grafic_x_values = []
    grafic_y_values = []
    pop = int(input("Tamanho da população a resolver o problema\n"))
    iter = int(input("Numero de iterações\n"))
    schema = int(input("1 - Schema DE/RAND/1/BIN\n2 - Schema DE/RAND/2\n3 - Schema DE/BEST/2\n"))
    geracao = mt.create_generation(dificuldade, pop)
    cross = mt.cross_over_aritmetico(geracao)
    if schema == 1:
        grafic_y_values.append(1)
        grafic_x_values.append(mt.get_best_individuo(cross))
        mut = mt.mutacao_DE(1,cross)
        for i in range(iter):
            cross = mt.cross_over_aritmetico(mut)
            mut = mt.mutacao_DE(1,cross)
            grafic_y_values.append(i+1)
            grafic_x_values.append(mt.get_best_individuo(mut))
    mt.gerarGrafico(grafico_x_values,grafico_y_values)

    if schema == 2:
        grafic_y_values.append(1)
        grafic_x_values.append(mt.get_best_individuo(cross))
        mut = mt.mutacao_DE(2,cross)
        for i in range(iter):
            cross = mt.cross_over_aritmetico(mut)
            mut = mt.mutacao_DE(2,cross)
            grafic_y_values.append(i+1)
            grafic_x_values.append(mt.get_best_individuo(mut))
    mt.gerarGrafico(grafico_x_values,grafico_y_values)

    if schema == 3:
        grafic_y_values.append(1)
        grafic_x_values.append(mt.get_best_individuo(cross))
        mut = mt.mutacao_DE(3,cross)
        for i in range(iter):
            cross = mt.cross_over_aritmetico(mut)
            mut = mt.mutacao_DE(3,cross)
            grafic_y_values.append(i+1)
            grafic_x_values.append(mt.get_best_individuo(mut))
    mt.gerarGrafico(grafico_x_values,grafico_y_values)




