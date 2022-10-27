import streamlit as st
import schedule
import time
from st_functions import st_button, load_css
from PIL import Image

load_css()

st.write("[![Star](https://img.shields.io/github/stars/dataprofessor/links.svg?logo=github&style=social)](https://gitHub.com/dataprofessor/links)")

col1, col2, col3 = st.columns(3)
col2.image(Image.open('dp.png'))

st.header('THE BIG GREEN')

st.info('Curating soulful music and adovcating for more sustainable nightlife.')

icon_size = 20

# Discord button

st_button('discord', 'https://discord.gg/xs83PBTcw2', 'Our Discord Community', icon_size)

# This function defines the schedule for the open deck link to drop.


def od_job():
    schedule.every().thursday.at("18:23").do(
            st_button('open_deck', 'https://docs.google.com/spreadsheets/d/17nO20xzAFPw7ulF7iJgfqj7Lem-u_yBB5ljWiwVBBsQ/edit#gid=0Q/edit#gid=0', 'PALMS DJ JAM OPEN DECKS SIGN UP - 5th October 2022', icon_size)
    )

while True:
    schedule.run_pending()
    time.sleep(1)


