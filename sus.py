import array as ar


fila = []

def adicionar():
    add = input('Digite aqui o nome da pessoa:')
    prioridade = input(f'O {add} é prioridade? S/N:')
    if prioridade.capitalize() == 'S':
        fila.insert(0, add)
    else:
        fila.append(add)

def atendimento():
    print(f"{fila[0]} está sendo atendido")
    filar = fila.pop(0)
    print(filar)

def visualizar_fila():
    print(fila)

while True:
    print('\n Opções')
    print("1. ADICIONAR PESSOA A FILA \n2. ATENDER PROXIMA PESSOA \n3. VISUALIZAR FILA \n4. SAIR DO BANCO")
    opcao = input("ESCOLHA UMA OPÇÃO: ")
    if opcao == "1":
        adicionar()
    elif opcao == "2":
        atendimento()
    elif opcao == "3":
        visualizar_fila()
    elif opcao == "4":
        print('Saindo do banco...')
        break
    else:
        print('Opção inválida, tente um núḿero válido!')