class Carro:
    def __init__(self, marca, modelo, ano):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano

carros = [
    Carro("toyota", "corolla", 2020),
    Carro("honda", "civic", 2018),
    Carro("Ford", "mustang", 2018),
]

for carro in carros:
    print(carro.marca)
    print(carro.modelo)
    print(carro.ano)
