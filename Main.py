from dash import html, dcc, Dash
import pandas as pd
import plotly.express as px


df = pd.read_csv('imdb_movies.csv')

#print(df.isnull().sum())

#Fazendo um explode para separar os gêneros
df['genre'] = df['genre'].str.split(',')
df = df.explode('genre')
df['genre'] = df['genre'].str.strip()

#tratamento de valores nulos
df.fillna('Unknown', inplace=True)

