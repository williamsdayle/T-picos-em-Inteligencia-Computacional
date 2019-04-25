import methodsDeJong as mt

value = int(input("1 - Resolver sem DE\n2 - Resolver com DE\n"))
if value == 1:
    gen_tam = int(input("1 - Tamanho da geração\n"))
    iter = int(input("2 - Numero de iterações\n"))
    geracao = mt.create_generation(gen_tam)
    mut = mt.mutacao_real(geracao)
    cross = mt.cross_over_aritmetico(mut)
    grafic_x_values = []
    grafic_y_values = []
    grafic_y_values.append(0)
    grafic_x_values.append(mt.get_best_crom(cross))
    for i in range(1,iter):
        mut = mt.mutacao_real(cross)
        cross = mt.cross_over_aritmetico(mut)
        grafic_y_values.append(i)
        grafic_x_values.append(mt.get_best_crom(cross))

    mt.gerarGrafico(grafic_x_values,grafic_y_values)
elif value == 2:
    gen_tam = int(input("1 - Tamanho da geração\n"))
    iter = int(input("2 - Numero de iterações\n"))
    schema = int(input("1 - Schema DE/RAND/1/BIN\n2 - Schema DE/RAND/2\n3 - Schema DE/BEST/2\n"))
    geracao = mt.create_generation(gen_tam)
    mut = mt.mutacao_DE(schema,geracao)
    cross = mt.cross_over_aritmetico(mut)
    grafic_x_values = []
    grafic_y_values = []
    grafic_y_values.append(0)
    grafic_x_values.append(mt.get_best_crom(cross))
    for i in range(1,iter):
        mut = mt.mutacao_DE(schema, cross)
        cross = mt.cross_over_aritmetico(mut)
        grafic_y_values.append(i)
        grafic_x_values.append(mt.get_best_crom(cross))
    mt.gerarGrafico(grafic_x_values,grafic_y_values)













