import tkinter as tk
from tkinter import messagebox
import requests

class WeatherApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Weather Forecast Application")
        self.root.geometry("400x400")

        self.api_key = "Hidden_Weather_API_Key"

        self.location_label = tk.Label(root, text="Enter Location:")
        self.location_label.pack(pady=10)

        self.location_entry = tk.Entry(root)
        self.location_entry.pack(pady=10)

        self.get_weather_button = tk.Button(root, text="Get Weather", command=self.get_weather)
        self.get_weather_button.pack(pady=10)

        self.output_label = tk.Label(root, text="")
        self.output_label.pack(pady=10)

    def get_weather(self):
        location = self.location_entry.get().strip()
        if not location:
            messagebox.showwarning("Input Error", "Please enter a location.")
            return
        
        url = f"http://api.openweathermap.org/data/2.5/weather?q={location}&appid={self.api_key}&units=metric"
        
        try:
            response = requests.get(url)
            data = response.json()
            if data["cod"] != 200:
                raise ValueError(data["message"])
            
            city = data["name"]
            temperature = data["main"]["temp"]
            humidity = data["main"]["humidity"]
            wind_speed = data["wind"]["speed"]

            weather_info = (f"Weather in {city}:\n"
                            f"Temperature: {temperature}°C\n"
                            f"Humidity: {humidity}%\n"
                            f"Wind Speed: {wind_speed} m/s")
            self.output_label.config(text=weather_info)
        
        except ValueError as exception:
            messagebox.showerror("Error", str(exception))
        except Exception as exception:
            messagebox.showerror("Error", "An error occurred while fetching the weather data.")

if __name__ == "__main__":
    root = tk.Tk()
    app = WeatherApp(root)
    root.mainloop()
