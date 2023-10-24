"""Exercício: Gerenciamento de Lista de Nomes e Tipos Sanguíneos
Objetivo: Criar um programa Python que permita aos alunos gerenciar uma lista de nomes de pessoas e seus tipos sanguíneos. Os alunos serão instruídos a adicionar, visualizar e salvar os dados em um arquivo de texto.

Instruções:
Crie um programa Python que ofereça as seguintes funcionalidades:
a. Adicionar um novo nome e tipo sanguíneo à lista.
b. Visualizar a lista atual de nomes e tipos sanguíneos.
c. Salvar a lista em um arquivo de texto chamado "lista_tipos_sanguineos.txt".

O programa deve começar com uma lista vazia e dar ao usuário a opção de adicionar nomes e tipos sanguíneos. Eles devem ser capazes de adicionar quantas entradas desejarem.

O programa também deve permitir ao usuário visualizar a lista de nomes e tipos sanguíneos.

Após adicionar nomes e tipos sanguíneos, o programa deve fornecer a opção de salvar os dados em um arquivo de texto. Os dados devem ser formatados de forma legível.

Ao iniciar o programa, ele deve verificar se o arquivo "lista_tipos_sanguineos.txt" existe. Se o arquivo existir, o programa deve carregar os dados do arquivo no início da execução.

Dica: Você pode usar uma estrutura de dados como uma lista de dicionários para armazenar os nomes e tipos sanguíneos, e a função open() para criar ou carregar o arquivo. Certifique-se de lidar com exceções, como erros de abertura ou leitura de arquivo. """

# inicializa uma lista vazia para armazenas os dados
lista_de_pessoas = []

#nome do arquivo nonde vamos carregar os dados
nome_do_arquivo = "lista_tipos_sanguineos.txt"

#adicionar nome e tipo sanguineo a lista
def adicionar_nome_e_tipo_sanguineo():

    pessoas = input('Adicione nomes dos doadores: ')
    sangue = input('Escreva o tipo sanguineo do doador: ')
    pacientes = {
        "Nome": pessoas,
        "Tipo Sanguíneo": sangue
    }
    lista_de_pessoas.append(pacientes)
    print(f'Dados de {pacientes} armazenados com sucesso!')

#visualizar a lista de pacientes
def visualizar_lista():
    if not lista_de_pessoas:
        print("A lista está vazia")
    else:
        print("Lista de Nomes e Tipagem Sanguínea:")
        for pacientes in lista_de_pessoas:
            print(
                f"Nome: {pacientes['Nome']}, Tipo Sanguíneo: {pacientes['Tipo Sanguíneo']}"
            )
#salvar os dados em um arquivo txt
def salvar_dados():
    with open(nome_do_arquivo, "w") as arquivo:
        for pacientes in lista_de_pessoas:
            arquivo.write(
                f"Nome: {pacientes['Nome']}, Tipo Sanguíneo: {pacientes['Tipo Sanguíneo']}"
            )
        print("Arquivo gerado com sucesso!")

#Carregar dados
def carregar_dados():
    try:
        with open(nome_do_arquivo, "r") as arquivo:
            for linha in arquivo:
                dados = linha.strip().split(', ')
                nome = dados[0].split(": ")[1]
                tipo_sanguineo = dados[1].split(": ")[1]
                pessoa = {
                    "Nome": nome,
                    "Tipo Sanguíneo": tipo_sanguineo
                }
                lista_de_pessoas.append(pessoa)
            print("Dados carregados com sucesso!")
    except FileNotFoundError:
        print(f"ERRO! \n O arquivo {nome_do_arquivo} não foi encontrado. \n Contate o adm do sistema.")

carregar_dados()

#menu principal
while True:
    print('\n Opções')
    print(
        "1. ADICIONAR PACIENTE E TIPO SANGUÍNEO \n2. VISUALIZAR PACIENTES \n3. SALVAR DADOS EM ARQUIVO \nDa4. ENCERRAR O SISTEMA"
    )
    opcao = input("ESCOLHA UMA OPÇÃO: ")
    if opcao == "1":
        adicionar_nome_e_tipo_sanguineo()
    elif opcao == "2":
        visualizar_lista()
    elif opcao == "3":
        salvar_dados()
    elif opcao == "4":
        print('Desligando o sistema.')
        break
    else:
        print('Opção inválida, tente um núḿero válido!')

