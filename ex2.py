class Categoria:
    def __init__(self, nome):
        self.nome = nome

class Avaliacao:
    def __init__(self, cliente, nota, comentario):
        self.cliente = cliente
        self.nota = nota
        self.comentario = comentario

    def __str__(self):
        return f"Avaliação de {self.cliente}: Nota {self.nota} - {self.comentario}"

class Produto:
    def __init__(self, nome, preco, estoque, categoria):
        self.__nome = nome
        self.__preco = preco
        self.__estoque = estoque
        self.__categoria = categoria
        self.__avaliacoes = []

    def vender(self, quantidade):
        if quantidade <= self.__estoque:
            self.__estoque -= quantidade

    def reabastecer(self, quantidade):
        self.__estoque += quantidade

    def adicionar_avaliacao(self, avaliacao):
        self.__avaliacoes.append(avaliacao)

    def get_estoque(self):
        return self.__estoque

    def __str__(self):
        avaliacoes_str = "\n".join(str(av) for av in self.__avaliacoes) or "Sem avaliações"
        return (
            f"Produto: {self.__nome}\n"
            f"Preço: R${self.__preco:.2f}\n"
            f"Estoque: {self.__estoque}\n"
            f"Categoria: {self.__categoria.nome}\n"
            f"Avaliações:\n{avaliacoes_str}"
        )

class Loja:
    def __init__(self):
        self.__produtos = []

    def adicionar_produto(self, produto):
        self.__produtos.append(produto)

    def visualizar_estoque(self):
        for produto in self.__produtos:
            print(f"{produto._Produto__nome}: {produto.get_estoque()} unidades")

# Programa principal
categoria1 = Categoria("Eletrônicos")
categoria2 = Categoria("Livros")

produto1 = Produto("Smartphone", 1500.00, 10, categoria1)
produto2 = Produto("Livro Python", 80.00, 5, categoria2)

loja = Loja()
loja.adicionar_produto(produto1)
loja.adicionar_produto(produto2)

produto1.vender(2)
produto2.reabastecer(3)

avaliacao1 = Avaliacao("João", 5, "Ótimo produto!")
produto1.adicionar_avaliacao(avaliacao1)

print("\nEstoque da loja:")
loja.visualizar_estoque()

print("\nDetalhes do produto:")
print(produto1)
