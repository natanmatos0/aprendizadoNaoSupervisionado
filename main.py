# %%
import pandas as pd # dataframes
import numpy as np # operações numericas
import matplotlib.pyplot as plt #mostrar dados 
import io #conversão de bytes

plt.rcParams.update({
    "font.family": "serif",
    "font.serif": ["CMU Serif", "Computer Modern", "DejaVu Serif"]
})

cms = 1/2.54

# %%
df = pd.read_excel("./data/DadosCoracao.xlsx")
df.head()

# %%
print(f"Idade minima: {df["Idade"].min()}")
print(f"Idade maxima: {df["Idade"].max()}")
print(f"Idade media: {df["Idade"].mean()}")
print(f"Desvio padrão da media das idades {df["Idade"].std()}")

# %%
# resume tudo que foi feito na linha anterior e dá ainda mais informações
df.describe()

# %%
print(f"Moda:  {df["Sexo"].mode().iloc[0]}") # Valor que mais se repete
print(f"Frequencia absoluta: \n {df["Sexo"].value_counts()}") # Mostra a quantidade de cada valor na coluna
print(f"Proporção: \n {df["Sexo"].value_counts(normalize=True)}") # Mostra a proporção entre os dois valores

# %%
# VISUALIZAÇÃO GRAFICA
counts = df["Sexo"].value_counts()# Mostra a quantidade de cada valor na coluna
counts

# %%
plt.figure(figsize=(10*cms, 7*cms))
plt.bar(counts.index, # acessa o eixo x(nome das colunas)
        counts.values, # acessa o eixo y(valores)
        color=["blue", "red"]
        )
plt.title("Distribuição de frequencia - Sexo")
plt.ylabel("Frequencia")

# %%
# Dispersão da idade, colesterol e Doença Cardíaca
plt.figure(figsize=(10*cms,7*cms))
colors = df["DoencaCard"].map( # define que pra caso seja sim, sera da cor azul, caso seja nao, sera vermelha
    {
    "Sim":"blue",
    "Nao": "red"
    }
)

plt.scatter(df["BCMax"], df["Colesterol"], c=colors,edgecolors="black") # define que sera um grafico de bolinhas

plt.xlabel("Batimentos")
plt.ylabel("Colesterol")
plt.show()


