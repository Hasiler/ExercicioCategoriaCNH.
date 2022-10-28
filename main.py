"Exercicio Categorias de Habilitação"

peso = float(input('Qual peso do veiculo?'))
qtdrodas = int(input('Qual a quantidade de rodas do veiculo?'))
capacidade = int(input('Quantas pessoas o veiculo pode carregar'))

if qtdrodas <= 3:
    print('Categoria A da CNH')
elif peso <= 3500.0 and qtdrodas == 4 and capacidade == 8:
    print('Categoria B da CNH')
elif 3500.0 < peso <= 6000.0:
    print('Categoria C da CNH')
elif qtdrodas >= 4 and capacidade >= 8 or peso > 6000.0:
    print('Categoria D da CNH')
else:
    print('Dados inseridos inválidos, comece novamente!')