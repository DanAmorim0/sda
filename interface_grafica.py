import tkinter as tk

def mostrar_mensagem():
    label.config(text="Você é gay!")

#criar uma janela
janela = tk.Tk() #busca na biblioteca
janela.title("Exemplo de GUI em Python")

#criar um rótulo
label = tk.Label(janela, text="Bem vindo à interface gráfica de usuário.")
label.pack(padx=100, pady=70)

#criar um botão do tipo CTA(call to action)
botao = tk.Button(janela, text="Clique aqui e descubra se você é gay!", command=mostrar_mensagem)
botao.pack(pady= 20, padx=20)

#Iniciar a GUI em loop
janela.mainloop()
    