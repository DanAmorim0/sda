'''class MinhaClasse:
    nome = "Romes"

p1 = MinhaClasse()

print(p1.nome)'''

class Pessoa:
    def __init__(self, nome, idade, habilitacao):
        self.nome = nome
        self.idade = idade
        self.habilitacao = habilitacao

    def __str__(self):
        return f'Nome: {self.nome} e sua idade é: {self.idade}'
    
    def maioridade(self):
        if self.idade > 17:
            print(f'Você é maior de idade, tem {self.idade} anos nas costas.')
        else:
            print("Menor de idade")    
    
    def habilita(self):
        if self.habilitacao == True:
            print(f'{self.nome} é habilitado!')
        else:
            print(f' {self.nome} não possui habilitação')

usuario1 = Pessoa('joão', 18, True)
usuario2 = Pessoa('maria', 30, False)
usuario3 = Pessoa('Cleber', 4, False)

usuario1.maioridade()
usuario2.maioridade()
usuario3.maioridade()

usuario1.habilita()
usuario3.habilita()