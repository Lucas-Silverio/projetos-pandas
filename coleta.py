import requests
import pandas as pd

def encontrar_maior_ano(x):
    itens = []
    anos = []
    #Salvando os itens
    for i in x:
        itens.append({"Ano": i["year"], "Populacao" : i["value"]})
    #Salvando os anos
    for i in itens:
        anos.append(i["Ano"])
    #Procurando o item com maior ano
    for i in itens:
        if(i["Ano"] == max(anos)):
            return i
    return None

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
#Indexando o DF por Cidade
df_indexado_cidade = df.set_index("city")

df_novo = None

#Valor de I será a Cidade por se tratar do Index
for i,x in df_indexado_cidade.populationCounts.items():
    maior_ano = encontrar_maior_ano(x)
    if(maior_ano):
        df_auxiliar = pd.DataFrame([{"Cidade": i, "Ano" : maior_ano["Ano"], "População" : maior_ano["Populacao"]}])
        df_novo = pd.concat([df_novo,df_auxiliar],ignore_index=True)
    
print(df_novo)