class Jogo:
    def __init__(self, nome, categoria, taxa_entrada, identificador):
        self.nome = nome
        self.categoria = categoria
        self.taxa_entrada = taxa_entrada
        self.id = identificador

    def __str__(self):
        return f"Nome: {self.nome}, Categoria: {self.categoria}, Taxa de Entrada: {self.taxa_entrada}, ID: {self.id}"

class Plataforma:
    def __init__(self):
        self.lista_de_jogos = []

    def adicionar_jogo(self, jogo):
        self.lista_de_jogos.append(jogo)

    def remover_jogo(self, identificador):
        for jogo in self.lista_de_jogos:
            if jogo.id == identificador:
                self.lista_de_jogos.remove(jogo)
                print(f"Jogo com ID {identificador} removido.")
                return
        print(f"Jogo com ID {identificador} não encontrado.")

    def listar_jogos(self):
        for jogo in self.lista_de_jogos:
            print(jogo)

    def __str__(self):
        total_de_jogos = len(self.lista_de_jogos)
        return f"Total de Jogos na Plataforma: {total_de_jogos}"

jogo1 = Jogo("Pôquer", "Cartas", 10.0, 1)
jogo2 = Jogo("Caça-Níqueis", "Máquinas", 5.0, 2)
jogo3 = Jogo("Roleta", "Mesa", 15.0, 3)

plataforma = Plataforma()
plataforma.adicionar_jogo(jogo1)
plataforma.adicionar_jogo(jogo2)
plataforma.adicionar_jogo(jogo3)

print("Listando todos os jogos na plataforma:")
plataforma.listar_jogos()

print("\nRemovendo o jogo com ID 2:")
plataforma.remover_jogo(2)

print("\nListando todos os jogos após a remoção:")
plataforma.listar_jogos()

print(plataforma)
