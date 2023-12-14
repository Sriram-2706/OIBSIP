import tkinter as tk
from tkinter import messagebox, ttk
import requests
import matplotlib.pyplot as plt
def get_weather():
    city = city_entry.get()
    api_key = "b4e21ebf51272167583840b3ca757a0c"  
    weather_url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
    forecast_url = f"https://api.openweathermap.org/data/2.5/forecast?q={city}&appid={api_key}&units=metric"

    try:
        # Fetch current weather data
        response = requests.get(weather_url)
        data = response.json()

        if response.status_code == 200:
            city_name = data["name"]
            weather_condition = data["weather"][0]["description"]
            temperature = data["main"]["temp"]
            humidity = data["main"]["humidity"]
            wind_speed = data["wind"]["speed"]

            current_weather_info = (
                f"Weather in {city_name}: {weather_condition}\n"
                f"Temperature: {temperature}°C\n"
                f"Humidity: {humidity}%\n"
                f"Wind Speed: {wind_speed} m/s"
            )
            current_weather_label.config(text=current_weather_info)

            # Fetch forecast data
            response = requests.get(forecast_url)
            forecast_data = response.json()

            if response.status_code == 200:
                dates = []
                temperatures = []
                humidities = []

                for item in forecast_data["list"]:
                    day = item["dt"]
                    date = day * 1000  # Converting to milliseconds for matplotlib
                    temperature = item["main"]["temp"]
                    humidity = item["main"]["humidity"]

                    dates.append(date)
                    temperatures.append(temperature)
                    humidities.append(humidity)

                # Update Graph
                plt.figure(figsize=(8, 5))
                plt.plot(dates, temperatures, label='Temperature (°C)', color='blue')
                plt.plot(dates, humidities, label='Humidity (%)', color='green')
                plt.xlabel('Date')
                plt.legend()
                plt.title('7-Day Forecast')
                plt.tight_layout()

                # Display the graph
                plt.show()

            else:
                messagebox.showerror("Error", "Failed to fetch forecast data!")
        else:
            messagebox.showerror("Error", "City not found!")

    except requests.exceptions.RequestException as e:
        messagebox.showerror("Error", "Network error. Please check your internet connection.")

root = tk.Tk()
root.title("Weather App")

# Tab creation
tab_control = ttk.Notebook(root)
current_weather_tab = ttk.Frame(tab_control)
hourly_forecast_tab = ttk.Frame(tab_control)

tab_control.add(current_weather_tab, text='Current Weather')
tab_control.add(hourly_forecast_tab, text='Hourly Forecast')
tab_control.pack(expand=1, fill='both')

# Current Weather Tab
city_frame = tk.Frame(current_weather_tab)
city_frame.pack(pady=20)

city_label = tk.Label(city_frame, text="Enter city:")
city_label.pack(side=tk.LEFT)

city_entry = tk.Entry(city_frame)
city_entry.pack(side=tk.LEFT)

get_weather_button = tk.Button(current_weather_tab, text="Get Weather", command=get_weather)
get_weather_button.pack()

current_weather_label = tk.Label(current_weather_tab, text="", justify="left")
current_weather_label.pack(pady=20)

# Hourly Forecast Tab
hourly_forecast_label = tk.Label(hourly_forecast_tab, text="Hourly Forecast Tab")
hourly_forecast_label.pack()

root.mainloop()
