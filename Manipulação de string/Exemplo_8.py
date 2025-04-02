import re

texto = "Meu e-mail é exemplo@email.com, entre em contato"
padrao = r'\b\w+@\w+\.\w+\b' # Padrão para encontrar endereçoes de e-mail

novo_texto = re.sub(padrao, "[email oculto]", texto)
print(novo_texto)