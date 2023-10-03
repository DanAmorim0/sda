"""
Crie uma classe chamada Carro que represente diferentes carros em uma revendedora de automóveis. A classe deve ter os seguintes atributos e métodos:
Atributos:
marca: Representa a marca do carro (por exemplo, Toyota, Ford, BMW, etc.).
modelo: Representa o modelo específico do carro.
ano: Representa o ano de fabricação do carro.
preco: Representa o preço do carro.
vendido: Um valor booleano que indica se o carro foi vendido ou não. Por padrão, todos os carros são considerados não vendidos.
Métodos:
exibir_informacoes(): Mostra todas as informações sobre o carro.
vender(): Marca o carro como vendido.
ajustar_preco(novo_preco): Ajusta o preço do carro para o valor especificado.

Instancie pelo menos 5 objetos.
"""

class Carro:

    modelos = {
        "Corolla": 18000,
        "Mustang": 100000,
        "Uno Mille": 1000,
        "Gol G3": 2000,
        "Marea Turbo": 1
    }
    def __init__(self, marca, modelo, ano, preco, vendido):

        self.marca = marca
        self.modelo = modelo
        self.ano = ano
        self.preco = max(preco, self.modelos.get(modelo, 0))
        self.vendido = False
        
    def exibir_informacoes(self):
        if self.vendido == False:
            return f'Marca:{self.marca}\nModelo:{self.modelo}\nAno:{self.ano}\nPreço:{self.preco}R$\nVendido:Em estoque'
        else:
            return f'Marca:{self.marca}\nModelo:{self.modelo}\nAno:{self.ano}\nPreço:{self.preco}R$\nVendido:Sem estoque'
    
    def vender(self):
        self.vendido = True
        print(f'Carro {self.marca} vendido com sucesso!!')

    def ajustar_preco(self, novo_preco):
        self.preco = novo_preco

    def tabela(self):
        if self.ajustar_preco <= 25000:
            print('Está abaixo da tabela, não pode ser vendido tão barato')
        else: 
            print('pode ser vendido')        
        

carro1 = Carro('toyota', 'Quadrado', 2001, 81888, False)
carro2 = Carro('Ford', 'Redondo', 2013, 98821, False)
carro3 = Carro('BMW', 'Esportivo', 2023, 200, False)

carro1.vender = True
carro1.ajustar_preco(20000)


print(carro1.exibir_informacoes())
print(carro1.tabela())



