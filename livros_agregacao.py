# Atributos: Autor, livro, quantidade de peças e se está disponivel ou não para venda
print('--- Biblioteca ---')

class Livros:
    def __init__(self, nome, autor, quantidade):
        self.nome = nome
        self.autor = autor
        self.quantidade = quantidade

class Biblioteca:
    def __init__(self):
        self.livros = []

    def adicionar_livro(self, livro):
        self.livros.append(livro)

    def apresentar_catalogo(self):
        for livro in self.livros:
            print(f'- Nome do livro: {livro.nome}')
            print(f'- Autor: {livro.autor}')
            print(f'- Disponível:{f" Sim\n- Quantidade em estoque: {livro.quantidade}" if livro.quantidade >= 1 else " Não"}')
    
#Cadastrando os livros
livro_1 = Livros('Entendendo Algoritmos', 'Aditya Y. Bhargava', 0)

#Adicionar a Biblioteca
biblioteca = Biblioteca()
biblioteca.adicionar_livro(livro_1)  
biblioteca.apresentar_catalogo()