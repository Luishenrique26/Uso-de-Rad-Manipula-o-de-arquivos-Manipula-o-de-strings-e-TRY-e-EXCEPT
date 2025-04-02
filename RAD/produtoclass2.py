from dataclasses import dataclass 

@dataclass 
class Produto:
    nome: str
    preço: float
    quantidade: int

    def exibir_informacoes(self) -> str:
        return (
            f"Produto: {self.nome} Preço: {self.preço}, quantidade: {self.quantidade}"
        )

produto1 = Produto("caneta", 1.50, 100)

print(produto1.exibir_informacoes())
