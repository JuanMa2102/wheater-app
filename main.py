import streamlit as st
import plotly.express as px
import pandas as pd

st.title("Wheater Forecast for the Next Days")
place = st.text_input("Place: ")
days = st.slider("Forecast days", min_value=1, max_value=5, help="Select the number of days for the forecast")
option = st.selectbox("Select data to view", ("Temperature", "Sky"))

st.subheader(f"{option} for the next {days} days in {place}")

def get_data(days):
    dates = ["2023-10-01", "2023-10-02", "2023-10-03", "2023-10-04", "2023-10-05"]
    temperatures = [20, 22, 21, 19, 18]
    temperatures = [ days * i for i in temperatures]
    return dates, temperatures

dates, temperatures = get_data(days)
figure = px.line(x = dates ,y = temperatures,labels={
    "x": "Date",
    "y": "Temperature (°C)",
})
st.plotly_chart(
    figure
)