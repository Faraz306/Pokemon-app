import streamlit as st
from PIL import Image

st.title("Yamaan_faraz's cool app.")
st.write("which pokemon do you like?")

if 'clicked' not in st.session_state:
    st.session_state.clicked = False

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.image("avatar.png", width=100)
    if st.button("Psyduck"):
        st.info("""Information about Psyduck...
        A Stupid pokemon. powerfullest attack: confuse attack. type - water
        """)
        st.session_state.clicked = True

with col2:
    st.image("pikachu.png", width=100)
    if st.button("Pikachu"):
        st.info("""Information about Pikachu...
        Most rarest pokemon. type - electric. powerfullest attack: thunderbolt
        """)
        st.session_state.clicked = True

with col3:
    st.image("game.png", width=100)
    if st.button("Bulbasaur"):
        st.info("""Information about Bulbasaur...
        type - grass . powerfullest attack: solar beam
        """)
        st.session_state.clicked = True

with col4:
    st.image("charizard.png", width=100)
    if st.button("Charizard"):
        st.info("""Information about Charizard...
        type - fire. powerfullest attack: fire
        """)
        st.session_state.clicked = True

# Show success message if any button was clicked
if st.session_state.clicked:
    st.success("Thanks for visiting! for more information, please go to contact us.")