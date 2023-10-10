class Livro:
    def __init__(self, titulo, autor):
        self.titulo = titulo
        self.autor = autor
        self.status = "disponível"

class Membro:
    def __init__(self, nome):
        self.nome = nome
        self.livros_emprestados = []

class Biblioteca:
    def __init__(self):
        self.livros = {}
        self.membros = {}

    def adicionar_livro(self, livro):
        self.livros[livro.titulo] = livro

    def registrar_membro(self, membro):
        self.membros[membro.nome] = membro

    def emprestar_livro(self, titulo_livro, nome_membro):
        livro = self.livros.get(titulo_livro)
        membro = self.membros.get(nome_membro)

        if livro and membro:
            if livro.status == "disponível":
                livro.status = "emprestado"
                membro.livros_emprestados.append(livro)
                return f'O livro "{titulo_livro}" foi emprestado para {nome_membro}.'
            else:
                return f'O livro "{titulo_livro}" já foi emprestado para outro membro.'
        else:
            return "Livro ou membro não encontrado."

    def retornar_livro(self, titulo_livro, nome_membro):
        livro = self.livros.get(titulo_livro)
        membro = self.membros.get(nome_membro)

        if livro and membro and livro in membro.livros_emprestados:
            livro.status = "disponível"
            membro.livros_emprestados.remove(livro)
            return f'O livro "{titulo_livro}" foi devolvido por {nome_membro}.'
        else:
            return "Livro não encontrado ou não emprestado por este membro."

    def buscar_membro(self, busca):
        membros_encontrados = [nome for nome in self.membros.keys() if busca in nome]
        return membros_encontrados

# Exemplo de uso do seu código
livro1 = Livro('Estrela', 'Jorge')
livro2 = Livro('Céu', 'Claudio')
livro3 = Livro('Terra', 'Fernando')

membro1 = Membro('Daniel')
membro2 = Membro('Denis')
membro3 = Membro('Daniboy')

biblioteca = Biblioteca()
biblioteca.adicionar_livro(livro1)
biblioteca.adicionar_livro(livro2)
biblioteca.adicionar_livro(livro3)
biblioteca.registrar_membro(membro1)
biblioteca.registrar_membro(membro2)
biblioteca.registrar_membro(membro3)



