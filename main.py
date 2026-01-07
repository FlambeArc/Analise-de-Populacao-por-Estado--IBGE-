import pandas as pd
import requests
import matplotlib.pyplot as plt

url = "https://servicodados.ibge.gov.br/api/v1/localidades/estados"
response = requests.get(url)
data = response.json()

df = pd.DataFrame(data)
estados = pd.read_csv("estados/estados.csv")
merge = pd.merge(df, estados, on="sigla")
merge["população relativa 2024"] = merge["população estimada 2024"] / merge["área (1.000 Km²)"]
merge["população relativa 2025"] = merge["população estimada 2025"] / merge["área (1.000 Km²)"]
df_popumaior24 = merge[["sigla", "nome", "população estimada 2024"]].sort_values(by="população estimada 2024", ascending=False)
df_popumaior24 = df_popumaior24.set_index("sigla")
df_popumenor25 = merge[["sigla", "nome", "população estimada 2025"]].sort_values(by="população estimada 2025")
df_popumenor25 = df_popumenor25.set_index("sigla")
df_areamaior = merge[["sigla", "nome", "área (1.000 Km²)"]].sort_values(by="área (1.000 Km²)", ascending=False)
df_areamaior = df_areamaior.set_index("sigla")
df_crescimento = merge.set_index("sigla")[["população estimada 2024", "população estimada 2025"]]

print(merge)
print("")
print("Ordenado pelo maior numero de população de 2024")
print(df_popumaior24)
print("")
print("Ordenado pelo menor numero de população de 2025")
print(df_popumenor25)
print("")
print("Ordenado pela maior área territorial")
print(df_areamaior)

df_popumaior24.plot(kind="bar")
plt.title("Ordenado pelo maior numero de população de 2024")
plt.xlabel("Estados")
plt.ylabel("População em Milhões")
plt.savefig("População 2024")
plt.show()

df_popumenor25.plot(kind="bar")
plt.title("Ordenado pelo menor numero de população de 2025")
plt.xlabel("Estados")
plt.ylabel("População em Milhões")
plt.savefig("População 2025")
plt.show()

df_areamaior.plot(kind="bar")
plt.title("Ordenado pela maior área territorial")
plt.xlabel("Estados")
plt.ylabel("área (1.000 Km²)")
plt.savefig("Área por Estados")
plt.show()

df_crescimento.plot(kind='bar')
plt.title('População por estado (2024 x 2025)')
plt.xlabel('Estado')
plt.ylabel('População em Milhões')
plt.savefig("Crescimento (2024 x 2025)")
plt.show()

merge.to_csv("Analise de População por Estado")
df_popumaior24.to_csv("População 2024")
df_popumenor25.to_csv("População 2025")
df_areamaior.to_csv("Área por Estado")
