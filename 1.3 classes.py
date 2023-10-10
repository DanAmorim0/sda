class Animal:
    def __init__(self, nome, especie, idade, dieta, habitat):
        self.nome = nome
        self.especie = especie
        self.idade = idade
        self.dieta = dieta
        self.habitat = habitat

    def descricao(self):
        return f"{self.nome} é um(a) {self.especie} de {self.idade} anos que é {self.dieta}. Habitat: {self.habitat}"

class Zoologico:
    def __init__(self):
        self.animais = []

    def adicionar_animal(self, animal):
        self.animais.append(animal)
        print(f"{animal.nome} foi adicionado ao zoológico.")

    def remover_animal(self, nome):
        for animal in self.animais:
            if animal.nome == nome:
                self.animais.remove(animal)
                print(f"{animal.nome} foi removido do zoológico.")
                return
        print(f"Animal com nome {nome} não encontrado no zoológico.")

    def listar_animais(self):
        if not self.animais:
            print("O zoológico está vazio.")
        else:
            for animal in self.animais:
                print(animal.descricao())

    def buscar_por_especie(self, especie):
        animais_da_especie = [animal for animal in self.animais if animal.especie == especie]
        if animais_da_especie:
            for animal in animais_da_especie:
                print(animal.descricao())
        else:
            print(f"Nenhum animal da espécie {especie} encontrado no zoológico.")

    def listar_animais_em_habitat(self, habitat):
        animais_no_habitat = [animal for animal in self.animais if animal.habitat == habitat]
        if animais_no_habitat:
            for animal in animais_no_habitat:
                print(animal.descricao())
        else:
            print(f"Nenhum animal no habitat {habitat} encontrado no zoológico.")

zoo = Zoologico()

animal1 = Animal("Leo", "Leão", 5, "Carnívoro", "Savana")
animal2 = Animal("Polly", "Papagaio", 3, "Onívoro", "Floresta Tropical")
animal3 = Animal("Rocky", "Rinoceronte", 10, "Herbívoro", "Savana")

zoo.adicionar_animal(animal1)
zoo.adicionar_animal(animal2)
zoo.adicionar_animal(animal3)

print("\nListando todos os animais no zoológico:")
zoo.listar_animais()

print("\nBuscando por espécie 'Leão':")
zoo.buscar_por_especie("Leão")

print("\nListando animais no habitat 'Savana':")
zoo.listar_animais_em_habitat("Savana")

zoo.remover_animal("Polly")

print("\nListando todos os animais após a remoção:")
zoo.listar_animais()
