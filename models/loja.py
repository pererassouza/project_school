from produto import Produto
import sqlite3


class Loja:
    def __init__(self, nome):
        self.nome = nome
        self.conn = sqlite3.connect('databases/loja.db')
        self.criar_tabela()

    def criar_tabela(self):
        cursor = self.conn.cursor()
        cursor.execute('''CREATE TABLE IF NOT EXISTS produtos
                          (id INTEGER PRIMARY KEY, nome TEXT, preco REAL, \
                       quantidade INTEGER)''')
        self.conn.commit()

    def adicionar_produto(self, produto):
        cursor = self.conn.cursor()
        cursor.execute("INSERT INTO produtos (nome, preco, quantidade) VALUES \
                       (?, ?, ?)",
                       (produto.nome, produto.preco, produto.quantidade))
        self.conn.commit()

    def atualizar_produto(self, nome_produto, novo_preco, nova_quantidade):
        cursor = self.conn.cursor()
        cursor.execute("UPDATE produtos SET preco=?,\
                        quantidade=? WHERE nome=?",
                       (novo_preco, nova_quantidade, nome_produto))
        self.conn.commit()
        print(f"{nome_produto} atualizado com sucesso.")

    def vender_produto(self, nome_produto, quantidade):
        cursor = self.conn.cursor()
        cursor.execute("SELECT * FROM produtos WHERE nome=?", (nome_produto,))
        produto = cursor.fetchone()
        if produto and produto[3] >= quantidade:
            novo_estoque = produto[3] - quantidade
            cursor.execute(
                "UPDATE produtos SET quantidade=? WHERE nome=?",
                (novo_estoque, nome_produto))
            self.conn.commit()
            print(f"{quantidade} unidades de {nome_produto} vendidas.")
        else:
            print("Produto não disponível em estoque.")

    def verificar_estoque(self):
        cursor = self.conn.cursor()
        cursor.execute("SELECT * FROM produtos")
        produtos = cursor.fetchall()
        print("Estoque disponível na loja:")
        for produto in produtos:
            print(f"{produto[1]}: {produto[3]} unidades")


# Exemplo de uso
if __name__ == "__main__":
    # Criando a loja
    loja = Loja("Minha Loja")

    # Adicionando produtos à loja
    loja.adicionar_produto(Produto(None, "Camiseta", 29.99, 50))
    loja.adicionar_produto(Produto(None, "Calça Jeans", 59.99, 30))
    loja.adicionar_produto(Produto(None, "Tênis", 79.99, 20))

    # Verificando estoque inicial
    loja.verificar_estoque()

    # Atualizando preço e estoque de um produto
    loja.atualizar_produto("Camiseta", 80.20, 32)

    # Verificando estoque após atualização
    loja.verificar_estoque()

    # Vendendo alguns produtos
    loja.vender_produto("Camiseta", 10)
    loja.vender_produto("Tênis", 5)

    # Verificando estoque após vendas
    loja.verificar_estoque()
