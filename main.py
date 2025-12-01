import streamlit as st
from PIL import Image

st.title("Yamaan_faraz's Pokemon app.")
st.write("which pokemon do you like?")

if 'clicked' not in st.session_state:
    st.session_state.clicked = False


col1, col2, col3, col4, col5= st.columns(5)

with col1:
    st.image("avatar.png", width=100)
    if st.button("Psyduck"):
        st.info("""Information about Psyduck...
        A Stupid pokemon. powerfullest attack: Psychic attack. type - water
        """)
        st.session_state.clicked = True

with col2:
    st.image("pikachu.png", width=100)
    if st.button("Pikachu"):
        st.info("""Information about Pikachu...
        Most iconic pokemon. type - electric. powerfullest attack: thunderbolt
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
        type - fire. powerfullest attack: fire blast
        """)
        st.session_state.clicked = True
with col5:
    st.image("arbok.png", width=100)
    if st.button("Arbok"):
        st.info("""Information about Arbok...
        type - snake . powerfullest attack: bite
        """)
        st.session_state.clicked = True

col6, col7, col8, col9, col10 = st.columns(5)
with col6:
    st.image("avatar (1).png", width=100)
    if st.button("Meowth"):
        st.info("""Information about Meowth...
        type - cat . powerfullest attack: scratch
        """)
        st.session_state.clicked = True
with col7:
    st.image("avatar (3).png", width=100)
    if st.button("Snorlax"):
        st.info("""Information about Snorlax...
        type - sleeping . powerfullest attack: None
        """)
        st.session_state.clicked = True
with col8:
    st.image("avatar (2).png", width=100)
    if st.button("Staryu"):
        st.info("""Information about Staryu...
        type - water . powerfullest attack: Bubble Beam
        """)
        st.session_state.clicked = True
with col9:
    st.image("jigglypuff.png", width=100)
    if st.button("Jigglypuff"):
        st.info("""Information about Jigglypuff...
        type - ballon . powerfullest attack: singing
        """)
        st.session_state.clicked = True
with col10:
    st.image("squirtle.png", width=100)
    if st.button("Squirtle"):
        st.info("""Information about Squirtle...
        type - water . powerfullest attack: Aqua Tail.
        """)
        st.session_state.clicked = True
col11, col12, col13, col14, col15 = st.columns(5)
with col11:
    st.image("avatar (5).png", width=100)
    if st.button("Ghast"):
        st.info("""Information about Ghast...
        type - ghost . powerfullest attack: fireball
        """)
        st.session_state.clicked = True
with col12:
    st.image("avatar (6).png", width=100)
    if st.button("Exeggutor"):
        st.info("""Information about Exeggutor...
        type - grass/Psychic . powerfullest attack: Psychic
        """)
        st.session_state.clicked = True
with col13:
    st.image("chicken.png", width=100)
    if st.button("Pidgeoto"):
        st.info("""Information about Pidgeoto...
        type - bird . powerfullest attack: Gust attack
        """)
        st.session_state.clicked = True
with col14:
    st.image("zubat.png", width=100)
    if st.button("Zubat"):
        st.info("""Information about Zubat...
        type - bat . powerfullest attack: bite
        """)
        st.session_state.clicked = True
with col15:
    st.image("avatar (4).png", width=100)
    if st.button("Muk"):
        st.info("""Information about Muk...
        type - poison . powerfullest attack: Gunk shot
        """)
if st.session_state.clicked:
    st.success("Thanks for visiting! for more information, please go to contact us.")
