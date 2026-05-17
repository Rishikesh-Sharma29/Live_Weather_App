# Live Weather App

A lightweight real-time weather application built using Python and Streamlit. The application allows users to search for weather information of any city and instantly view live weather conditions such as temperature, humidity, feels-like temperature, and weather status.

Based on the uploaded project report. fileciteturn0file0

---

# Features

* Real-time weather information retrieval
* Simple and responsive user interface
* Weather search by city name
* Displays:

  * Temperature
  * Feels-like temperature
  * Humidity
  * Weather condition
  * Country code
* API-based weather data fetching
* Error handling for invalid inputs and network issues
* Loading spinner during data retrieval
* Modular project structure

---

# Technologies Used

* Python
* Streamlit
* Requests Library
* OpenWeatherMap API

---

# Project Structure

```text
Live_Weather_App/
│
├── app.py
├── config.py
├── requirements.txt
├── README.md
│
├── services/
│   └── weather_services.py
│
├── components/
│   └── weather_display.py
│
├── utils/
│   └── helpers.py
│
├── screenshots/
├── assets/
├── report/
└── venv/
```

---

# Installation

## 1. Clone the Repository

```bash
git clone <repository-url>
cd Live_Weather_App
```

## 2. Create Virtual Environment

```bash
python -m venv venv
```

## 3. Activate Virtual Environment

### Windows

```bash
venv\Scripts\activate
```

### Linux / macOS

```bash
source venv/bin/activate
```

## 4. Install Dependencies

```bash
pip install -r requirements.txt
```

---

# API Setup

1. Create a free account on the OpenWeatherMap website.
2. Generate your API key.
3. Open `config.py`.
4. Add your API key:

```python
API_KEY = "your_api_key_here"
```

---

# Run the Application

Use the following command:

```bash
streamlit run app.py
```

After execution, the application will automatically open in your browser.

---

# How It Works

1. User enters a city name.
2. The application validates the input.
3. API request is sent to OpenWeatherMap.
4. Weather data is received in JSON format.
5. Required weather details are extracted.
6. Information is displayed on the dashboard.
7. Errors are handled if invalid input or network issues occur.

---

# Functional Requirements

* Accept city name input
* Retrieve real-time weather information
* Display weather details clearly
* Handle invalid city names
* Handle network and API errors
* Provide loading feedback to users

---

# Non-Functional Requirements

* Lightweight application
* Easy-to-use interface
* Fast response time
* Modular and maintainable code
* Cross-platform compatibility

---

# Advantages

* Simple and beginner-friendly
* Fast weather retrieval
* Easy to maintain and extend
* Uses real-time API communication
* Responsive dashboard layout

---

# Limitations

* Requires internet connection
* Depends on OpenWeatherMap API availability
* Current version supports only live weather information
* Free API plan may have request limits

---

# Future Enhancements

Possible future improvements include:

* Hourly and weekly weather forecasting
* Weather charts and graphs
* GPS-based location detection
* Mobile application support
* Dark mode and theme customization
* Air quality and UV index monitoring
* Weather history tracking
* Machine learning-based weather prediction

---

# Testing

The application was tested for:

* Valid city name input
* Invalid city names
* Empty input fields
* Network failures
* API response handling
* User interface responsiveness

All major functionalities worked successfully during testing.

---

# References

* Python Official Documentation
* Streamlit Documentation
* Requests Library Documentation
* OpenWeatherMap API Documentation
* GeeksforGeeks Python Resources
* W3Schools Python Tutorial

---

# Conclusion

The Live Weather App successfully demonstrates real-time weather retrieval using API communication and Python-based web application development. The project highlights concepts such as modular programming, JSON data handling, error management, and responsive user interface design using Streamlit.
