import pandas as pd
import requests

url = "https://servicodados.ibge.gov.br/api/v1/localidades/estados"
response = requests.get(url)
data = response.json()

df = pd.DataFrame(data)
estados = pd.read_csv("estados/estados.csv")
merge = pd.merge(df, estados, on="sigla")
print(merge)