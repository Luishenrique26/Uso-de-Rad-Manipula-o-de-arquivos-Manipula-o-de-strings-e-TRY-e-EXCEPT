caminho_arquivo = 'Lh.txt'

arquivo = open("Lh.txt", 'w')
arquivo.write("Neymar")
arquivo.writelines(["\nDaniel alves", "\nRobinho", "\nMessi"])
arquivo.close()

arquivo = open (caminho_arquivo, 'r')
linhas = arquivo.readlines()
for i, linha in enumerate(linhas, start=1):
    print(f'linha {i}: {linha}')