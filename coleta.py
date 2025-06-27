import requests
import pandas as pd

#Finlandia cidades :
corpo = {
    "limit" : 5,
    "order" : "asc",
    "orderBy" : "name",
    "country" : "finland"
}

resposta = requests.post("https://countriesnow.space/api/v0.1/countries/population/cities/filter",json=corpo)
#Todos os dados: 
dados = resposta.json()["data"]
df = pd.DataFrame(dados)
#Instancia do resultado
df_finlandia = None
#Refatorando usando apenas o DataFrame inicial
for indice,cidade,pais,popCount in df.itertuples():
    #Uso de função anonima para encontrar o maior pela chave year da lista de dictionaries que popCount retorna
    item_maior_ano = max(popCount, key=lambda chave : chave["year"])
    df_auxiliar = pd.DataFrame([{"Cidade": cidade,"País" : pais, "Ano" : item_maior_ano["year"], "População" : item_maior_ano["value"]}])
    df_finlandia = pd.concat([df_finlandia,df_auxiliar],ignore_index=True)

if df_finlandia is not None:
    print(df_finlandia)