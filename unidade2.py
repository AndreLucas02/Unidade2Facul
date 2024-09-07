import matplotlib.pyplot as plt


class Livro:
    def __init__(self, titulo, autor, genero, quantidade):
        self.titulo = titulo
        self.autor = autor
        self.genero = genero
        self.quantidade = quantidade

biblioteca = []

def cadastrar_livro(titulo, autor, genero, quantidade):
    novo_livro = Livro(titulo, autor, genero, quantidade)
    biblioteca.append(novo_livro)
    print(f"O livro '{titulo}' foi adicionado a biblioteca!")

def listar_livros():
    if not biblioteca:
        print("Não há livros cadastrados.")
    else:
        for i, livro in enumerate(biblioteca, start=1):
            print(f"\nLivro {i}:")
            print(f"Título: {livro.titulo}")
            print(f"Autor: {livro.autor}")
            print(f"Gênero: {livro.genero}")
            print(f"Quantidade: {livro.quantidade}\n")

def buscar_livro(titulo):
    for livro in biblioteca:
        if livro.titulo.lower() == titulo.lower():
            print(f"Livro encontrado:\nTítulo: {livro.titulo}\nAutor: {livro.autor}\nGênero: {livro.genero}\nQuantidade: {livro.quantidade}\n")
            return
    print("Livro não encontrado.")

def gerar_grafico():
    generos = []
    quantidades = []
    for livro in biblioteca:
        if livro.genero not in generos:
            generos.append(livro.genero)
            quantidades.append(livro.quantidade)
        else:
            indice = generos.index(livro.genero)
            quantidades[indice] += livro.quantidade

    plt.bar(generos, quantidades)
    plt.xlabel("Gênero")
    plt.ylabel("Quantidade de Livros")
    plt.title("Livros por Gênero")
    plt.show()

# Cadastrar alguns biblioteca
cadastrar_livro("O Pequeno Príncipe", "Antoine de Saint-Exupéry", "Ficção", 10)
cadastrar_livro("1984", "George Orwell", "Distopia", 5)
cadastrar_livro("O Hobbit", "J.R.R. Tolkien", "Fantasia", 8)
cadastrar_livro("Orgulho e Preconceito", "Jane Austen", "Romance", 12)

# Listar todos os livros
listar_livros()

# Buscar um livro
buscar_livro("1984")

# Gerar o gráfico
gerar_grafico()

