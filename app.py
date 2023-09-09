import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Link para collab onde tem ulgumas tabelas filtros de exemplo
# https://colab.research.google.com/drive/1GN-y2J88mMGIIdlvBao-gTvVLNAHyrd7?usp=sharing

# Lendo a Base de dados
dataBase = pd.read_csv('dataset.csv')

# Limpando dos alunos que ainda estão cursando.
dataBase = dataBase[dataBase.Target != 'Enrolled']

# Criação da barra lateral com aalgumas seleções.
st.sidebar.title("Predict students' dropout and academic success")
# Seleção do filtro de Graduação e Desistencias da base.
baseSelecionada = st.sidebar.selectbox('Escolha o formato da base', ['Completa', 'Graduados', 'Abandonos'])
# Selecção de campos da tabala e suas legendas.
legenda = st.sidebar.selectbox('Escolha o campo que deseja consultar a Legenda', ['Martial status', 'Application mode', 'Course', 'Daytime/evening', 'Previous qualification', 'Nacionality', "Mother's and Father's qualification", "Gender"])

# Verifivação do Filtro da Base da dados.
# Base completa
if(baseSelecionada == 'Completa'):
    st.title("Dados dos estudantes Universitarios")
    st.dataframe(dataBase)

    selectColuna = st.selectbox("Escolha a coluna a ser exibida", ["", "Marital status", "Application mode", "Application order", "Course", "Daytime/evening attendance", "Previous qualification", "Nacionality", "Mother's qualification", "Father's qualification", "Displaced", "Educational special needs", "Debtor", "Tuition fees up to date", "Gender", "Scholarship holder", "Age at enrollment", "International", "Curricular units 1st sem (credited)", "Curricular units 1st sem (enrolled)", "Curricular units 1st sem (evaluations)", "Curricular units 1st sem (approved)", "Curricular units 1st sem (grade)", "Curricular units 1st sem (without evaluations)", "Curricular units 2nd sem (credited)", "Curricular units 2nd sem (enrolled)", "Curricular units 2nd sem (evaluations)", "Curricular units 2nd sem (approved)", "Curricular units 2nd sem (grade)", "Curricular units 2nd sem (without evaluations)", "Unemployment rate", "Inflation rate", "GDP"])
    # Seleção de histograma vazio
    if(selectColuna == ""):
        print(".1")
    
    # Seleção de histograma do Aplicação
    elif(selectColuna == "Marital status"):
        st.write("Histograma de alunos por Aplicação")
        fig, ax2 = plt.subplots()
        ax2.hist(dataBase[selectColuna], rwidth=0.8)
        plt.xticks(range(8))

        st.pyplot(fig)
    
    # Seleção de histograma do Forma de Aplicação
    elif(selectColuna == "Application mode"):
        st.write("Histograma de alunos por Aplicação")
        fig, ax2 = plt.subplots()
        ax2.hist(dataBase[selectColuna], bins= 18, range=[1,18], rwidth=0.9)
        plt.xticks(range(19))

        st.pyplot(fig)

    # Seleção de histograma do Ordem de Aplicação
    elif(selectColuna == "Application order"):
        st.write("Histograma de alunos por Ordem de aplicação")
        fig, ax2 = plt.subplots()
        ax2.hist(dataBase[selectColuna], range=[1,8], rwidth=0.8)
        # plt.xticks(range(8))

        st.pyplot(fig)

    # Seleção de histograma do Curso
    elif(selectColuna == "Course"):
        st.write("")
        st.write("Histograma de alunos divididos por curso")
        fig, ax2 = plt.subplots()
        ax2.hist(dataBase[selectColuna], bins = 17)
        plt.xticks(range(17))

        st.pyplot(fig)

    # Seleção de histograma do horario de aulas
    elif(selectColuna == "Daytime/evening attendance"):
        st.write("Histograma de alunos por Horario das aulas")
        fig, ax2 = plt.subplots()
        ax2.hist(dataBase[selectColuna], rwidth=0.8)
        plt.xticks(range(2))

        st.pyplot(fig)

    # Seleção de histograma do qualificação previa
    elif(selectColuna == "Previous qualification"):
        st.write("Histograma de alunos por qualificação previa")
        fig, ax2 = plt.subplots()
        ax2.hist(dataBase[selectColuna], rwidth=0.5)
        plt.xticks(range(18))

        st.pyplot(fig)

    # Seleção de histograma do Nacionalidade
    elif(selectColuna == "Nacionality"):
        st.write("Histograma de alunos por Nacionalidade")
        fig, ax2 = plt.subplots()
        ax2.hist(dataBase[selectColuna], rwidth=0.2)
        plt.xticks(range(21))

        st.pyplot(fig)
    
    # Seleção de histograma do qualificações da mãe
    elif(selectColuna == "Mother's qualification"):
        st.write("Histograma de alunos por Qualificações da mãe")
        fig, ax2 = plt.subplots()
        ax2.hist(dataBase[selectColuna], rwidth=0.3)
        plt.xticks(range(30))

        st.pyplot(fig)
    
    # Seleção de histograma do qualificações do pai
    elif(selectColuna == "Fathe's qualification"):
        st.write("Histograma de alunos por Qualificações da pai")
        fig, ax2 = plt.subplots()
        ax2.hist(dataBase[selectColuna], rwidth=0.3)
        plt.xticks(range(30))

        st.pyplot(fig)
    
    # Seleção de histograma do Deslocado
    elif(selectColuna == "Displaced"):
        st.write("Histograma de alunos por Deslocado")
        fig, ax2 = plt.subplots()
        ax2.hist(dataBase[selectColuna], rwidth=0.8)
        plt.xticks(range(2))

        st.pyplot(fig)
    
    # Seleção de histograma do Necessidades educacionais especiais
    elif(selectColuna == "Educational special needs"):
        st.write("Histograma de alunos por necessidades educacionais especiais")
        fig, ax2 = plt.subplots()
        ax2.hist(dataBase[selectColuna], rwidth=0.8)
        plt.xticks(range(2))

        st.pyplot(fig)

    # Seleção de histograma do Devedor
    elif(selectColuna == "Debtor"):
        st.write("Histograma de alunos por Devedor")
        fig, ax2 = plt.subplots()
        ax2.hist(dataBase[selectColuna], rwidth=0.8)
        plt.xticks(range(2))

        st.pyplot(fig)

    # Seleção de histograma do Mensalidades em dia
    elif(selectColuna == "Tuition fees up to date"):
        st.write("Histograma de alunos por Mensalidade em dia")
        fig, ax2 = plt.subplots()
        ax2.hist(dataBase[selectColuna], rwidth=0.8)
        plt.xticks(range(2))

        st.pyplot(fig)

    # Seleção de histograma por Generos
    elif(selectColuna == "Gender"):
        st.write("Histograma de alunos por Genero")
        fig, ax2 = plt.subplots()
        ax2.hist(dataBase[selectColuna], rwidth=0.8)
        plt.xticks(range(2))

        st.pyplot(fig)

    # Seleção de histograma por Bolsistas
    elif(selectColuna == "Scholarship holder"):
        st.write("Histograma de alunos por Bolsistas")
        fig, ax2 = plt.subplots()
        ax2.hist(dataBase[selectColuna], rwidth=0.8)
        plt.xticks(range(2))

        st.pyplot(fig)

    # Seleção de histograma por Idade na Inscrição
    elif(selectColuna == "Age at enrollment"):
        st.write("Histograma de alunos por Idade na Inscrição")
        fig, ax2 = plt.subplots()
        ax2.hist(dataBase[selectColuna], rwidth=0.8)
        plt.xticks(range(46))

        st.pyplot(fig)

    # Seleção de histograma pelo campo Internacional
    elif(selectColuna == "International"):
        st.write("Histograma de alunos por Internacional")
        fig, ax2 = plt.subplots()
        ax2.hist(dataBase[selectColuna], rwidth=0.8)
        plt.xticks(range(2))

        st.pyplot(fig)

    # Seleção de histograma das Unidades curriculares 1º semestre (creditadas)
    elif(selectColuna == "Curricular units 1st sem (credited)"):
        st.write("Histograma de alunos por Unidades curriculares 1º semestre (creditadas)")
        fig, ax2 = plt.subplots()
        ax2.hist(dataBase[selectColuna], rwidth=0.5)
        plt.xticks(range(21))

        st.pyplot(fig)

    # Seleção de histograma das Unidades curriculares 1º semestre (matriculado)
    elif(selectColuna == "Curricular units 1st sem (enrolled)"):
        st.write("Histograma de alunos por Unidades curriculares 1º semestre (matriculado)")
        fig, ax2 = plt.subplots()
        ax2.hist(dataBase[selectColuna], rwidth=0.5)
        plt.xticks(range(23))

        st.pyplot(fig)

    # Seleção de histograma das Unidades curriculares 1º semestre (avaliações)
    elif(selectColuna == "Curricular units 1st sem (evaluations)"):
        st.write("Histograma de alunos por Unidades curriculares 1º semestre (avaliações)")
        fig, ax2 = plt.subplots()
        ax2.hist(dataBase[selectColuna], rwidth=0.8)
        plt.xticks(range(8))

        st.pyplot(fig)

    # Seleção de histograma das Unidades curriculares 1º semestre (aprovado)
    elif(selectColuna == "Curricular units 1st sem (approved)"):
        st.write("Histograma de alunos por Unidades curriculares 1º semestre (aprovado)")
        fig, ax2 = plt.subplots()
        ax2.hist(dataBase[selectColuna], rwidth=0.2)
        plt.xticks(range(35))

        st.pyplot(fig)

    # Seleção de histograma das Unidades curriculares 1º semestre (Nota)
    elif(selectColuna == "Curricular units 1st sem (grade)"):
        st.write("Histograma de alunos por Unidades curriculares 1º semestre (Nota)")
        fig, ax2 = plt.subplots()
        ax2.hist(dataBase[selectColuna], rwidth=0.8)
        plt.xticks(range(8))

        st.pyplot(fig)

    # Seleção de histograma das Unidades curriculares 1º semestre (sem avaliações)
    elif(selectColuna == "Curricular units 1st sem (without evaluations)"):
        st.write("Histograma de alunos por Unidades curriculares 1º semestre (sem avaliações)")
        fig, ax2 = plt.subplots()
        ax2.hist(dataBase[selectColuna], rwidth=0.7)
        plt.xticks(range(11))

        st.pyplot(fig)

    # Seleção de histograma das Unidades curriculares 2º semestre (creditadas)
    elif(selectColuna == "Curricular units 2nd sem (credited)"):
        st.write("Histograma de alunos por Unidades curriculares 2º semestre (creditadas)")
        fig, ax2 = plt.subplots()
        ax2.hist(dataBase[selectColuna], rwidth=0.4)
        plt.xticks(range(21))

        st.pyplot(fig)

    # Seleção de histograma das Unidades curriculares 2º semestre (matriculado)
    elif(selectColuna == "Curricular units 2nd sem (enrolled)"):
        st.write("Histograma de alunos por Unidades curriculares 2º semestre (matriculado)")
        fig, ax2 = plt.subplots()
        ax2.hist(dataBase[selectColuna], rwidth=0.3)
        plt.xticks(range(23))

        st.pyplot(fig)

    # Seleção de histograma das Unidades curriculares 2º semestre (avaliações)
    elif(selectColuna == "Curricular units 2nd sem (evaluations)"):
        st.write("Histograma de alunos por Unidades curriculares 2º semestre (avaliações)")
        fig, ax2 = plt.subplots()
        ax2.hist(dataBase[selectColuna], rwidth=0.8)
        plt.xticks(range(8))

        st.pyplot(fig)

    # Seleção de histograma das Unidades curriculares 2º semestre (aprovado)
    elif(selectColuna == "Curricular units 2nd sem (approved)"):
        st.write("Histograma de alunos por Unidades curriculares 2º semestre (aprovado)")
        fig, ax2 = plt.subplots()
        ax2.hist(dataBase[selectColuna], rwidth=0.2)
        plt.xticks(range(35))

        st.pyplot(fig)

    # Seleção de histograma das Unidades curriculares 2º semestre (Nota)
    elif(selectColuna == "Curricular units 2nd sem (grade)"):
        st.write("Histograma de alunos por Unidades curriculares 2º semestre (Nota)")
        fig, ax2 = plt.subplots()
        ax2.hist(dataBase[selectColuna], rwidth=0.8)
        plt.xticks(range(8))

        st.pyplot(fig)

    # Seleção de histograma das Unidades curriculares 2º semestre (sem avaliações)
    elif(selectColuna == "Curricular units 2nd sem (without evaluations)"):
        st.write("Histograma de alunos por Unidades curriculares 2º semestre (sem avaliações)")
        fig, ax2 = plt.subplots()
        ax2.hist(dataBase[selectColuna], rwidth=0.7)
        plt.xticks(range(11))

        st.pyplot(fig)

    # Seleção de histograma do taxa de desemprego
    elif(selectColuna == "Unemployment rate"):
        st.write("Histograma de alunos por taxa de desemprego")
        fig, ax2 = plt.subplots()
        ax2.hist(dataBase[selectColuna], rwidth=0.8)
        plt.xticks(range(8))

        st.pyplot(fig)

    # Seleção de histograma do taxa de inflação
    elif(selectColuna == "Inflation rate"):
        st.write("Histograma de alunos por taxa de inflação")
        fig, ax2 = plt.subplots()
        ax2.hist(dataBase[selectColuna], rwidth=1)
        # plt.xticks(range(9))

        st.pyplot(fig)

    # Seleção de histograma do GPD
    elif(selectColuna == "GDP"):
        st.write("Histograma de alunos por GPD")
        fig, ax2 = plt.subplots()
        ax2.hist(dataBase[selectColuna], rwidth=0.8)
        plt.xticks(range(8))

        st.pyplot(fig)


