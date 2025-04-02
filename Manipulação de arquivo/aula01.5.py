linhas = [
    "Esta e a primeira linha.\n",
    "Esta e a segunda linha.\n",
    "Esta e a terceira linha.\n",
]

with open("Lh.txt", "w", encoding="utf-8") as arquivo:
    # escreve todas as linhas de uma vez no arquivo
    arquivo.writelines(linhas)

with open("Lh.txt", "r", encoding="utf-8") as arquivo:
    conteudo = arquivo.read()
    print("Conteúdo do arquivo:")
    print(conteudo)
