# Sistema de Gerenciamento de Estoque

[![License](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE)

## Descrição

Este projeto é um sistema de gerenciamento de estoque para uma loja de varejo. Ele permite adicionar, atualizar, vender produtos e verificar o estoque. O projeto utiliza `PyQt5` para a interface gráfica e `SQLite3` para o banco de dados.

## Funcionalidades

- Adicionar novos produtos ao estoque
- Atualizar informações de produtos existentes
- Vender produtos, ajustando a quantidade no estoque
- Verificar o estoque disponível na loja

## Tecnologias Utilizadas

- Python
- PyQt5
- SQLite3

## Estrutura do projeto

sistema-gerenciamento-estoque/
├── app.py
├── models/
│   ├── loja.py
│   └── produto.py
└── databases/
    └── loja.db