# Base apenas com os alunos Graduados
elif (baseSelecionada == 'Graduados'):
    st.title("Dados dos estudantes Universitarios que se Graduaram")
    dataGraduate = dataBase.query("Target == 'Graduate'")
    st.dataframe(dataGraduate)

    selectColuna = st.selectbox("Escolha a coluna a ser exibida", ["", "Marital status", "Application mode", "Application order", "Course", "Daytime/evening attendance", "Previous qualification", "Nacionality", "Mother's qualification", "Father's qualification", "Displaced", "Educational special needs", "Debtor", "Tuition fees up to date", "Gender", "Scholarship holder", "Age at enrollment", "International", "Curricular units 1st sem (credited)", "Curricular units 1st sem (enrolled)", "Curricular units 1st sem (evaluations)", "Curricular units 1st sem (approved)", "Curricular units 1st sem (grade)", "Curricular units 1st sem (without evaluations)", "Curricular units 2nd sem (credited)", "Curricular units 2nd sem (enrolled)", "Curricular units 2nd sem (evaluations)", "Curricular units 2nd sem (approved)", "Curricular units 2nd sem (grade)", "Curricular units 2nd sem (without evaluations)", "Unemployment rate", "Inflation rate", "GDP"])
    # Seleção de histograma vazio
    if(selectColuna == ""):
        print(".1")
    
    # Seleção de histograma do Aplicação
    elif(selectColuna == "Marital status"):
        st.write("Histograma de alunos por Aplicação")
        fig, ax2 = plt.subplots()
        ax2.hist(dataGraduate[selectColuna], rwidth=0.8)
        plt.xticks(range(8))

        st.pyplot(fig)
    
    # Seleção de histograma do Forma de Aplicação
    elif(selectColuna == "Application mode"):
        st.write("Histograma de alunos por Aplicação")
        fig, ax2 = plt.subplots()
        ax2.hist(dataGraduate[selectColuna], bins= 18, range=[1,18], rwidth=0.9)
        plt.xticks(range(19))

        st.pyplot(fig)

    # Seleção de histograma do Ordem de Aplicação
    elif(selectColuna == "Application order"):
        st.write("Histograma de alunos por Ordem de aplicação")
        fig, ax2 = plt.subplots()
        ax2.hist(dataGraduate[selectColuna], range=[1,8], rwidth=0.8)
        # plt.xticks(range(8))

        st.pyplot(fig)

    # Seleção de histograma do Curso
    elif(selectColuna == "Course"):
        st.write("")
        st.write("Histograma de alunos divididos por curso")
        fig, ax2 = plt.subplots()
        ax2.hist(dataGraduate[selectColuna], bins = 17)
        plt.xticks(range(17))

        st.pyplot(fig)

    # Seleção de histograma do horario de aulas
    elif(selectColuna == "Daytime/evening attendance"):
        st.write("Histograma de alunos por Horario das aulas")
        fig, ax2 = plt.subplots()
        ax2.hist(dataGraduate[selectColuna], rwidth=0.8)
        plt.xticks(range(2))

        st.pyplot(fig)

    # Seleção de histograma do qualificação previa
    elif(selectColuna == "Previous qualification"):
        st.write("Histograma de alunos por qualificação previa")
        fig, ax2 = plt.subplots()
        ax2.hist(dataGraduate[selectColuna], rwidth=0.5)
        plt.xticks(range(18))

        st.pyplot(fig)

    # Seleção de histograma do Nacionalidade
    elif(selectColuna == "Nacionality"):
        st.write("Histograma de alunos por Nacionalidade")
        fig, ax2 = plt.subplots()
        ax2.hist(dataGraduate[selectColuna], rwidth=0.2)
        plt.xticks(range(21))

        st.pyplot(fig)
    
    # Seleção de histograma do qualificações da mãe
    elif(selectColuna == "Mother's qualification"):
        st.write("Histograma de alunos por Qualificações da mãe")
        fig, ax2 = plt.subplots()
        ax2.hist(dataGraduate[selectColuna], rwidth=0.3)
        plt.xticks(range(30))

        st.pyplot(fig)
    
    # Seleção de histograma do qualificações do pai
    elif(selectColuna == "Fathe's qualification"):
        st.write("Histograma de alunos por Qualificações da pai")
        fig, ax2 = plt.subplots()
        ax2.hist(dataGraduate[selectColuna], rwidth=0.3)
        plt.xticks(range(30))

        st.pyplot(fig)
    
    # Seleção de histograma do Deslocado
    elif(selectColuna == "Displaced"):
        st.write("Histograma de alunos por Deslocado")
        fig, ax2 = plt.subplots()
        ax2.hist(dataGraduate[selectColuna], rwidth=0.8)
        plt.xticks(range(2))

        st.pyplot(fig)
    
    # Seleção de histograma do Necessidades educacionais especiais
    elif(selectColuna == "Educational special needs"):
        st.write("Histograma de alunos por necessidades educacionais especiais")
        fig, ax2 = plt.subplots()
        ax2.hist(dataGraduate[selectColuna], rwidth=0.8)
        plt.xticks(range(2))

        st.pyplot(fig)

    # Seleção de histograma do Devedor
    elif(selectColuna == "Debtor"):
        st.write("Histograma de alunos por Devedor")
        fig, ax2 = plt.subplots()
        ax2.hist(dataGraduate[selectColuna], rwidth=0.8)
        plt.xticks(range(2))

        st.pyplot(fig)

    # Seleção de histograma do Mensalidades em dia
    elif(selectColuna == "Tuition fees up to date"):
        st.write("Histograma de alunos por Mensalidade em dia")
        fig, ax2 = plt.subplots()
        ax2.hist(dataGraduate[selectColuna], rwidth=0.8)
        plt.xticks(range(2))

        st.pyplot(fig)

    # Seleção de histograma por Generos
    elif(selectColuna == "Gender"):
        st.write("Histograma de alunos por Genero")
        fig, ax2 = plt.subplots()
        ax2.hist(dataGraduate[selectColuna], rwidth=0.8)
        plt.xticks(range(2))

        st.pyplot(fig)

    # Seleção de histograma por Bolsistas
    elif(selectColuna == "Scholarship holder"):
        st.write("Histograma de alunos por Bolsistas")
        fig, ax2 = plt.subplots()
        ax2.hist(dataGraduate[selectColuna], rwidth=0.8)
        plt.xticks(range(2))

        st.pyplot(fig)

    # Seleção de histograma por Idade na Inscrição
    elif(selectColuna == "Age at enrollment"):
        st.write("Histograma de alunos por Idade na Inscrição")
        fig, ax2 = plt.subplots()
        ax2.hist(dataGraduate[selectColuna], rwidth=0.8)
        plt.xticks(range(46))

        st.pyplot(fig)

    # Seleção de histograma pelo campo Internacional
    elif(selectColuna == "International"):
        st.write("Histograma de alunos por Internacional")
        fig, ax2 = plt.subplots()
        ax2.hist(dataGraduate[selectColuna], rwidth=0.8)
        plt.xticks(range(2))

        st.pyplot(fig)

    # Seleção de histograma das Unidades curriculares 1º semestre (creditadas)
    elif(selectColuna == "Curricular units 1st sem (credited)"):
        st.write("Histograma de alunos por Unidades curriculares 1º semestre (creditadas)")
        fig, ax2 = plt.subplots()
        ax2.hist(dataGraduate[selectColuna], rwidth=0.5)
        plt.xticks(range(21))

        st.pyplot(fig)

    # Seleção de histograma das Unidades curriculares 1º semestre (matriculado)
    elif(selectColuna == "Curricular units 1st sem (enrolled)"):
        st.write("Histograma de alunos por Unidades curriculares 1º semestre (matriculado)")
        fig, ax2 = plt.subplots()
        ax2.hist(dataGraduate[selectColuna], rwidth=0.5)
        plt.xticks(range(23))

        st.pyplot(fig)

    # Seleção de histograma das Unidades curriculares 1º semestre (avaliações)
    elif(selectColuna == "Curricular units 1st sem (evaluations)"):
        st.write("Histograma de alunos por Unidades curriculares 1º semestre (avaliações)")
        fig, ax2 = plt.subplots()
        ax2.hist(dataGraduate[selectColuna], rwidth=0.8)
        plt.xticks(range(8))

        st.pyplot(fig)

    # Seleção de histograma das Unidades curriculares 1º semestre (aprovado)
    elif(selectColuna == "Curricular units 1st sem (approved)"):
        st.write("Histograma de alunos por Unidades curriculares 1º semestre (aprovado)")
        fig, ax2 = plt.subplots()
        ax2.hist(dataGraduate[selectColuna], rwidth=0.2)
        plt.xticks(range(35))

        st.pyplot(fig)

    # Seleção de histograma das Unidades curriculares 1º semestre (Nota)
    elif(selectColuna == "Curricular units 1st sem (grade)"):
        st.write("Histograma de alunos por Unidades curriculares 1º semestre (Nota)")
        fig, ax2 = plt.subplots()
        ax2.hist(dataGraduate[selectColuna], rwidth=0.8)
        plt.xticks(range(8))

        st.pyplot(fig)

    # Seleção de histograma das Unidades curriculares 1º semestre (sem avaliações)
    elif(selectColuna == "Curricular units 1st sem (without evaluations)"):
        st.write("Histograma de alunos por Unidades curriculares 1º semestre (sem avaliações)")
        fig, ax2 = plt.subplots()
        ax2.hist(dataGraduate[selectColuna], rwidth=0.7)
        plt.xticks(range(11))

        st.pyplot(fig)

    # Seleção de histograma das Unidades curriculares 2º semestre (creditadas)
    elif(selectColuna == "Curricular units 2nd sem (credited)"):
        st.write("Histograma de alunos por Unidades curriculares 2º semestre (creditadas)")
        fig, ax2 = plt.subplots()
        ax2.hist(dataGraduate[selectColuna], rwidth=0.4)
        plt.xticks(range(21))

        st.pyplot(fig)

    # Seleção de histograma das Unidades curriculares 2º semestre (matriculado)
    elif(selectColuna == "Curricular units 2nd sem (enrolled)"):
        st.write("Histograma de alunos por Unidades curriculares 2º semestre (matriculado)")
        fig, ax2 = plt.subplots()
        ax2.hist(dataGraduate[selectColuna], rwidth=0.3)
        plt.xticks(range(23))

        st.pyplot(fig)

    # Seleção de histograma das Unidades curriculares 2º semestre (avaliações)
    elif(selectColuna == "Curricular units 2nd sem (evaluations)"):
        st.write("Histograma de alunos por Unidades curriculares 2º semestre (avaliações)")
        fig, ax2 = plt.subplots()
        ax2.hist(dataGraduate[selectColuna], rwidth=0.8)
        plt.xticks(range(8))

        st.pyplot(fig)

    # Seleção de histograma das Unidades curriculares 2º semestre (aprovado)
    elif(selectColuna == "Curricular units 2nd sem (approved)"):
        st.write("Histograma de alunos por Unidades curriculares 2º semestre (aprovado)")
        fig, ax2 = plt.subplots()
        ax2.hist(dataGraduate[selectColuna], rwidth=0.2)
        plt.xticks(range(35))

        st.pyplot(fig)

    # Seleção de histograma das Unidades curriculares 2º semestre (Nota)
    elif(selectColuna == "Curricular units 2nd sem (grade)"):
        st.write("Histograma de alunos por Unidades curriculares 2º semestre (Nota)")
        fig, ax2 = plt.subplots()
        ax2.hist(dataGraduate[selectColuna], rwidth=0.8)
        plt.xticks(range(8))

        st.pyplot(fig)

    # Seleção de histograma das Unidades curriculares 2º semestre (sem avaliações)
    elif(selectColuna == "Curricular units 2nd sem (without evaluations)"):
        st.write("Histograma de alunos por Unidades curriculares 2º semestre (sem avaliações)")
        fig, ax2 = plt.subplots()
        ax2.hist(dataGraduate[selectColuna], rwidth=0.7)
        plt.xticks(range(11))

        st.pyplot(fig)

    # Seleção de histograma do taxa de desemprego
    elif(selectColuna == "Unemployment rate"):
        st.write("Histograma de alunos por taxa de desemprego")
        fig, ax2 = plt.subplots()
        ax2.hist(dataGraduate[selectColuna], rwidth=0.8)
        plt.xticks(range(8))

        st.pyplot(fig)

    # Seleção de histograma do taxa de inflação
    elif(selectColuna == "Inflation rate"):
        st.write("Histograma de alunos por taxa de inflação")
        fig, ax2 = plt.subplots()
        ax2.hist(dataGraduate[selectColuna], rwidth=1)
        # plt.xticks(range(9))

        st.pyplot(fig)

    # Seleção de histograma do GPD
    elif(selectColuna == "GDP"):
        st.write("Histograma de alunos por GPD")
        fig, ax2 = plt.subplots()
        ax2.hist(dataGraduate[selectColuna], rwidth=0.8)
        plt.xticks(range(8))

        st.pyplot(fig)

