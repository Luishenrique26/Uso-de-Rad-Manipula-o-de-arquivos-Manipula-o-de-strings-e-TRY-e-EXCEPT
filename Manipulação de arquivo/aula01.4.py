caminho_arquivo = 'Lh.txt'

with open(caminho_arquivo, 'w') as arquivo:
    arquivo.write('Esta e a primeira linha.\n')
    arquivo.write('Esta e a segunda linha.\n')

    linhas = ['Esta e a primeira linha em um lista.\n', 'Esta e a segunda linha em uma lista. \n']
    arquivo.writelines(linhas)
    