import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Lendo a Base de dados
dataBase = pd.read_csv('dataset.csv')

# Limpando dos alunos que ainda estão cursando.
dataBase = dataBase[dataBase.Target != 'Enrolled']

# Criação da barra lateral com aalgumas seleções.
st.sidebar.title("Predict students' dropout and academic success")
# Seleção do filtro de Graduação e Desistencias da base.
baseSelecionada = st.sidebar.selectbox('Escolha o formato da base', ['Completa', 'Graduados', 'Abandonos'])
# Selecção de campos da tabala e suas legendas.
legenda = st.sidebar.selectbox('Escolha o campo que deseja consultar a Legenda', ['Martial status', 'Course', 'Daytime/evening', 'Previous qualification', 'Nacionality', "Mother's and Father's qualification"])

# Verifivação do Filtro da Base da dados.
# Base completa
if(baseSelecionada == 'Completa'):
    st.title("Dados dos estudantes Universitarios")
    st.dataframe(dataBase)

    st.write("Histograma de alunos divididos por curso")
    fig2, ax2 = plt.subplots()
    ax2.hist(dataBase['Course'], bins = 17)
    plt.xticks(range(17))

    st.pyplot(fig2)

# Base apenas com os alunos Graduados
elif (baseSelecionada == 'Graduados'):
    st.title("Dados dos estudantes Universitarios que se Graduaram")
    dataGraduate = dataBase.query("Target == 'Graduate'")
    st.dataframe(dataGraduate)

    st.write("Histograma de alunos Graduados divididos por curso")
    fig2, ax2 = plt.subplots()
    ax2.hist(dataGraduate['Course'], bins = 17)
    plt.xticks(range(17))

    st.pyplot(fig2)

# Base apensa com os alunos Desistentes
elif(baseSelecionada == 'Abandonos'):
    st.title("Dados dos estudantes Universitarios que abandonaram")
    dataDropout = dataBase.query("Target == 'Dropout'")
    st.dataframe(dataDropout)

    st.write("Histograma de alunos Desistentes divididos por curso")
    fig2, ax2 = plt.subplots()
    ax2.hist(dataDropout['Course'], bins = 17)
    plt.xticks(range(17))

    st.pyplot(fig2)

# Seleção da exibição de legendas
# Legeda Martial status
if(legenda == 'Martial status'):
    st.sidebar.write("1 - Solteiro")
    st.sidebar.write("2 - Casado")
    st.sidebar.write("3 - Viuvo")
    st.sidebar.write("4 - Divorciado")
    st.sidebar.write("5 - União de Fato")
    st.sidebar.write("6 - Separedo Judicialmente")

# Legeda Curso
elif(legenda == 'Course'):
    st.sidebar.write("1 - 33 - Tecnologias de Produção de Biocombustíveis")
    st.sidebar.write("2 - 171 - Animação e Design Multimédia")
    st.sidebar.write("3 - 8014 - Serviço Social")
    st.sidebar.write("4 - 9003 - Agronomia")
    st.sidebar.write("5 - 9070 - Design de Comunicação")
    st.sidebar.write("6 - 9085 - Enfermagem Veterinária")
    st.sidebar.write("7 - 9119 - Engenharia Informática")
    st.sidebar.write("8 - 9130 - Equinicultura")
    st.sidebar.write("9 - 9147 - Gestão")
    st.sidebar.write("10 - 9238 - Serviço Social")
    st.sidebar.write("11 - 9254 - Turismo")
    st.sidebar.write("12 - 9500 - Enfermagem")
    st.sidebar.write("13 - 9556 - Higiene Oral")
    st.sidebar.write("14 - 9670 - Gestão de Publicidade e Marketing")
    st.sidebar.write("15 - 9773 - Jornalismo e Comunicação")
    st.sidebar.write("16 - 9853 - Ensino Básico")
    st.sidebar.write("17 - 9991 - Gestão")

# Legeda Horarios de aulas
elif(legenda == 'Daytime/evening'):
    st.sidebar.write('1 - diurno')
    st.sidebar.write('0 - noturno')

# Legeda Qualificações anteriores
elif(legenda == 'Previous qualification'):
    st.sidebar.write("1 - Ensino secundário")
    st.sidebar.write("2 – Ensino superior – bacharelado")
    st.sidebar.write("3 – Ensino superior – licenciatura")
    st.sidebar.write("4 – Ensino superior – mestrado")
    st.sidebar.write("5 – Ensino superior – doutorado")
    st.sidebar.write("6 – Frequência do ensino superior")
    st.sidebar.write("7  9º ano de escolaridade - não concluído")
    st.sidebar.write("8  10º ano de escolaridade - não concluído")
    st.sidebar.write("9  11º ano de escolaridade - não concluído")
    st.sidebar.write("10  12º ano de escolaridade - não concluído")
    st.sidebar.write("11 - 10º ano de escolaridade - não concluído")
    st.sidebar.write("12 - 11º ano de escolaridade - não concluído")
    st.sidebar.write("13 - Outros - 11º ano de escolaridade")
    st.sidebar.write("14 - 10º ano de escolaridade")
    st.sidebar.write("15 - 10º ano de escolaridade - não concluído")
    st.sidebar.write("19 - Ensino básico 3.º ciclo (9.º/10.º/11.º ano) ou equiv.")

# Legeda Nacionalidade
elif(legenda == 'Nacionality'):
    st.sidebar.write("1 - Português")
    st.sidebar.write("3 - Frances")
    st.sidebar.write("9 - Marroquino")
    st.sidebar.write("12 - Argelino")
    st.sidebar.write("14 - Inglês")

# Legeda Qualificações da Mãe e do Pai
elif(legenda = "Mother's and Father's qualification"):
    st.sidebar.write("2 - Ensino Superior - Bacharelado")
    st.sidebar.write("3 – Ensino Superior – Licenciatura")
    st.sidebar.write("4 – Ensino Superior – Mestrado")
    st.sidebar.write("5 – Ensino Superior – Doutorado")
    st.sidebar.write("6 - Frequência do Ensino Superior")
    st.sidebar.write("9 - 12º Ano de Escolaridade - Não Concluído")
    st.sidebar.write("10 - 11º Ano de Escolaridade - Não Concluído")
    st.sidebar.write("11 - 7º ano (antigo)")
    st.sidebar.write("12 - Outros - 11º Ano de Escolaridade")
    st.sidebar.write("14 - 10º Ano de Escolaridade")
    st.sidebar.write("18 – Curso de comércio geral")
    st.sidebar.write("19 - Ensino Básico 3.º Ciclo (9.º/10.º/11.º Ano) ou Equiv.")