# Base apensa com os alunos Desistentes
elif(baseSelecionada == 'Abandonos'):
    st.title("Dados dos estudantes Universitarios que abandonaram")
    dataDropout = dataBase.query("Target == 'Dropout'")
    st.dataframe(dataDropout)

    selectColuna = st.selectbox("Escolha a coluna a ser exibida", ["", "Marital status", "Application mode", "Application order", "Course", "Daytime/evening attendance", "Previous qualification", "Nacionality", "Mother's qualification", "Father's qualification", "Displaced", "Educational special needs", "Debtor", "Tuition fees up to date", "Gender", "Scholarship holder", "Age at enrollment", "International", "Curricular units 1st sem (credited)", "Curricular units 1st sem (enrolled)", "Curricular units 1st sem (evaluations)", "Curricular units 1st sem (approved)", "Curricular units 1st sem (grade)", "Curricular units 1st sem (without evaluations)", "Curricular units 2nd sem (credited)", "Curricular units 2nd sem (enrolled)", "Curricular units 2nd sem (evaluations)", "Curricular units 2nd sem (approved)", "Curricular units 2nd sem (grade)", "Curricular units 2nd sem (without evaluations)", "Unemployment rate", "Inflation rate", "GDP"])
    # Seleção de histograma vazio
    if(selectColuna == ""):
        print(".1")
    
    # Seleção de histograma do Aplicação
    elif(selectColuna == "Marital status"):
        st.write("Histograma de alunos por Aplicação")
        fig, ax2 = plt.subplots()
        ax2.hist(dataDropout[selectColuna], rwidth=0.8)
        plt.xticks(range(8))

        st.pyplot(fig)
    
    # Seleção de histograma do Forma de Aplicação
    elif(selectColuna == "Application mode"):
        st.write("Histograma de alunos por Aplicação")
        fig, ax2 = plt.subplots()
        ax2.hist(dataDropout[selectColuna], bins= 18, range=[1,18], rwidth=0.9)
        plt.xticks(range(19))

        st.pyplot(fig)

    # Seleção de histograma do Ordem de Aplicação
    elif(selectColuna == "Application order"):
        st.write("Histograma de alunos por Ordem de aplicação")
        fig, ax2 = plt.subplots()
        ax2.hist(dataDropout[selectColuna], range=[1,8], rwidth=0.8)
        # plt.xticks(range(8))

        st.pyplot(fig)

    # Seleção de histograma do Curso
    elif(selectColuna == "Course"):
        st.write("")
        st.write("Histograma de alunos divididos por curso")
        fig, ax2 = plt.subplots()
        ax2.hist(dataDropout[selectColuna], bins = 17)
        plt.xticks(range(17))

        st.pyplot(fig)

    # Seleção de histograma do horario de aulas
    elif(selectColuna == "Daytime/evening attendance"):
        st.write("Histograma de alunos por Horario das aulas")
        fig, ax2 = plt.subplots()
        ax2.hist(dataDropout[selectColuna], rwidth=0.8)
        plt.xticks(range(2))

        st.pyplot(fig)

    # Seleção de histograma do qualificação previa
    elif(selectColuna == "Previous qualification"):
        st.write("Histograma de alunos por qualificação previa")
        fig, ax2 = plt.subplots()
        ax2.hist(dataDropout[selectColuna], rwidth=0.5)
        plt.xticks(range(18))

        st.pyplot(fig)

    # Seleção de histograma do Nacionalidade
    elif(selectColuna == "Nacionality"):
        st.write("Histograma de alunos por Nacionalidade")
        fig, ax2 = plt.subplots()
        ax2.hist(dataDropout[selectColuna], rwidth=0.2)
        plt.xticks(range(21))

        st.pyplot(fig)
    
    # Seleção de histograma do qualificações da mãe
    elif(selectColuna == "Mother's qualification"):
        st.write("Histograma de alunos por Qualificações da mãe")
        fig, ax2 = plt.subplots()
        ax2.hist(dataDropout[selectColuna], rwidth=0.3)
        plt.xticks(range(30))

        st.pyplot(fig)
    
    # Seleção de histograma do qualificações do pai
    elif(selectColuna == "Fathe's qualification"):
        st.write("Histograma de alunos por Qualificações da pai")
        fig, ax2 = plt.subplots()
        ax2.hist(dataDropout[selectColuna], rwidth=0.3)
        plt.xticks(range(30))

        st.pyplot(fig)
    
    # Seleção de histograma do Deslocado
    elif(selectColuna == "Displaced"):
        st.write("Histograma de alunos por Deslocado")
        fig, ax2 = plt.subplots()
        ax2.hist(dataDropout[selectColuna], rwidth=0.8)
        plt.xticks(range(2))

        st.pyplot(fig)
    
    # Seleção de histograma do Necessidades educacionais especiais
    elif(selectColuna == "Educational special needs"):
        st.write("Histograma de alunos por necessidades educacionais especiais")
        fig, ax2 = plt.subplots()
        ax2.hist(dataDropout[selectColuna], rwidth=0.8)
        plt.xticks(range(2))

        st.pyplot(fig)

    # Seleção de histograma do Devedor
    elif(selectColuna == "Debtor"):
        st.write("Histograma de alunos por Devedor")
        fig, ax2 = plt.subplots()
        ax2.hist(dataDropout[selectColuna], rwidth=0.8)
        plt.xticks(range(2))

        st.pyplot(fig)

    # Seleção de histograma do Mensalidades em dia
    elif(selectColuna == "Tuition fees up to date"):
        st.write("Histograma de alunos por Mensalidade em dia")
        fig, ax2 = plt.subplots()
        ax2.hist(dataDropout[selectColuna], rwidth=0.8)
        plt.xticks(range(2))

        st.pyplot(fig)

    # Seleção de histograma por Generos
    elif(selectColuna == "Gender"):
        st.write("Histograma de alunos por Genero")
        fig, ax2 = plt.subplots()
        ax2.hist(dataDropout[selectColuna], rwidth=0.8)
        plt.xticks(range(2))

        st.pyplot(fig)

    # Seleção de histograma por Bolsistas
    elif(selectColuna == "Scholarship holder"):
        st.write("Histograma de alunos por Bolsistas")
        fig, ax2 = plt.subplots()
        ax2.hist(dataDropout[selectColuna], rwidth=0.8)
        plt.xticks(range(2))

        st.pyplot(fig)

    # Seleção de histograma por Idade na Inscrição
    elif(selectColuna == "Age at enrollment"):
        st.write("Histograma de alunos por Idade na Inscrição")
        fig, ax2 = plt.subplots()
        ax2.hist(dataDropout[selectColuna], rwidth=0.8)
        plt.xticks(range(46))

        st.pyplot(fig)

    # Seleção de histograma pelo campo Internacional
    elif(selectColuna == "International"):
        st.write("Histograma de alunos por Internacional")
        fig, ax2 = plt.subplots()
        ax2.hist(dataDropout[selectColuna], rwidth=0.8)
        plt.xticks(range(2))

        st.pyplot(fig)

    # Seleção de histograma das Unidades curriculares 1º semestre (creditadas)
    elif(selectColuna == "Curricular units 1st sem (credited)"):
        st.write("Histograma de alunos por Unidades curriculares 1º semestre (creditadas)")
        fig, ax2 = plt.subplots()
        ax2.hist(dataDropout[selectColuna], rwidth=0.5)
        plt.xticks(range(21))

        st.pyplot(fig)

    # Seleção de histograma das Unidades curriculares 1º semestre (matriculado)
    elif(selectColuna == "Curricular units 1st sem (enrolled)"):
        st.write("Histograma de alunos por Unidades curriculares 1º semestre (matriculado)")
        fig, ax2 = plt.subplots()
        ax2.hist(dataDropout[selectColuna], rwidth=0.5)
        plt.xticks(range(23))

        st.pyplot(fig)

    # Seleção de histograma das Unidades curriculares 1º semestre (avaliações)
    elif(selectColuna == "Curricular units 1st sem (evaluations)"):
        st.write("Histograma de alunos por Unidades curriculares 1º semestre (avaliações)")
        fig, ax2 = plt.subplots()
        ax2.hist(dataDropout[selectColuna], rwidth=0.8)
        plt.xticks(range(8))

        st.pyplot(fig)

    # Seleção de histograma das Unidades curriculares 1º semestre (aprovado)
    elif(selectColuna == "Curricular units 1st sem (approved)"):
        st.write("Histograma de alunos por Unidades curriculares 1º semestre (aprovado)")
        fig, ax2 = plt.subplots()
        ax2.hist(dataDropout[selectColuna], rwidth=0.2)
        plt.xticks(range(35))

        st.pyplot(fig)

    # Seleção de histograma das Unidades curriculares 1º semestre (Nota)
    elif(selectColuna == "Curricular units 1st sem (grade)"):
        st.write("Histograma de alunos por Unidades curriculares 1º semestre (Nota)")
        fig, ax2 = plt.subplots()
        ax2.hist(dataDropout[selectColuna], rwidth=0.8)
        plt.xticks(range(8))

        st.pyplot(fig)

    # Seleção de histograma das Unidades curriculares 1º semestre (sem avaliações)
    elif(selectColuna == "Curricular units 1st sem (without evaluations)"):
        st.write("Histograma de alunos por Unidades curriculares 1º semestre (sem avaliações)")
        fig, ax2 = plt.subplots()
        ax2.hist(dataDropout[selectColuna], rwidth=0.7)
        plt.xticks(range(11))

        st.pyplot(fig)

    # Seleção de histograma das Unidades curriculares 2º semestre (creditadas)
    elif(selectColuna == "Curricular units 2nd sem (credited)"):
        st.write("Histograma de alunos por Unidades curriculares 2º semestre (creditadas)")
        fig, ax2 = plt.subplots()
        ax2.hist(dataDropout[selectColuna], rwidth=0.4)
        plt.xticks(range(21))

        st.pyplot(fig)

    # Seleção de histograma das Unidades curriculares 2º semestre (matriculado)
    elif(selectColuna == "Curricular units 2nd sem (enrolled)"):
        st.write("Histograma de alunos por Unidades curriculares 2º semestre (matriculado)")
        fig, ax2 = plt.subplots()
        ax2.hist(dataDropout[selectColuna], rwidth=0.3)
        plt.xticks(range(23))

        st.pyplot(fig)

    # Seleção de histograma das Unidades curriculares 2º semestre (avaliações)
    elif(selectColuna == "Curricular units 2nd sem (evaluations)"):
        st.write("Histograma de alunos por Unidades curriculares 2º semestre (avaliações)")
        fig, ax2 = plt.subplots()
        ax2.hist(dataDropout[selectColuna], rwidth=0.8)
        plt.xticks(range(8))

        st.pyplot(fig)

    # Seleção de histograma das Unidades curriculares 2º semestre (aprovado)
    elif(selectColuna == "Curricular units 2nd sem (approved)"):
        st.write("Histograma de alunos por Unidades curriculares 2º semestre (aprovado)")
        fig, ax2 = plt.subplots()
        ax2.hist(dataDropout[selectColuna], rwidth=0.2)
        plt.xticks(range(35))

        st.pyplot(fig)

    # Seleção de histograma das Unidades curriculares 2º semestre (Nota)
    elif(selectColuna == "Curricular units 2nd sem (grade)"):
        st.write("Histograma de alunos por Unidades curriculares 2º semestre (Nota)")
        fig, ax2 = plt.subplots()
        ax2.hist(dataDropout[selectColuna], rwidth=0.8)
        plt.xticks(range(8))

        st.pyplot(fig)

    # Seleção de histograma das Unidades curriculares 2º semestre (sem avaliações)
    elif(selectColuna == "Curricular units 2nd sem (without evaluations)"):
        st.write("Histograma de alunos por Unidades curriculares 2º semestre (sem avaliações)")
        fig, ax2 = plt.subplots()
        ax2.hist(dataDropout[selectColuna], rwidth=0.7)
        plt.xticks(range(11))

        st.pyplot(fig)

    # Seleção de histograma do taxa de desemprego
    elif(selectColuna == "Unemployment rate"):
        st.write("Histograma de alunos por taxa de desemprego")
        fig, ax2 = plt.subplots()
        ax2.hist(dataDropout[selectColuna], rwidth=0.8)
        plt.xticks(range(8))

        st.pyplot(fig)

    # Seleção de histograma do taxa de inflação
    elif(selectColuna == "Inflation rate"):
        st.write("Histograma de alunos por taxa de inflação")
        fig, ax2 = plt.subplots()
        ax2.hist(dataDropout[selectColuna], rwidth=1)
        # plt.xticks(range(9))

        st.pyplot(fig)

    # Seleção de histograma do GPD
    elif(selectColuna == "GDP"):
        st.write("Histograma de alunos por GPD")
        fig, ax2 = plt.subplots()
        ax2.hist(dataDropout[selectColuna], rwidth=0.8)
        plt.xticks(range(8))

        st.pyplot(fig)

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
elif(legenda == "Mother's and Father's qualification"):
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

