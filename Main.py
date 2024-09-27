import pandas as pd
import plotly.express as px
import streamlit as st

st.set_page_config(layout="wide")

df = pd.read_csv('imdb_movies.csv')

#print(df.isnull().sum())

#Fazendo um explode para separar os gêneros
#df['genre'] = df['genre'].str.split(',')
#df = df.explode('genre')
#df['genre'] = df['genre'].str.strip()

#tratamento de valores nulos
df.fillna('Unknown', inplace=True)

#print(df.duplicated().sum())

df = df.rename(columns={'names': 'name', 'budget_x': 'budget_mil', 'revenue': 'revenue_mil', 'date_x': 'date', 'country': 'release_country'})

#print(list(df.columns))

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

df['income_tier'] = df['income_mil'].apply(lambda x: 
                                                "Financial Loss" if x < 0 \
                                             else "Low" if 0 <= x <= 10 \
                                             else "Mid" if 10 < x <= 100 \
                                             else "High" if 100 < x <= 250 \
                                             else "Very High")


p_genre = st.sidebar.selectbox("Genre", df["primary_genre"].unique())
df_filtered = df[df["primary_genre"] == p_genre]

df_filtered
col1, col2 = st.columns(2)

fig = px.pie(df_filtered, names ='income_tier', title='Distribution of Income Tiers', color_discrete_sequence=px.colors.sequential.RdBu)
col1.plotly_chart(fig)

#df['income_mil'].median()
#fig = px.bar(df_filtered, x ='', title='Distribution of Income Tiers', color_discrete_sequence=px.colors.sequential.RdBu)
#col1.plotly_chart(fig)

df_filtered['decade'] = (df['year']//10)*10

df_decade_median_filtered = df_filtered.groupby('decade')['income_mil'].median().reset_index()

fig_decade = px.bar(df_decade_median_filtered, x='decade', y='income_mil',
                    labels={'decade': 'Decade', 'income_mil': 'Income Median (Millions)'},
                    title='Median Income by Decade ',
                    color_discrete_sequence=px.colors.sequential.RdBu
                    )

col2.plotly_chart(fig_decade)



