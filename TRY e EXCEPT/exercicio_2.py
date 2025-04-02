try:
    f = open('Nomes')
    s = f.readline()
    i = int(s.strip())
except FileNotFoundError:
    print("Arquivo 'teste.txt' não encontrado.")
except IOError:
    print("Erro na abertura do arquivo.")
except ValueError:
    print("Formato inválido encontrado no arquivo.")
except Exception as e:
    print(f"Erro inesperado: {e}")
    raise