elif(legenda == "Mother's and Father's occupation"):
    st.sidebar.write("1 - 0 - Estudante")
    st.sidebar.write("2 - 1º - Representantes do Poder Legislativo e dos Órgãos Executivos, Diretores, Diretores e Gerentes Executivos")
    st.sidebar.write("3 - 2 - Especialistas em Atividades Intelectuais e Científicas")
    st.sidebar.write("4 - 3 - Técnicos e Profissões de Nível Intermediário")
    st.sidebar.write("5 - 4 – Pessoal administrativo")
    st.sidebar.write("6 - 5 - Serviços Pessoais, Trabalhadores e Vendedores de Segurança e Proteção")
    st.sidebar.write("7 - 6 - Agricultores e trabalhadores qualificados na agricultura, pesca e silvicultura")
    st.sidebar.write("8 - 7 - Trabalhadores qualificados na indústria, construção e artesãos")
    st.sidebar.write("9 - 8 - Operadores de Instalação e Máquinas e Trabalhadores de Montagem")
    st.sidebar.write("10 - 9 – Trabalhadores não qualificados")
    st.sidebar.write("11 - 10 - Profissões das Forças Armadas")
    st.sidebar.write("12 - 90 - Outra Situação")
    st.sidebar.write("13 - 99 - (em branco)")
    st.sidebar.write("14 - 122 - Profissionais de saúde")
    st.sidebar.write("15 - 123 - professores")
    st.sidebar.write("16 - 125 - Especialistas em tecnologias de informação e comunicação (TIC)")
    st.sidebar.write("17 - 131 - Técnicos e profissões de ciência e engenharia de nível intermediário")
    st.sidebar.write("18 - 132 - Técnicos e profissionais, de nível intermédio de saúde 134 - Técnicos de nível intermédio dos serviços jurídicos, sociais, desportivos, culturais e similares")
    st.sidebar.write("19 - 141 - Trabalhadores de escritório, secretárias em geral e operadores de processamento de dados")
    st.sidebar.write("20 - 143 - Operadores de dados, contabilidade, estatística, serviços financeiros e operadores relacionados a registros")
    st.sidebar.write("21 - 144 - Outro pessoal de apoio administrativo")
    st.sidebar.write("22 - 151 - trabalhadores de serviços pessoais")
    st.sidebar.write("23 - 152 - vendedores")
    st.sidebar.write("24 - 153 - Profissionais de cuidados pessoais e similares")
    st.sidebar.write("25 - 171 - Trabalhadores qualificados da construção civil e similares, exceto eletricistas")
    st.sidebar.write("26 - 173 - Trabalhadores qualificados em impressão, fabricação de instrumentos de precisão, joalheiros, artesãos e similares")
    st.sidebar.write("27 - 175 - Trabalhadores de processamento de alimentos, marcenaria, vestuário e outras indústrias e artesanato")
    st.sidebar.write("28 - 191 - trabalhadores de limpeza")
    st.sidebar.write("29 - 192 - Trabalhadores não qualificados na agricultura, produção animal, pesca e silvicultura")
    st.sidebar.write("30 - 193 - Trabalhadores não qualificados na indústria extractiva, construção, indústria transformadora e transportes")
    st.sidebar.write("31 - 194 - Auxiliares de preparação de refeições")

