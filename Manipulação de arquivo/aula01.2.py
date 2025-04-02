arquivo = open('Lh.txt', 'w')
arquivo.write('Gb' '\nluis')
arquivo.close()


arquivo = open('Lh.txt')
print(arquivo.readline())
arquivo.close()

caminho_arquivo = 'Lh.txt'

arquivo = open(caminho_arquivo, 'r')

linha1 = arquivo.readline()
print(f'Linha 1: {linha1}')
linha2 = arquivo.readline()
print(f'Linha 2: {linha2}')

arquivo.close()