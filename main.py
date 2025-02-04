import os
import requests
import logging
import matplotlib.pyplot as plt
import seaborn as sns
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Retrieve API key and base URL from environment variables
API_KEY = os.getenv('API_KEY')
BASE_URL = os.getenv('BASE_URL')

# Set up logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def get_weather_data(lat, lon):
    """
    Fetch weather data from the OpenWeather API using the provided latitude and longitude.
    """
    url = f"{BASE_URL}?lat={lat}&lon={lon}&appid={API_KEY}&units=metric"
    logging.info(f"Fetching weather data for coordinates: ({lat}, {lon})")

    try:
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()

        if response.status_code == 200:
            logging.info(f"Successfully fetched data for coordinates: ({lat}, {lon})")
            return data
        else:
            logging.error(f"Error fetching data: {data['message']}")
            return None

    except requests.exceptions.RequestException as e:
        logging.error(f"Request failed: {e}")
        return None


def visualize_weather_data(data, lat, lon):
    """
    Visualize weather data using seaborn and matplotlib.
    """
    if not data:
        logging.error("No data to visualize.")
        return

    # Extract relevant weather parameters
    temperature = data['main']['temp']
    feels_like = data['main']['feels_like']
    humidity = data['main']['humidity']
    pressure = data['main']['pressure']
    wind_speed = data['wind']['speed']

    # Prepare data for visualization
    labels = ['Temperature (°C)', 'Feels Like (°C)', 'Humidity (%)', 'Pressure (hPa)', 'Wind Speed (m/s)']
    values = [temperature, feels_like, humidity, pressure, wind_speed]

    plt.figure(figsize=(10, 6))
    sns.barplot(x=labels, y=values, palette="Blues_d", edgecolor='black')

    # Customizing the plot to improve 
    plt.title(f"Weather Data for Latitude {lat}, Longitude {lon}", fontsize=16, fontweight='bold')
    plt.xlabel("Weather Parameters", fontsize=12)
    plt.ylabel("Values", fontsize=12)
    
    # Add gridlines for better readability
    plt.grid(True, axis='y', linestyle='--', alpha=0.7)

    # Add value labels on top of the bars
    for i, value in enumerate(values):
        plt.text(i, value + 0.5, f'{value:.1f}', ha='center', fontsize=12)

    # Display the plot
    plt.tight_layout()
    plt.show()


def main():
    """
    Main function to execute the program logic.
    """
    try:
        # Input latitude and longitude from the user
        lat = float(input("Enter the latitude (e.g., 35): "))
        lon = float(input("Enter the longitude (e.g., 139): "))
    except ValueError:
        logging.error("Invalid input. Please enter valid numeric values for latitude and longitude.")
        return

    # Fetch weather data
    weather_data = get_weather_data(lat, lon)

    # If data is fetched successfully, visualize it
    if weather_data:
        visualize_weather_data(weather_data, lat, lon)


if __name__ == "__main__":
    main()