elif(legenda == "Gender"):
    st.sidebar.write("0 - Feminino")
    st.sidebar.write("1 - Masculino")

elif(legenda == "Application mode"):
    st.sidebar.write("1 – 1ª fase – contingente geral")
    st.sidebar.write("2 – Portaria nº 612/93")
    st.sidebar.write("3 - 1ª fase - contingente especial (Ilha dos Açores)")
    st.sidebar.write("4 - Titulares de outros cursos superiores")
    st.sidebar.write("5 - Portaria nº 854-B/99")
    st.sidebar.write("6 - Estudante internacional (bacharelado)")
    st.sidebar.write("7 – 1ª fase – contingente especial (Ilha da Madeira)")
    st.sidebar.write("8 – 2ª fase – contingente geral")
    st.sidebar.write("9 – 3ª fase – contingente geral")
    st.sidebar.write("10 - Portaria n.º 533-A/99, alínea b2) (Plano Diferente)")
    st.sidebar.write("11 - Portaria nº 533-A/99, item b3 (Outra Instituição)")
    st.sidebar.write("12 - Maiores de 23 anos 42 - Transferência")
    st.sidebar.write("13 – Mudança de rumo")
    st.sidebar.write("14 - Titulares de diploma de especialização tecnológica")
    st.sidebar.write("15 - Mudança de instituição/curso")
    st.sidebar.write("16 - Titulares de diplomas de ciclo curto")
    st.sidebar.write("17 - Mudança de instituição/curso (Internacional)")