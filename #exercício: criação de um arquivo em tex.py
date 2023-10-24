#exercício: criação de um arquivo em texto via terminal
#objetivo: criar um arquivo de texto chamado "meuarquivo.txt usando o console."

nome_do_arquivo = "meuarquivo.txt"

with open(nome_do_arquivo, "w") as arquivo:
    arquivo.write("Este é o conteúdo do arquivo de revisão!!!")

print(f"O arquivo {nome_do_arquivo} foi criado com sucesso!")