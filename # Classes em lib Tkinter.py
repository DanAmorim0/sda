# Classes em lib Tkinter

# Classes
"""
Tk                # Classe para criar uma janela principal
Toplevel          # Classe para criar janelas secundárias
Frame             # Classe para criar quadros (frames) na interface
Label             # Classe para criar rótulos de texto
Button            # Classe para criar botões
Entry             # Classe para criar campos de entrada de texto
Text              # Classe para criar áreas de texto
Canvas            # Classe para criar áreas de desenho
Checkbutton       # Classe para criar caixas de verificação (checkbuttons)
Radiobutton       # Classe para criar botões de seleção (radiobuttons)
Scale             # Classe para criar barras de rolagem (scales)
Listbox           # Classe para criar listas de seleção
Menu              # Classe para criar menus
Scrollbar         # Classe para criar barras de rolagem
Combobox          # Classe para criar listas suspensas (comboboxes)
Message           # Classe para criar caixas de mensagem
MessageBox        # Classe para exibir caixas de diálogo
...
# Métodos

mainloop()        # Método para iniciar o loop da GUI
after()           # Método para agendar chamadas de função após um período de tempo
bind()            # Método para vincular eventos a funções
pack()            # Método para gerenciamento de geometria usando empacotamento
grid()            # Método para gerenciamento de geometria usando uma grade
place()           # Método para gerenciamento de geometria usando posicionamento absoluto
...
# Constantes
LEFT, RIGHT, TOP, BOTTOM  # Constantes para especificar a direção do empacotamento
YES, NO, BOTH             # Constantes para especificar como o widget deve se expandir

"""
import tkinter as tk
from tkinter import messagebox
import pesquisar_produto

pesquisar_produto.


def abrir_janela(mensagem):
    nova_janela = tk.Toplevel()
    nova_janela.title("Executando ação...")

    label = tk.Label(nova_janela, text=mensagem, padx=20, pady=20)
    label.pack()

    botao_fechar = tk.Button(nova_janela, text="SAIR", command = nova_janela.destroy)
    botao_fechar.pack(padx=20,pady=10)

#Funções para as diferentes funcionalidades do sistema ERP

def pesquisa_produto():
    abrir_janela("Pesquisar Produto")

def checar_estoque():
    abrir_janela("Checar stoque")

def acrescentar_estoque():
    abrir_janela("Acrescentar Estoque")

def remover_estoque():
    abrir_janela("Remover Estoque")

def cadastrar_produto():
    abrir_janela("Cadastrar Produto")

#criar janela principal

janela_princpal = tk.Tk()
janela_princpal.title("SISTEMA ERP IESGO")
janela_princpal.attributes('-fullscreen', True)

#Configurar ícones
icon_pesquisar = tk.PhotoImage(file="/home/lab03/Área de Trabalho/Python/DANIEL AMORIM, BOA NOITE FELIPE/icons/pesquisar.png")
icon_estoque = tk.PhotoImage(file="/home/lab03/Área de Trabalho/Python/DANIEL AMORIM, BOA NOITE FELIPE/icons/estoque.png")
icon_cadastrar = tk.PhotoImage(file="/home/lab03/Área de Trabalho/Python/DANIEL AMORIM, BOA NOITE FELIPE/icons/cadastrar.png")
icon_remove = tk.PhotoImage(file="/home/lab03/Área de Trabalho/Python/DANIEL AMORIM, BOA NOITE FELIPE/icons/lixeira.png")
icon_acrescentar = tk.PhotoImage(file="/home/lab03/Área de Trabalho/Python/DANIEL AMORIM, BOA NOITE FELIPE/icons/adicionar.png")

#criar botões com ícones
botao_pesquisar = tk.Button(janela_princpal, image=icon_pesquisar, command=pesquisa_produto)
botao_estoque = tk.Button(janela_princpal,image=icon_estoque, command=checar_estoque)
botao_acrescentar_estoque = tk.Button(janela_princpal, image=icon_acrescentar, command=acrescentar_estoque)
botao_remover_estoque = tk.Button(janela_princpal, image=icon_remove, command=remover_estoque)
botao_cadastrar_produto = tk.Button(janela_princpal, image=icon_cadastrar, command=cadastrar_produto)

#exibir botões na janela
botao_pesquisar.pack()
botao_estoque.pack()
botao_acrescentar_estoque.pack()
botao_cadastrar_produto.pack()
botao_remover_estoque.pack()

#loop da janela

janela_princpal.mainloop()