class Restaurante:
    def __init__(self):
        self.itens_menu = {
            "hamburger": 5.50,
            "batata frita": 2.00,
            "refrigerante": 1.50,
            "pizza": 8.00,
            "salada": 3.50
        }
        self.pedidos = {}
        self.numero_pedido = 1

    def adicionar_pedido(self):
        pedido = {}
        while True:
            item = input("Digite o nome do item (ou 'sair' para encerrar o pedido): ").lower()
            if item == 'sair':
                break
            if item in self.itens_menu:
                quantidade = int(input(f"Quantidade de {item}: "))
                pedido[item] = quantidade
            else:
                print("Item não encontrado no menu. Tente novamente.")

        if pedido:
            self.pedidos[self.numero_pedido] = pedido
            self.numero_pedido += 1
            print(f"Pedido {self.numero_pedido - 1} adicionado com sucesso!")

    def adicionar_item_pedido(self):
        numero_pedido = int(input("Digite o número do pedido: "))
        if numero_pedido in self.pedidos:
            pedido = self.pedidos[numero_pedido]
            item = input("Digite o nome do item: ").lower()
            if item in self.itens_menu:
                quantidade = int(input(f"Quantidade de {item}: "))
                if item in pedido:
                    pedido[item] += quantidade
                else:
                    pedido[item] = quantidade
                print(f"Item adicionado ao pedido {numero_pedido}.")
            else:
                print("Item não encontrado no menu. Tente novamente.")
        else:
            print("Pedido não encontrado.")

    def calcular_total_pedido(self, numero_pedido):
        pedido = self.pedidos.get(numero_pedido)
        if pedido:
            total = sum(self.itens_menu[item] * quantidade for item, quantidade in pedido.items())
            return total
        else:
            return None

    def visualizar_pedidos(self):
        for numero_pedido, pedido in self.pedidos.items():
            total_pedido = self.calcular_total_pedido(numero_pedido)
            print(f"Pedido {numero_pedido}: {pedido}, Total: R${total_pedido:.2f}")

restaurante = Restaurante()

while True:
    print("\nOpções:")
    print("1. Adicionar novo pedido")
    print("2. Adicionar item a pedido existente")
    print("3. Calcular total de um pedido")
    print("4. Visualizar todos os pedidos")
    print("5. Sair")
    escolha = input("Escolha uma opção: ")

    if escolha == "1":
        restaurante.adicionar_pedido()
    elif escolha == "2":
        restaurante.adicionar_item_pedido()
    elif escolha == "3":
        numero_pedido = int(input("Digite o número do pedido: "))
        total = restaurante.calcular_total_pedido(numero_pedido)
        if total is not None:
            print(f"Total do Pedido {numero_pedido}: R${total:.2f}")
        else:
            print("Pedido não encontrado.")
    elif escolha == "4":
        restaurante.visualizar_pedidos()
    elif escolha == "5":
        break
    else:
        print("Escolha inválida. Tente novamente.")
