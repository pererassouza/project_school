from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QLabel, \
    QLineEdit, QVBoxLayout, QWidget, QDesktopWidget
import sys

from models.loja import Loja
from models.produto import Produto


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Sistema de Gerenciamento de Estoque")

        # Centralizar a janela na tela
        self.center_window()

        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)

        self.layout = QVBoxLayout()  # type: ignore
        self.central_widget.setLayout(self.layout)

        self.setWindowTitle("Sistema de Gerenciamento de Estoque")
        self.setGeometry(100, 100, 400, 300)

        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)

        self.layout = QVBoxLayout()  # type: ignore
        self.central_widget.setLayout(self.layout)

        self.label_nome_produto = QLabel("Nome do Produto:")
        self.layout.addWidget(self.label_nome_produto)

        self.input_nome_produto = QLineEdit()
        self.layout.addWidget(self.input_nome_produto)

        self.label_preco = QLabel("Preço:")
        self.layout.addWidget(self.label_preco)

        self.input_preco = QLineEdit()
        self.layout.addWidget(self.input_preco)

        self.label_quantidade = QLabel("Quantidade:")
        self.layout.addWidget(self.label_quantidade)

        self.input_quantidade = QLineEdit()
        self.layout.addWidget(self.input_quantidade)

        self.btn_adicionar = QPushButton("Adicionar Produto")
        self.btn_adicionar.clicked.connect(self.adicionar_produto)
        self.layout.addWidget(self.btn_adicionar)

        self.btn_atualizar = QPushButton("Atualizar Produto")
        self.btn_atualizar.clicked.connect(self.atualizar_produto)
        self.layout.addWidget(self.btn_atualizar)

        self.btn_vender = QPushButton("Vender Produto")
        self.btn_vender.clicked.connect(self.vender_produto)
        self.layout.addWidget(self.btn_vender)

        self.btn_verificar_estoque = QPushButton("Verificar Estoque")
        self.btn_verificar_estoque.clicked.connect(self.verificar_estoque)
        self.layout.addWidget(self.btn_verificar_estoque)

        self.label_status = QLabel()
        self.layout.addWidget(self.label_status)

        self.loja = Loja("Minha Loja")

    def center_window(self):
        # Obtém a geometria da tela
        screen_geometry = QDesktopWidget().screenGeometry()

        # Obtém a geometria da janela
        window_geometry = self.geometry()

        # Centraliza a janela na tela
        x = (screen_geometry.width() - window_geometry.width()) // 2
        y = (screen_geometry.height() - window_geometry.height()) // 2
        self.setGeometry(x, y, window_geometry.width(),
                         window_geometry.height())

    def adicionar_produto(self):
        nome = self.input_nome_produto.text()
        preco_texto = self.input_preco.text()
        quantidade_texto = self.input_quantidade.text()

        if preco_texto.strip() and quantidade_texto.strip():
            preco = float(preco_texto)
            quantidade = int(quantidade_texto)
            produto = Produto(None, nome, preco, quantidade)
            self.loja.adicionar_produto(produto)
            self.label_status.setText(f"{nome} adicionado com sucesso.")
        else:
            self.label_status.setText(
                "Por favor, insira um preço e uma quantidade válidos.")

    def atualizar_produto(self):
        nome = self.input_nome_produto.text()
        preco_texto = self.input_preco.text()
        quantidade_texto = self.input_quantidade.text()

        if preco_texto.strip() and quantidade_texto.strip():
            preco = float(preco_texto)
            quantidade = int(quantidade_texto)
            self.loja.atualizar_produto(nome, preco, quantidade)
            self.label_status.setText(f"{nome} atualizado com sucesso.")
        else:
            self.label_status.setText(
                "Por favor, insira um preço e uma quantidade válidos.")

    def vender_produto(self):
        nome = self.input_nome_produto.text()
        quantidade_texto = self.input_quantidade.text()

        if quantidade_texto.strip():  # Verifica se a string não está vazia
            quantidade = int(quantidade_texto)
            self.loja.vender_produto(nome, quantidade)
            self.label_status.setText(
                f"{quantidade} unidades de {nome} vendidas.")
        else:
            self.label_status.setText(
                "Por favor, insira uma quantidade válida.")

    def verificar_estoque(self):
        self.label_status.setText("")
        self.loja.verificar_estoque()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
