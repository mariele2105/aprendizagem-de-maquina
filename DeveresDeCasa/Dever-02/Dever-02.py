# Função para solicitar e validar a entrada do usuário
def obter_frase():
    while True:
        frase = input("Digite uma frase: ")
        if frase.strip():  # Verifica se a frase não está vazia
            return frase
        else:
            print("Entrada vazia! Por favor, digite uma frase válida.")

# Função para realizar a análise da frase
def analisar_frase(frase):
    # Contagem de caracteres
    num_caracteres = len(frase)
    
    # Contagem de palavras (usando o método split para separar por espaços)
    palavras = frase.split()
    num_palavras = len(palavras)
    
    # Maior palavra (usando a função max para achar a maior em comprimento)
    maior_palavra = max(palavras, key=len) if palavras else ""
    
    return num_caracteres, num_palavras, maior_palavra, palavras

# Função para manipular e formatar a frase
def manipular_frase(frase, palavras):
    # Inversão da frase por caracteres
    frase_invertida_caracteres = frase[::-1]
    
    # Inversão da ordem das palavras
    frase_invertida_palavras = " ".join(palavras[::-1])
    
    # Alteração de caixa (maiúsculas e minúsculas)
    frase_maiuscula = frase.upper()
    frase_minuscula = frase.lower()
    
    # Tupla de palavras
    tupla_palavras = tuple(palavras)
    
    return (frase_invertida_caracteres, frase_invertida_palavras,
            frase_maiuscula, frase_minuscula, tupla_palavras)

# Função principal para controlar o fluxo do programa
def main():
    # Obter a frase do usuário
    frase = obter_frase()
    
    # Analisar a frase
    num_caracteres, num_palavras, maior_palavra, palavras = analisar_frase(frase)
    
    # Manipular e formatar a frase
    (frase_invertida_caracteres, frase_invertida_palavras, 
     frase_maiuscula, frase_minuscula, tupla_palavras) = manipular_frase(frase, palavras)
    
    # Exibir os resultados formatados
    print(f"\nResultados da análise da frase:")
    print(f"Frase original: '{frase}'")
    print(f"Número de caracteres: {num_caracteres}")
    print(f"Número de palavras: {num_palavras}")
    print(f"Maior palavra: '{maior_palavra}'")
    print(f"Frase invertida (por caracteres): '{frase_invertida_caracteres}'")
    print(f"Frase invertida (por palavras): '{frase_invertida_palavras}'")
    print(f"Frase em maiúsculas: '{frase_maiuscula}'")
    print(f"Frase em minúsculas: '{frase_minuscula}'")
    print(f"Tupla de palavras: {tupla_palavras}")

# Chamar a função principal para rodar o programa
main()