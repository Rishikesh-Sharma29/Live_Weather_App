import streamlit as st
from services.weather_services import get_weather_data
from components.weather_display import display_weather
from utils.helpers import validate_city

st.set_page_config(page_title="Live Weather App", page_icon="🌤️")

st.title("🌤️ Live Weather App")
st.write("Enter a city name to get the current weather conditions.")

city_name = st.text_input(
    "City:",
    placeholder="e.g., London, Tokyo, New York"
)

if st.button("Get Weather", type="primary"):

    if not validate_city(city_name):
        st.warning("⚠️ Please enter a city name.")

    else:
        with st.spinner(f"Fetching weather for {city_name}..."):

            response = get_weather_data(city_name)

            if response.get("cod") != 200:
                st.error(
                    f"❌ Error: {response.get('message', 'City not found').title()}"
                )

            else:
                display_weather(response)