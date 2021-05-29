import pandas as pd
import numpy as np
import streamlit as st
import requests
from streamlit_lottie import st_lottie


st.set_page_config(layout="wide")


def load_lottieurl(url: str):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()


lottie_linkedin = load_lottieurl(
    "https://assets9.lottiefiles.com/packages/lf20_yNYxCH.json"
)
st_lottie(lottie_linkedin, speed=1, height=200, key="initial")

# introduction
row0_1, row0_spacer, row0_2 = st.beta_columns((2, 0.4, 1))
row0_1.title("Analzying LinkedIn Connections")
row0_2.write("")
row0_2.subheader("📱 by [Okkar Min](https://okkarm.in)")

# explanation
"Hey hey 👋 , talk about the explanation here"

# .csv uploader
st.file_uploader("Your Connections.csv")
