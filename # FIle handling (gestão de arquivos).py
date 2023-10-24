# FIle handling (gestão de arquivos)
# Quais são as funções básicas para gestão de arquivo?
### ler (read)
### criar (create)
### acrescentar (append)

minha_lista = "/home/lab03/Área de Trabalho/daniboy/minhalista.txt"

'''lista_nomes = open(minha_lista, "r")
for x in lista_nomes:
    print(x)


with open(minha_lista, "rt") as lista:
    conteudo = lista.read()

print(conteudo)'''

f = open(minha_lista)
print(f.readline(3))
f.close()