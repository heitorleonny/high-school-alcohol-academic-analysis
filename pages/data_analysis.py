import streamlit as st
import pandas as pd
from home import load_data
import matplotlib.pyplot as plt




def main():
    st.title("Análise Exploratória")

    data = load_data()

    st.table(data.describe())
    st.table(data.head())

    st.set_option('deprecation.showPyplotGlobalUse', False)
    data['idade'].hist()
    plt.title('Histograma da Coluna idade')
    plt.xlabel('Valores')
    plt.ylabel('Frequência')
    plt.show()
    st.pyplot()
    

if __name__ == '__main__':
    main()
