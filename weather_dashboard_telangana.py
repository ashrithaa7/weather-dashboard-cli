
# weather_dashboard_telangana.py
import requests
from colorama import Fore, Style, init

init(autoreset=True)

API_KEY = "YOUR_REAL_API_KEY"
BASE_URL = "https://api.openweathermap.org/data/2.5/weather"

telangana_cities = [
    "Hyderabad", "Warangal", "Nizamabad", "Karimnagar",
    "Khammam", "Ramagundam", "Mahbubnagar", "Siddipet",
    "Nalgonda", "Adilabad"
]

def get_weather(city):
    params = {"q": city, "appid": API_KEY, "units": "metric"}
    response = requests.get(BASE_URL, params=params)
    if response.status_code == 200:
        data = response.json()
        temp = data['main']['temp']
        humidity = data['main']['humidity']
        desc = data['weather'][0]['description']

        if temp >= 30:
            temp_color = Fore.RED
        elif temp >= 20:
            temp_color = Fore.YELLOW
        else:
            temp_color = Fore.CYAN

        print(f"{Fore.GREEN}Weather in {city}:")
        print(f"Temperature: {temp_color}{temp}°C")
        print(f"Humidity: {Fore.BLUE}{humidity}%")
        print(f"Condition: {Fore.MAGENTA}{desc.capitalize()}\n")
    else:
        print(Fore.RED + "Error fetching data. Try again.\n")

def main():
    print(f"{Fore.CYAN}🌤️ Telangana Weather Dashboard CLI 🌤️\n")
    print("Available cities:", ", ".join(telangana_cities), "\n")
    
    while True:
        city = input("Enter city from Telangana (or type 'exit' to quit): ").strip().title()
        if city.lower() == 'exit':
            print("Goodbye! Stay weather-aware 🌦️")
            break
        elif city not in telangana_cities:
            print(Fore.RED + "City not in Telangana list. Choose from the available cities.\n")
        else:
            get_weather(city)

if __name__ == "__main__":
    main()
