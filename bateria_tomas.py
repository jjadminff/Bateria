import streamlit as st

# ----------------------------
# CONFIGURACIÓN INICIAL
# ----------------------------
st.set_page_config(page_title="Batería de Tomás", layout="centered")

# Inicializar energía en sesión
if "energia" not in st.session_state:
    st.session_state.energia = 60

energia = st.session_state.energia

# ----------------------------
# DEFINIR COLOR SEGÚN NIVEL
# ----------------------------
if energia > 70:
    color = "#4CAF50"   # Verde
elif energia > 30:
    color = "#FFC107"   # Amarillo
else:
    color = "#F44336"   # Rojo

# ----------------------------
# BATERÍA GRANDE CENTRADA
# ----------------------------
st.markdown(f"""
<div style="display:flex; justify-content:center; margin-top:40px;">
    <div style="
        width:350px;
        height:140px;
        border:8px solid #333;
        border-radius:25px;
        position:relative;
        background-color:white;
    ">
        <div style="
            width:{energia}%;
            height:100%;
            background-color:{color};
            border-radius:15px;
            transition: width 0.6s ease-in-out;
        "></div>
    </div>
    <div style="
        width:25px;
        height:70px;
        background-color:#333;
        margin-left:6px;
        margin-top:35px;
        border-radius:5px;
    "></div>
</div>

<h1 style="text-align:center; margin-top:25px; font-size:48px;">
    {energia}%
</h1>
""", unsafe_allow_html=True)

# ----------------------------
# MENSAJES MOTIVACIONALES
# ----------------------------
if energia < 30:
    st.warning("⚠️ Energía baja. Necesitas combustible para seguir aprendiendo y jugando.")
elif energia < 70:
    st.info("🙂 Energía media. Un poco más de comida y estarás al máximo.")
else:
    st.success("🚀 ¡Energía al máximo! Listo para aprender y divertirse.")

# ----------------------------
# BOTONES DE ALIMENTACIÓN
# ----------------------------
st.divider()
st.subheader("🍽️ Alimentar a Tomás")

col1, col2, col3 = st.columns(3)

with col1:
    if st.button("🥄 Comió poco (+10%)"):
        st.session_state.energia = min(100, energia + 10)

with col2:
    if st.button("🍛 Comió normal (+20%)"):
        st.session_state.energia = min(100, energia + 20)

with col3:
    if st.button("🍕 Comió todo (+35%)"):
        st.session_state.energia = min(100, energia + 35)

# ----------------------------
# SIMULAR GASTO DE ENERGÍA
# ----------------------------
st.divider()

if st.button("⏳ Pasó tiempo (gastar energía -15%)"):
    st.session_state.energia = max(0, energia - 15)
