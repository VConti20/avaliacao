from funções import *

while True:
    menu(["Cadastrar livro","Listar livros","Pesquisar livro","Remover livro","Calcular idade da publicação","Relatório","Matriz de consulta","Sair"])
    opcao=input("Selecione uma das opções: ")

    match opcao:
        case "1":
            cadastrar_livro()
        case "2":
            listar_livros()
        case "3":
            pesquisar_livro()
        case "4":
            remover_livro()
        case "5":
            calcular()
        case "6":
            relatorio()
        case "7":
            mostrar_matriz()
        case "8":
            break
        case _:
            print("Opção invalida!")