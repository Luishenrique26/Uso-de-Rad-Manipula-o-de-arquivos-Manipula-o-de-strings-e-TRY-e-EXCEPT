# Função para adicionar notas ao arquivo
def adicionar_nota():
    nome = input("Nome do aluno: ")
    notas = input("Digite as notas separadas por vírgula (ex: 8.5,7.0,9.0): ")
    
    with open("notas.txt1", "a") as arquivo:
        arquivo.write(f"{nome}: {notas}\n")
    
    print("Nota adicionada com sucesso!")

# Função para exibir todas as notas
def exibir_notas():
    with open("notas.txt", "r") as arquivo:
        print("\n--- Notas dos Alunos ---")
        for linha in arquivo:
            print(linha.strip())

# Função para calcular a média das notas de um aluno específico
def calcular_media():
    nome = input("Digite o nome do aluno para calcular a média: ")
    
    encontrado = False
    with open("notas.txt", "r") as arquivo:
        for linha in arquivo:
            aluno, notas_str = linha.strip().split(": ")
            if aluno.lower() == nome.lower():
                notas = list(map(float, notas_str.split(",")))
                media = sum(notas) / len(notas)
                print(f"Média de {aluno}: {media:.2f}")
                encontrado = True
                break

    if not encontrado:
        print("Aluno não encontrado.")

# Menu do programa
while True:
    print("\n--- Sistema de Notas ---")
    print("1. Adicionar Nota")
    print("2. Exibir Notas")
    print("3. Calcular Média")
    print("4. Sair")
    
    opcao = input("Escolha uma opção: ")
    
    if opcao == "1":
        adicionar_nota()
    elif opcao == "2":
        exibir_notas()
    elif opcao == "3":
        calcular_media()
    elif opcao == "4":
        print("Saindo do sistema...")
        break
    else:
        print("Opção inválida. Tente novamente.")
