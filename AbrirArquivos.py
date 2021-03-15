#https://docs.python.org/3/library/fun...
#link que mostra os modos de abertura

file = open('abc.txt', 'w+')
file.write('linha1\n')
file.write('linha2\n')
file.write('linha3\n')
#Fecha para nao causar problemas no sistema
file.seek(0, 0)             #encontrar a posicao absoluta do arquivo
print("Lendo linhas:")
print(file.read())

file.seek(0,0)              #volta o cursor na posicao inicial do arquivo
print(file.readline(), end="")      #ele linha por linha, end le ate o final
print(file.readline(), end= "")
print(file.readline(), end="")
print("###################")

#Colocando dentro de uma lista 
file.seek(0,0)
print(file.readlines()) #podemos facilmente associar essa funcao com uma list para assimilar os valores

#Plotando cada linha de outra maneira
for linha in file:
    print(linha)

file.close()