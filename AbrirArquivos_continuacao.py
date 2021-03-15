import os
#verifica se o arquivo foi encontrado
try:
    file = open('abc.txt', 'w+')
    file.write('Linha1')
    file.seek(0)
    print(file.read())
#fecha o arquivo independente se o arquivo foi encontrado
finally:
    file.close

#Aqui fecha o arquivo automaticamente, maneira mais comum em python para salvar os arquivos em python
with open("abc.txt", "w+") as file:
    """ file.write('linha1\n')
    file.write('linha2\n')
    file.write('linha3\n')"""
    
    #Volta para a posicao inicial
    file.seek(0)
    print(file.read())

#Aqui fecha o arquivo automaticamente, maneira mais comum em python para salvar os arquivos em python
#a funcao "a", serve para poder adicionar mais linhas no arquivo
with open("abc.txt", "a+") as file:
    file.write('linha1\n')
    file.write('linha2\n')
    file.write('linha3\n')
    file.write('Outra linha')
    #Escreve outra linha sem apagar as demais, pois o cursor foi colocado na ultima posicao da leitura
    
    file.seek(0)
    #Volta para a posicao inicial
    file.seek(0)
    print(file.read())

#Para apagar devemos importar a seguinte funcao
#os.remove("abc.txt")