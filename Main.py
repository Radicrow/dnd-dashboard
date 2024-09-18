import dash
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd
import plotly.express as px


df = pd.read_csv('imdb_movies.csv')

#Fazendo um explode para separar os gêneros
df['genre'] = df['genre'].str.split(',')
df = df.explode('genre')
df['genre'] = df['genre'].str.strip()
print(df[df['genre']== 'Animation'])

#tratamento de valores nulos
df.fillna('Unknown', inplace=True)

