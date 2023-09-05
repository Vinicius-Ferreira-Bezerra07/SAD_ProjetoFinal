import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import streamlit as st 

# Importação da Database
dataBase = pd.read_csv('dataset.csv')
print(dataBase.head())
st.dataframe(dataBase)

# Title do Streamlit
st.title("Database - Predict students' dropout and academic success")

# Printagem de dados em console para vizualização
print(dataBase['Nacionality'].value_counts())
#___________________________________________________________________________
# # Histograma de alunos divididos por Nacionalidade
# st.write("Histograma de alunos divididos por Nacionalidade")
# fig1, ax1 = plt.subplots()
# ax1.hist(dataBase['Nacionality'], bins = 21)

# st.pyplot(fig1)

w = sidebar.title('Filtro os estudantes')

# Histograma de alunos divididos por curso
st.write("Histograma de alunos divididos por curso")
fig2, ax2 = plt.subplots()
ax2.hist(dataBase['Course'], bins = 17)
plt.xticks(range(17))

st.pyplot(fig2)

# Base da dados apenas com os estudantes que Abandonaram o Curso
st.write("Histograma de alunos que abandonaram as aulas por curso")
dataDropout = dataBase.query("Target == 'Dropout'")
fig3, ax3 = plt.subplots()
ax3.hist(dataDropout['Course'], bins=17)

st.pyplot(fig3)

# Base da dados apenas com os estudantes que Abandonaram o Curso
st.write("Histograma de alunos que se graduaram por curso")
dataGraduate = dataBase.query("Target == 'Graduate'")
fig4, ax4 = plt.subplots()
ax4.hist(dataGraduate['Course'], bins=17)

st.pyplot(fig4)