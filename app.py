import utils
import streamlit as st
import requests
import pandas as pd
import numpy as np
import plotly.express as px
from streamlit_lottie import st_lottie
import streamlit_wordcloud as wordcloud
from PIL import Image


st.set_page_config(layout="wide")


def load_lottieurl(url: str):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()


lottie_linkedin = load_lottieurl(
    "https://assets9.lottiefiles.com/packages/lf20_yNYxCH.json"
)
# st_lottie(lottie_linkedin, speed=0.8, height=150, key="initial")

# introduction
row0_1, row0_spacer, row0_2 = st.beta_columns([2, 1, 1])
with row0_1:
    st.image(
        Image.open("./assets/linkedin_logo.png"),
        width=200,
    )
    "# Analyzing LinkedIn Connections"
row0_2.write("")
row0_2.write("")
with row0_2:
    "### 🛠 by [Okkar Min](https://okkarm.in)"

# explanation
"Hey hey 👋 , talk about the explanation here"

# .csv uploader
connections_csv = st.file_uploader("Your Connections.csv")
df = utils.remove_first_3_line(connections_csv)

total_connections = str(df.count()["First Name"])
unique_companies = str(df.nunique()["Company"])
unique_positions = str(df.nunique()["Position"])


# 3 column headers
row1_1, row1_2, row1_3 = st.beta_columns(3)

with row1_1:
    st.markdown(
        f"<h3 style='text-align: center;'>Total Connections</h3>",
        unsafe_allow_html=True,
    )
    st.markdown(
        f"<h2 style='text-align: center; font-weight: bold;'>{total_connections}</h2>",
        unsafe_allow_html=True,
    )
with row1_2:
    st.markdown(
        f"<h3 style='text-align: center;'>Companies</h3>",
        unsafe_allow_html=True,
    )
    st.markdown(
        f"<h2 style='text-align: center; font-weight: bold;'>{unique_companies}</h2>",
        unsafe_allow_html=True,
    )
with row1_3:
    st.markdown(
        f"<h3 style='text-align: center;'>Job Titles</h3>",
        unsafe_allow_html=True,
    )
    st.markdown(
        f"<h2 style='text-align: center; font-weight: bold;'>{unique_positions}</h2>",
        unsafe_allow_html=True,
    )

# 1 column chart
# group by 'Position'
pdf = df.groupby("Position").agg(["count"])
grouped_by_position = pdf["First Name"].sort_values(by=["count"], ascending=False)

# scatter plot
fig = px.scatter(
    grouped_by_position.head(50),
    y="count",
    labels={"count": "Head Count"},
    template="none",
)
fig.update_xaxes(tickangle=45)
st.plotly_chart(fig, use_container_width=True)

# plot explanation
top_job_title = grouped_by_position["count"].idxmax()
top_job_title_head_count = grouped_by_position["count"].max()
least_job_title = grouped_by_position["count"].idxmin()
least_job_title_head_count = grouped_by_position["count"].min()

f"You seem to be connected with alot of **{top_job_title}**, in fact \
**{top_job_title_head_count}** of them! Probably should connect more \
with **{least_job_title}** because there is only \
**{least_job_title_head_count}** in your network"

# 2 column charts
# row2_1, row_padding, row2_2 = st.beta_columns([2, 0.15, 2])
row2_1, row2_2 = st.beta_columns(2)

with row2_1:  # connections by company
    # group by 'Company'
    cdf = df.groupby("Company").agg(["count"])
    grouped_by_company = cdf["First Name"].sort_values(by=["count"], ascending=False)

    # bar chart
    fig = px.bar(
        grouped_by_company.head(10),
        y="count",
        labels={"count": "Pax"},
        template="none",
    )
    st.plotly_chart(fig, use_container_width=True)

    # chart explanation
    top_company = grouped_by_company["count"].idxmax()
    pax_in_top_company = grouped_by_company["count"].max()
    least_company = grouped_by_company["count"].idxmin()
    pax_in_least_company = grouped_by_company["count"].min()
    f"It appears that **{pax_in_top_company}** of your connections work at **{top_company}**,\
    and only **{pax_in_least_company}** is at **{least_company}**"

with row2_2:  # connections by date
    # change connected on text to datetime
    df["Connected On"] = pd.to_datetime(df["Connected On"], format="%d %b %Y")

    # group by 'Connected On'
    gdf = df.groupby("Connected On").agg(["count"])
    grouped_by_date = gdf["First Name"]

    # line chart
    fig = px.line(
        grouped_by_date, y="count", labels={"count": "Connection"}, template="none"
    )
    st.plotly_chart(fig, use_container_width=True)

    # chart explanation
    max_connection_in_day = grouped_by_date["count"].max()
    max_connection_day = (
        grouped_by_date["count"].idxmax().to_pydatetime().strftime("%d %b %Y")
    )
    average_connection = grouped_by_date["count"].mean()
    f"You were feeling sociable on **{max_connection_day}** with highest number of new\
    connections clocking in at **{max_connection_in_day}**.\
    On average, you made **{average_connection:.2f}** connections per day"

# 2 column charts
