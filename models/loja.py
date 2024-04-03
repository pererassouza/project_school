from produto import Produto


class Loja:
    def __init__(self, nome: str):
        self.nome = nome
        self.produtos = {}

    def adicionar_produto(self, produto: Produto, quantidade_inicial: int)\
            -> None:
        self.produtos[produto.nome] = produto
        produto.atualizar_quantidade(quantidade_inicial)

    def vender_produto(self, nome_produto: str, quantidade: int) -> None:
        produto = self.produtos.get(nome_produto)
        if produto and produto.quantidade >= quantidade:
            produto.atualizar_quantidade(-quantidade)
            print(f"{quantidade} unidade de {nome_produto} foram vendidas.")
        else:
            print("Produto não disponível em estoque.")

    def verificar_estoque(self) -> None:
        print("Estoque disponivel da loja:")
        for produto in self.produtos.values():
            print(f"{produto.nome}: {produto.quantidade} unidades")


if __name__ == "__main__":
    # Criando alguns produtos
    produto1 = Produto("Camiseta", 29.99, 50)
    produto2 = Produto("Calça Jeans", 59.99, 30)
    produto3 = Produto("Tênis", 79.99, 20)

    # Criando a loja
    loja = Loja("Minha Loja")

    # Adicionando produtos à loja
    loja.adicionar_produto(produto1, 50)
    loja.adicionar_produto(produto2, 30)
    loja.adicionar_produto(produto3, 20)

    # Verificando estoque inicial
    loja.verificar_estoque()

    # Vendendo alguns produtos
    loja.vender_produto("Camiseta", 10)
    loja.vender_produto("Tênis", 5)

    # Verificando estoque após vendas
    loja.verificar_estoque()
