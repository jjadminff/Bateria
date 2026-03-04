import streamlit as st

# Inicializar batería en sesión
if "energia" not in st.session_state:
    st.session_state.energia = 60

st.title("🔋 La Batería Interna de Tomás")

# Mostrar batería
st.progress(st.session_state.energia)
st.write(f"Energía actual: {st.session_state.energia}%")

st.divider()

st.subheader("🍽️ Alimentar a Tomás")

col1, col2, col3 = st.columns(3)

with col1:
    if st.button("🥄 Comió poco (+10%)"):
        st.session_state.energia += 10

with col2:
    if st.button("🍛 Comió normal (+20%)"):
        st.session_state.energia += 20

with col3:
    if st.button("🍕 Comió todo (+35%)"):
        st.session_state.energia += 35

# Limitar a 100%
if st.session_state.energia > 100:
    st.session_state.energia = 100

# Mensajes motivacionales
st.divider()

if st.session_state.energia < 30:
    st.warning("⚠️ Energía baja. Necesitas combustible para seguir aprendiendo.")
elif st.session_state.energia < 70:
    st.info("🙂 Energía media. Puedes mejorar un poco más.")
else:
    st.success("🚀 ¡Energía al máximo! Listo para jugar y aprender.")

# Botón para simular gasto de energía
if st.button("⏳ Pasó tiempo (gastar energía -15%)"):
    st.session_state.energia -= 15
    if st.session_state.energia < 0:
        st.session_state.energia = 0
