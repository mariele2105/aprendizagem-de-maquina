import random
import pandas as pd

# Passo 1: Criando a lista de frutas (com frutas repetidas)
frutas = ["maçã", "banana", "laranja", "uva", "maçã", "melão", "mamão", "banana"]

# Passo 2: Criando o arquivo "minhas_frutas.txt" e gravando as frutas com quantidades aleatórias
with open("minhas_frutas.txt", "w") as f:
    for fruta in frutas:
        quantidade = random.randint(0, 100)
        f.write(f"{fruta},{quantidade}\n")

# Passo 3: Lendo o arquivo e carregando os dados em um DataFrame
# Primeiro, abrimos o arquivo e lemos as linhas
frutas_dict = {}
with open("minhas_frutas.txt", "r") as f:
    for linha in f:
        fruta, quantidade = linha.strip().split(",")
        quantidade = int(quantidade)
        
        # Somando as quantidades para frutas repetidas
        if fruta in frutas_dict:
            frutas_dict[fruta] += quantidade
        else:
            frutas_dict[fruta] = quantidade

# Passo 4: Criando o DataFrame
df = pd.DataFrame(list(frutas_dict.items()), columns=["Fruta", "Quantidade"])

# Exibindo o DataFrame
print(df)
