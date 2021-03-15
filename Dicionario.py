import json

d1 ={
    'Pessoa 1': {
        'nome':'Luiz', 
        'idade': 25,
    },
    'Pessoa 2': {
        'nome' :'Rose', 
        'idade': 30,
    },
}

#Salva dados no arquivo principal, com dados do tipo json
d1_json = json.dumps(d1, indent = True)
with open('abc.txt', 'w+') as file:
    file.write(d1_json) #Escreve o dicionário como json, se quiser voltar e deixar o dicionario como estava antes
    #basta escrever: d1_json = json.load(d1_json)
print(d1_json)