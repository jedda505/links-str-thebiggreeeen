import streamlit as st
from st_functions import st_button, load_css
from PIL import Image

load_css()

st.write("[![Star](https://img.shields.io/github/stars/dataprofessor/links.svg?logo=github&style=social)](https://gitHub.com/dataprofessor/links)")

col1, col2, col3 = st.columns(3)
col2.image(Image.open('dp.png'))

st.header('The Big Green')

st.info('Soulful music and more sustainable nightlife.')

icon_size = 20

st_button('discord', 'https://discord.gg/xs83PBTcw2', 'Our Discord Community', icon_size)
st_button('open_deck', 'https://docs.google.com/spreadsheets/d/17nO20xzAFPw7ulF7iJgfqj7Lem-u_yBB5ljWiwVBBsQ/edit#gid=0Q/edit#gid=0', 'PALMS DJ JAM OPEN DECKS SIGN UP - 5th October 2022', icon_size)

