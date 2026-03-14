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

# %%
# Associação de Variáveis Categóricas
df_avc = df.select_dtypes(include="object")
df_avc

# %%
from scipy.stats import chi2_contingency

# %%
obs = pd.crosstab(df_avc["Sexo"], df["DoencaCard"]) # relaciona informação de duas colunas
obs

# %%
chi2, p_value, gl, expected = chi2_contingency(obs)
"""
chi2_contingency: O teste de Qui-Quadrado de independencia, 
serve para verificar uma associação entre duas variaveis,
neste caso, a relaçao entre sexo e a presença de doença cardiovascular

Saidas:
- chi2: a estatisca de teste calculada,
quanto maior este valor, mais os dados divergem do que seria esperado caso fossem independentes
(mais relacionados sao)

- p_value: O valor mais importante, se este valor for menor que 0,05(geralmente), 
descarta-se a hipotese nula e conclui que as variaveis estão relacionadas

- gl: grau de liberdade(dof - degrees of freedom) é calculado com base no numero de linhas e colunas da tabela

- expected: é uma nova tabela com as mesmas dimensoes do original(neste caso um 2x2), porem, 
contendo os valores esperadaos caso as variaveis fossem independentes
"""

# %%
print(f"{chi2}, \n{p_value}, \n{gl}, \n{expected}")

# %%
alpha = 0.05

# p_valor < alpha --> rejeita a hipotese (existe independencia entre as variveis)
# p_valor > alpha --> aceita a hipotese (existe independencia entre as variveis)

# %%
alpha > p_value

# %%
# Correlação de variaveis numericas
df_num = df.select_dtypes(include="number")
df_num

# %%
"""
.corr(): calcula a matriz de correlação de um df, 
o valor de intersecção de uma com uma coluna é chamado de 
COEFICIENTE DE RELAÇÃO DE PEARSON(r) dentre as duas variaveis
como lê-lo
r = 1: correlação positiva perfeita, os dois sao diretamente proporcionais
r = 0 nao existe correlaçao
r = -1: correlação negativa perfeita, os dois sao inversamente proporcionais
"""
corr = df_num.corr()
corr

# %%
plt.figure(figsize=(10*cms, 7*cms))
plt.imshow(corr.values)
plt.xticks(range(len(corr.columns)), corr.columns, rotation=45)
plt.yticks(range(len(corr.columns)), corr.columns)
plt.colorbar(label="Correlação")
plt.show()
# %%
