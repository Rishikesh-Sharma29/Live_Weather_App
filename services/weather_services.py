import requests
from config import API_KEY, BASE_URL


def get_weather_data(city_name):

    url = (
        f"{BASE_URL}?q={city_name}"
        f"&appid={API_KEY}&units=metric"
    )

    try:
        response = requests.get(url)
        return response.json()

    except Exception:
        return {
            "cod": 500,
            "message": "Network Error"
        }