import streamlit as st


def display_weather(response):

    temp = response["main"]["temp"]
    feels_like = response["main"]["feels_like"]
    humidity = response["main"]["humidity"]
    desc = response["weather"][0]["description"].title()
    country = response["sys"]["country"]
    name = response["name"]

    st.success(f"Weather found for **{name}, {country}**!")

    col1, col2, col3 = st.columns(3)

    col1.metric("Temperature", f"{temp} °C")
    col2.metric("Feels Like", f"{feels_like} °C")
    col3.metric("Humidity", f"{humidity} %")

    st.info(f"**Conditions:** {desc}")