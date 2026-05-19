import streamlit as st
import requests

st.set_page_config(page_title="Live Weather App", page_icon="🌤️")
st.title("🌤️ Live Weather App")
st.write("Enter a city name to get the current weather conditions.")

city_name = st.text_input("City:", placeholder="e.g., London, Tokyo, New York")

if st.button("Get Weather", type="primary"):
    
    if city_name == "":
        st.warning("⚠️ Please enter a city name.")
    else:
        with st.spinner(f"Fetching weather for {city_name}..."):
            
            api_key = "27240ce85f73056fe84f0a2091b78fc7"  
            url = f"http://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={api_key}&units=metric"
            
            try:
                response = requests.get(url).json()
                
                if response.get("cod") != 200:
                    st.error(f"❌ Error: {response.get('message', 'City not found').title()}")
                else:
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

            except Exception as e:
                st.error("❌ A network error occurred. Please check your internet connection.")
        
