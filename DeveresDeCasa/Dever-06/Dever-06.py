from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier

def main():
    # Carregar dados
    iris = load_iris()
    X = iris.data
    y = iris.target

    # Separar treino e teste
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # Criar o modelo
    modelo = KNeighborsClassifier(n_neighbors=3)

    # Treinar o modelo
    modelo.fit(X_train, y_train)

    # Entrada do usuário
    try:
        print("Digite as características da flor:")
        sepal_length = float(input("Comprimento da sépala (cm): "))
        sepal_width = float(input("Largura da sépala (cm): "))
        petal_length = float(input("Comprimento da pétala (cm): "))
        petal_width = float(input("Largura da pétala (cm): "))
    except ValueError:
        print("Entrada inválida! Digite apenas números.")
        return

    # Previsão
    entrada = [[sepal_length, sepal_width, petal_length, petal_width]]
    predicao = modelo.predict(entrada)

    # Mostrar resultado
    nome_flor = iris.target_names[predicao[0]]
    print(f"A flor prevista é: {nome_flor}")

if __name__ == "__main__":
    main()

