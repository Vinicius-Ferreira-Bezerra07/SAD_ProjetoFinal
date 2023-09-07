# pip install streamlit pandas matplotlib seaborn
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

graph1_type = st.sidebar.selectbox("Gráfico 1: Selecione o tipo de gráfico", ("Barra", "Pizza"))

gsheets_url = 'https://docs.google.com/spreadsheets/d/1Xr6uPNAlT4n9FDuR91JyY2QwFGLGmMICPE5WqjW-s1k/edit#gid=' + "1378939680"
@st.cache_data(ttl=120)
def load_data(sheets_url):
    csv_url = sheets_url.replace("/edit#gid=", "/export?format=csv&gid=")
    return pd.read_csv(csv_url)

data = load_data(gsheets_url)

# Adicionando um título
st.title("Análise de Dados do Dataset SISREF")


#explode
explode = (0, 0.1, 0, 0)


# Adicionando um gráfico de barras
st.subheader("Distribuição de Refeicão por Horário")
refeicao_count = data['Refeicao'].value_counts()
fig, ax = plt.subplots()
if graph1_type == "Pizza":
    ax.pie(refeicao_count.values, labels=refeicao_count.index, autopct='%1.1f%%', explode=explode)
    ax.set_title('Distribuição de Refeicao dos Estudantes po Horário')
else:
    sns.barplot(x=refeicao_count.index, y=refeicao_count.values)
    ax.set_xlabel('Horários')
    ax.set_ylabel('Número de Estudantes')
st.pyplot(fig)

# Adicionando um gráfico de barras
st.subheader("Distribuição de Refeicão dos Estudantes Por curso")
curso_count = data['Curso'].value_counts()
fig, ax = plt.subplots()
if graph1_type == "Pizza":
    ax.pie(curso_count.values, labels=curso_count.index, autopct='%1.1f%%')
    ax.set_title('Distribuição de Refeicao dos Estudantes Por Curso')
else:
    sns.barplot(x=curso_count.index, y=curso_count.values)
    ax.set_xlabel('Cursos')
    ax.set_ylabel('Número de Estudantes que reservaram refeição')
st.pyplot(fig)

# Adicionando um gráfico de barras
st.subheader("Número de Alunos que faltaram a Refeição")
falta_count = data['Compareceu'].value_counts()
fig, ax = plt.subplots()
if graph1_type == "Pizza":
    ax.pie(falta_count.values, labels=falta_count.index, autopct='%1.1f%%')
    ax.set_title('Falta vs Presença')
else:
    sns.barplot(x=falta_count.index, y=falta_count.values)
    ax.set_xlabel('Presença')
    ax.set_ylabel('Número')
st.pyplot(fig)