import streamlit as st

# ----------------------------
# CONFIGURACIÓN INICIAL
# ----------------------------
st.set_page_config(page_title="Batería de Tomás", layout="centered")

if "energia" not in st.session_state:
    st.session_state.energia = 60

energia = st.session_state.energia

# ----------------------------
# DEFINIR COLOR Y EFECTOS
# ----------------------------
if energia >= 100:
    color = "#00E676"  # Verde brillante
    efecto = "max"
elif energia > 70:
    color = "#4CAF50"
    efecto = "normal"
elif energia > 30:
    color = "#FFC107"
    efecto = "normal"
else:
    color = "#F44336"
    efecto = "low"

# ----------------------------
# ESTILOS Y ANIMACIONES
# ----------------------------
st.markdown(f"""
<style>

@keyframes pulse {{
  0% {{ box-shadow: 0 0 10px #00E676; }}
  50% {{ box-shadow: 0 0 40px #00E676; }}
  100% {{ box-shadow: 0 0 10px #00E676; }}
}}

@keyframes shake {{
  0% {{ transform: translateX(0); }}
  25% {{ transform: translateX(-5px); }}
  50% {{ transform: translateX(5px); }}
  75% {{ transform: translateX(-5px); }}
  100% {{ transform: translateX(0); }}
}}

.battery-container {{
    display:flex;
    justify-content:center;
    margin-top:40px;
}}

.battery {{
    width:350px;
    height:140px;
    border:8px solid #333;
    border-radius:25px;
    position:relative;
    background-color:white;
}}

.level {{
    width:{energia}%;
    height:100%;
    background-color:{color};
    border-radius:15px;
    transition: width 0.6s ease-in-out;
    {"animation: pulse 1.5s infinite;" if efecto=="max" else ""}
}}

.low {{
    {"animation: shake 0.4s;" if efecto=="low" else ""}
}}

.tip {{
    width:25px;
    height:70px;
    background-color:#333;
    margin-left:6px;
    margin-top:35px;
    border-radius:5px;
}}

</style>

<div class="battery-container">
    <div class="battery {'low' if efecto=='low' else ''}">
        <div class="level"></div>
    </div>
    <div class="tip"></div>
</div>

<h1 style="text-align:center; margin-top:25px; font-size:52px;">
    {energia}%
</h1>
""", unsafe_allow_html=True)

# ----------------------------
# MENSAJES GAMER
# ----------------------------
if energia < 30:
    st.warning("⚠️ ENERGÍA CRÍTICA - Necesitas combustible.")
elif energia < 70:
    st.info("⚡ Energía estable. Puedes mejorarla.")
elif energia < 100:
    st.success("🔥 Muy buena energía. ¡Sigue así!")
else:
    st.success("🚀 MAX POWER ACTIVADO 🚀")

# ----------------------------
# BOTONES DE ALIMENTACIÓN
# ----------------------------
st.divider()
st.subheader("🍽️ Alimentar a Tomás")

col1, col2, col3 = st.columns(3)

with col1:
    if st.button("🥄 Poco (+10%)"):
        st.session_state.energia = min(100, energia + 10)

with col2:
    if st.button("🍛 Normal (+20%)"):
        st.session_state.energia = min(100, energia + 20)

with col3:
    if st.button("🍕 Todo (+35%)"):
        st.session_state.energia = min(100, energia + 35)

# ----------------------------
# GASTO DE ENERGÍA
# ----------------------------
st.divider()

if st.button("⏳ Pasó tiempo (-15%)"):
    st.session_state.energia = max(0, energia - 15)

# Reset opcional
if st.button("🔄 Reiniciar energía"):
    st.session_state.energia = 60
