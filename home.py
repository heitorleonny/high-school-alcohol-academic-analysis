# app.py
import streamlit as st
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import linear_kernel


@st.cache_data
def load_data():
    data = pd.read_csv(r'data\lpor_classification.csv')
    return data



def main():
    st.title('Como o álcool pode influênciar no desempenho acadêmico?')

    st.markdown("""
A análise dos resultados acadêmicos de alunos que consomem álcool desempenha um papel crucial na compreensão do impacto dessa prática no desempenho escolar. Essa investigação oferece insights valiosos para educadores, pesquisadores e profissionais de saúde, ajudando a identificar possíveis correlações entre o consumo de álcool e o desempenho acadêmico.

Através da análise meticulosa de dados, é possível identificar padrões e tendências que podem fornecer uma compreensão mais profunda sobre como o consumo de álcool pode afetar a frequência escolar, a participação em atividades extracurriculares e o desempenho em exames. Além disso, essa análise pode destacar possíveis fatores de risco ou de proteção associados ao consumo de álcool, permitindo a implementação de estratégias preventivas e de apoio.

Ao entender a relação entre o consumo de álcool e o desempenho acadêmico, as instituições de ensino podem desenvolver políticas educacionais mais eficazes e programas de intervenção direcionados. Isso não apenas visa melhorar o rendimento dos alunos, mas também promove um ambiente escolar mais saudável e seguro.""")

    data = load_data()



if __name__ == '__main__':
    main()
