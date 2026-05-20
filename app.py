import pandas as pd
import streamlit as st
url = "https://docs.google.com/spreadsheets/d/e/2PACX-1vQyq5nco8M2Uy--wETczHITKQaSTQ8Fbqzb7rsJ91yER8_Y5J9v0W_8qZFuwxaJZ6YUmKivhmKitV5_/pubhtml?gid=0&single=true"
# 1. Carrega os dados brutos
dados_brutos = pd.read_json(url)
# 2. Organiza colunas e linhas (Pega a 1ª linha como cabeçalho)
df = pd.DataFrame(dados_brutos.values[1:], columns=dados_brutos.values[0])
# 3. Formatação de Tipos (Datetime e Float)
df['timestamp'] = pd.to_datetime(df['timestamp'])
df['temperatura'] = df['temperatura'].astype(float)
df['umidade'] = df['umidade'].astype(float)
# 4. Interface Streamlit
st.title("Monitoramento IoT")
# Gráfico de linhas usando o timestamp como eixo X
st.subheader("Evolução Temporal")
st.line_chart(df.set_index('timestamp')[['temperatura', 'umidade']])
# Tabela de dados
st.subheader("Dados Brutos")
st.dataframe(df)
