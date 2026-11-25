Sistema de Gerenciamento de Biblioteca (CLI)
Aplicação simples em Python via linha de comando (CLI) para cadastrar, consultar, remover e gerar relatórios de livros, além de exibir uma matriz de consultas por dia.

Funcionalidades
Cadastrar livro: registra título, autor e ano de publicação.
Listar livros: exibe todos os livros cadastrados com seus respectivos dados.
Pesquisar livro: busca um livro pelo título (sem diferenciar maiúsculas e minúsculas).
Remover livro: exclui um livro da lista a partir do título informado.
Calcular idade da publicação: calcula quantos anos se passaram desde a publicação (tendo 2026 como referência) e classifica o livro como recente ou antigo.
Relatório: mostra a quantidade total de livros cadastrados, o livro mais antigo e o livro mais recente.
Matriz de consulta: percorre a matriz consultas e exibe os valores registrados.
Sair: encerra a execução do programa.
Estrutura do Projeto
.
├── main.py       # Loop principal e menu interativo (match/case)
├── funções.py    # Listas/matrizes e funções do sistema
└── README.md     # Documentação do projeto
