class Estudante:
    def __init__(self, nome, idade, nota, identificador):
        self.nome = nome
        self.idade = idade
        self.nota = nota
        self.id = identificador

    def alterar_nota(self, nova_nota):
        self.nota = nova_nota

    def informacoes(self):
        return f"Nome: {self.nome}, Idade: {self.idade}, Nota: {self.nota}, ID: {self.id}"

class Turma:
    def __init__(self):
        self.estudantes = []

    def adicionar_estudante(self, estudante):
        self.estudantes.append(estudante)

    def remover_estudante(self, identificador):
        for estudante in self.estudantes:
            if estudante.id == identificador:
                self.estudantes.remove(estudante)
                print(f"Estudante com ID {identificador} removido.")
                return
        print(f"Estudante com ID {identificador} não encontrado.")

    def media_da_turma(self):
        if not self.estudantes:
            return 0 
        total_notas = sum(estudante.nota for estudante in self.estudantes)
        return total_notas / len(self.estudantes)

    def melhor_estudante(self):
        if not self.estudantes:
            return None
        return max(self.estudantes, key=lambda estudante: estudante.nota)

estudante1 = Estudante("Claudio", 8, 9, 4)
estudante2 = Estudante("Rafael", 7, 8, 6)
estudante3 = Estudante("Robson", 9, 5, 7)

turma = Turma()
turma.adicionar_estudante(estudante1)
turma.adicionar_estudante(estudante2)
turma.adicionar_estudante(estudante3)

print("Listando todos os estudantes na turma:")
for estudante in turma.estudantes:
    print(estudante.informacoes())

print("\nRemovendo o estudante com ID 2:")
turma.remover_estudante(2)

print("\nListando todos os estudantes após a remoção:")
for estudante in turma.estudantes:
    print(estudante.informacoes())

print("\nMédia da turma:", turma.media_da_turma())
melhor = turma.melhor_estudante()
if melhor:
    print("Melhor estudante:", melhor.nome)
