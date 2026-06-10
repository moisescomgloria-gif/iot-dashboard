import pandas as pd 
import streamlit as st 

url = "https://script.google.com/macros/s/AKfycbyOE0R6LCZobNJmTsUzMZAn_vOsYxj631lsbeY1mc5UqGTGeVmr5ht4rMex48Ryz1MX/exec" 

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
