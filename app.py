import streamlit as st
import pandas as pd

# Configuração Visual
st.set_page_config(page_title="Neurofood - Controle de Gelo", page_icon="❄️")

st.markdown("""
    <style>
    .main { background-color: #000000; }
    h1 { color: #00FF00; text-align: center; border: 2px solid #00FF00; padding: 10px; border-radius: 10px; font-family: monospace; }
    div[data-testid="stMetricValue"] { color: #00FF00 !important; }
    label { color: #00FF00 !important; font-weight: bold !important; }
    </style>
    """, unsafe_allow_html=True)

st.markdown("<h1>NEUROFOOD - CONTROLE DO GELO</h1>", unsafe_allow_html=True)

# Entradas na Barra Lateral
st.sidebar.header("⚙️ PARÂMETROS")
vol = st.sidebar.slider("Volume da Água (L)", 50, 1000, 250)
t_torn = st.sidebar.slider("Temp. Torneira (°C)", 15, 35, 24)
t_alvo = st.sidebar.slider("Temp. Alvo (°C)", 2, 18, 10)
t_amb = st.sidebar.slider("Temp. Ambiente (°C)", 15, 45, 28)
atlet = st.sidebar.number_input("Nº de Atletas", 0, 10, 2)
inter = st.sidebar.selectbox("Intervalo Recarga (min)", [5, 10, 15, 20, 30], index=2)

# Física
C_AGUA, L_FUSAO, K_AR, TERMOGENESE = 4.186, 334.0, 0.0007, 15.0

# Cálculos
gelo_ini = (vol * C_AGUA * (t_torn - t_alvo)) / L_FUSAO
q_manut = (vol * C_AGUA * (t_amb - t_alvo) * K_AR) + (atlet * TERMOGENESE)
gelo_rec = (q_manut / L_FUSAO) * inter

# Dash
c1, c2 = st.columns(2)
c1.metric("GELO INICIAL", f"{gelo_ini:.2f} kg")
c2.metric(f"RECARGA ({inter} min)", f"{gelo_rec:.2f} kg")

# Tabela
st.subheader("📋 CRONOGRAMA")
dados = [{"Min": m, "Ação": "CARGA INICIAL" if m==0 else f"Reposição {m//inter}", "Qtd": f"{gelo_ini:.1f}kg" if m==0 else f"{gelo_rec:.2f}kg"} for m in range(0, 61, inter)]
st.table(pd.DataFrame(dados))
