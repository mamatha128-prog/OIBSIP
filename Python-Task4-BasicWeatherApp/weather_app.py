import requests
import json

API_KEY = "YOUR_API_KEY"

print("===== Basic Weather App =====")

city = input("Enter city name: ").strip()

if city == "":
    print("Error: City name cannot be empty.")
    exit()

url = "https://api.openweathermap.org/data/2.5/weather"

params = {
    "q": city,
    "appid": API_KEY,
    "units": "metric"
}

try:
    response = requests.get(url, params=params, timeout=10)

    if response.status_code == 401:
        print("Error: Invalid API key.")

    elif response.status_code == 404:
        print("Error: City not found.")

    elif response.status_code == 200:
        data = response.json()

        temperature_c = data["main"]["temp"]
        temperature_f = (temperature_c * 9/5) + 32
        humidity = data["main"]["humidity"]
        weather = data["weather"][0]["description"]
        wind_speed = data["wind"]["speed"]

        print("\n===== Weather Information =====")
        print("City:", city)
        print(f"Temperature: {temperature_c:.1f} °C")
        print(f"Temperature: {temperature_f:.1f} °F")
        print("Humidity:", humidity, "%")
        print("Weather:", weather)
        print("Wind Speed:", wind_speed, "m/s")

    else:
        print("Error: Unable to get weather information.")

except requests.exceptions.Timeout:
    print("Error: Network request timed out.")

except requests.exceptions.ConnectionError:
    print("Error: Please check your internet connection.")

except requests.exceptions.RequestException as e:
    print("Error:", e)

except (KeyError, json.JSONDecodeError):
    print("Error: Unable to process weather data.")
