import pandas as pd
import numpy as np
import os
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier

caminho_pasta = "DeveresDeCasa/Dever-05"
os.makedirs(caminho_pasta, exist_ok=True)  
caminho_arquivo = os.path.join(caminho_pasta, "imc_obesidade.csv")

data = {
    "IMC": [18.5, 20.0, 22.0, 24.0, 26.0, 28.0, 30.0, 32.0, 35.0, 40.0],
    "Obeso": [False, False, False, False, False, False, True, True, True, True]
}

df = pd.DataFrame(data)
df.to_csv(caminho_arquivo, index=False)
print(f"Arquivo CSV criado em: {caminho_arquivo}")

df = pd.read_csv(caminho_arquivo)

X = df[["IMC"]]
y = df["Obeso"]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

model = RandomForestClassifier(n_estimators=10, random_state=42)
model.fit(X_train, y_train)

novo_imc = np.array([[27.0]])  
previsao = model.predict(novo_imc)[0]

print(f"O modelo previu que um IMC de 27.0 é obeso: {previsao}")
