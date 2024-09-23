import pandas as pd
#import plotly.express as px
import streamlit as st


df = pd.read_csv('imdb_movies.csv')

#print(df.isnull().sum())

#Fazendo um explode para separar os gêneros
#df['genre'] = df['genre'].str.split(',')
#df = df.explode('genre')
#df['genre'] = df['genre'].str.strip()

#tratamento de valores nulos
df.fillna('Unknown', inplace=True)

print(df.duplicated().sum())

df = df.rename(columns={'names': 'name', 'budget_x': 'budget_mil', 'revenue': 'revenue_mil', 'date_x': 'date', 'country': 'release_country'})

print(list(df.columns))

df['income_mil'] = (df['revenue_mil'] - df['budget_mil'])/10**6

df['budget_mil'] = df['budget_mil'] / 10**6
df['revenue_mil'] = df['revenue_mil'] / 10**6

df['date'] = pd.to_datetime(df['date']) 

df['year'] = df['date'].dt.year

df['primary_genre'] = df['genre'].apply(lambda x: x.split(',')[0])

#print(df[['name', 'primary_genre']])

df['profitable'] = df['income_mil'].apply(lambda x: "Yes" if x > 0 else "No")

df = df.drop(['date', 'genre','overview','crew','orig_title','status'], axis=1)


#Remoção de filmes nao lançados sem nota, e outras informações relevantes 
df = df[df.score != 0]
df = df[df.revenue_mil != 0]
df = df[df.budget_mil != 0]
print(df.describe())

print(df.head())