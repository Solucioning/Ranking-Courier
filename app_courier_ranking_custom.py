
import streamlit as st
import pandas as pd

st.set_page_config(
    page_title="Ranking de Couriers",
    page_icon="🚴‍♂️",
    layout="centered",
    initial_sidebar_state="collapsed"
)

# Mostrar logo
st.image("Captura de pantalla 2025-04-16 103817.png", width=200)

st.title("Consulta tu Ranking - Solucioning Delivery")

@st.cache_data
def load_data():
    df = pd.read_excel("Ranking_Couriers_Semanal.xlsx")
    return df

df = load_data()

courier_id = st.text_input("Introduce tu ID de Courier:", "")

if courier_id:
    resultados = df[df['IDCourier'].astype(str) == courier_id]
    if not resultados.empty:
        st.success(f"Resultados encontrados para IDCourier: {courier_id}")
        st.dataframe(resultados[[
            'Semana', 'Ciudad', 'Vehicle', 'Eficiencia', 'CDT', 'Speed',
            'No show', 'CAPU', 'Reassignament', 'Score_total',
            'Ranking_posicion', 'Incentivo_semanal', 'Reto_mensual'
        ]].sort_values(by='Semana', ascending=False))
    else:
        st.warning("No se encontraron resultados para ese ID.")
else:
    st.info("Introduce un ID para consultar tu rendimiento.")

# Ocultar el menú y footer de Streamlit
hide_streamlit_style = """
    <style>
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    </style>
"""
st.markdown(hide_streamlit_style, unsafe_allow_html=True)
