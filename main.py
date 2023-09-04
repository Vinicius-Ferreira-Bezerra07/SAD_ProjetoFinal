import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import streamlit as st 

# Importação da Database
dataBase = pd.read_csv('dataset.csv')
print(dataBase.head())

# Title do Streamlit
st.title("Database - Predict students' dropout and academic success")

# Printagem de dados em console para vizualização
print(dataBase['Nacionality'].value_counts())

# Histograma de alunos divididos por Nacionalidade
st.title("Histograma de alunos divididos por Nacionalidade")
fig1, ax1 = plt.subplots()
ax1.hist(dataBase['Nacionality'], bins = 21)

st.pyplot(fig1)
