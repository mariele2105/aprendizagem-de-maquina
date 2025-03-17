import csv

# 1. Criar o arquivo dados.csv contendo Nome, Idade
dados = [
    ["Nome", "Idade"],
    ["Ana", 25],
    ["Bruno", 30],
    ["Carla", 22],
    ["Daniel", 28],
    ["Eduardo", 35]
]

# Escrevendo o arquivo CSV
with open('dados.csv', mode='w', newline='') as file:
    writer = csv.writer(file)
    writer.writerows(dados)

# 2. Ler o arquivo dados.csv e armazenar os dados em uma lista
pessoas = []
with open('dados.csv', mode='r') as file:
    reader = csv.reader(file)
    next(reader)  # Pular o cabeçalho
    for row in reader:
        nome = row[0]
        idade = int(row[1])
        pessoas.append({"nome": nome, "idade": idade})

# Solicitar ao usuário um nome
nome_input = input("Digite um nome: ")

# Verificar se o nome está na lista e exibir a idade e se é a pessoa mais velha
encontrado = False
mais_velho = max(pessoas, key=lambda p: p["idade"])

for pessoa in pessoas:
    if pessoa["nome"].lower() == nome_input.lower():
        encontrado = True
        if pessoa["idade"] == mais_velho["idade"]:
            print(f"{pessoa['nome']} tem {pessoa['idade']} anos, é a pessoa mais velha da lista.")
        else:
            print(f"{pessoa['nome']} tem {pessoa['idade']} anos, não é a pessoa mais velha da lista.")
        break

if not encontrado:
    print("Nome não encontrado.")
