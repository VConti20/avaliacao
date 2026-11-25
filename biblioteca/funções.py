livros=[]

consultas= [
    [3, 2, 4],
    [1, 5, 2],
    [4, 3, 1]
]

def menu(lista):
    cont=1
    for l in lista:
        print(f"{cont} - {l}")
        cont +=1

def linha(msg):
    print(f"{'--' * 30}")
    print(msg)
    print(f"{'--' * 30}")

def cadastrar_livro():
    titulo=input("Digite o titulo: ")
    autor=input("Digite o autor: ")
    ano=input("Digite o ano da publicação: ")

    livro= {
        "titulo": titulo,
        "autor": autor,
        "ano": ano
    }

    livros.append(livro)
    linha("Livro cadastrado com sucesso!")

def listar_livros():
    if len(livros) == 0:
        print("Nenum livro cadastrado")
    else:
        for livro in livros:
            print(f"{'--' * 30}")
            print("Titulo:",livro["titulo"])
            print("Autor:",livro["autor"])
            print("Ano:",livro["ano"])
        print(f"{'--' * 30}")

def pesquisar_livro():
    pesquisa=input("Digite o titulo do livro: ")
    encontrado=False

    for livro in livros:
        if livro["titulo"].lower() == pesquisa.lower():
            print("Livro encontrado")
            print("Titulo:", livro['titulo'])
            print("Autor:", livro['autor'])
            print("Ano:", livro['ano'])
            encontrado=True
    if encontrado == False:
        print("Livro não encontrado")
def calcular():
    pesquisa=input("Digite o titulo do livro: ")

    for livro in livros:
        if livro["titulo"].lower() == pesquisa.lower():
            ano=int(livro["ano"])
            idade = 2026 - ano
            if idade >= 0 and idade <= 5:
                print(f"Livro recente! Publicado há {idade} anos.")
            elif idade > 5:
                print(f"Livro antigo! Publicado há {idade} anos")
            elif ano <= 0 or ano > 2026:
                print("Ano de publicação invalido.")
            return
    print("Livro não encontrado")


def relatorio():
    if len(livros) == 0:
        print("Nenhum livro cadastrado")
        return

    quantidade=len(livros)
    anos=[]

    for livro in livros:
        anos.append(int(livro["ano"]))

    menor_ano=min(anos)
    maior_ano=max(anos)

    linha("------ RELATÓRIO ------")
    print(f"Quantidade de livros: {quantidade}")
    for livro in livros:
        if int(livro["ano"]) == menor_ano:
            print(f"Livro mais antigo: {livro['titulo']}")

        if int(livro["ano"]) == maior_ano:
            print(f"Livro mais recente: {livro['titulo']}")



def remover_livro():
    pesquisa=input("Digite o titulo do livro que deseja remover: ")
    for livro in livros:
        if livro["titulo"].lower() == pesquisa.lower():
            livros.remove(livro)
            print(f"O {livro['titulo']} foi removido com sucesso")
            return
    print("Livro não encontrado")

def mostrar_matriz():
    dias = ["Segunda","Terça", "Quarta"]
    linha("Consulta por dia")

    for i in range(len(consultas)):
        total=0

        for j in range(len(consultas[i])):
            print(consultas[i][j], end= " ")
            total+=consultas[i][j]
    print(f"Total: {total} - {dias[i][j]}")





