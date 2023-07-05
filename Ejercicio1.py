# -------------------------------- 
# Author: Custo Blanch, Christian 
# Project: Inceptia Job Application
# --------------------------------

# Import the requests library
import requests

# --------------------------------

# Define the GeoAPI class
class GeoAPI:

    # Define the class attributes
    API_KEY = "d81015613923e3e435231f2740d5610b"
    LAT = "-35.836948753554054"
    LON = "-61.870523905384076"
    url = f"https://api.openweathermap.org/data/2.5/weather?lat={LAT}&lon={LON}&appid={API_KEY}&units=metric"

    # Define the class methods
    @classmethod

    # Define the is_hot_in_pehuajo method
    def is_hot_in_pehuajo(cls):
        """ Sends a GET request to the OpenWeatherMap API to retrieve weather data for Pehuajó.
            Returns True if it's hot in Pehuajó, False otherwise.
            Returns False if the request was not successful."""

        # Send a GET request to the API
        response = requests.get(cls.url)

        # Check if the request was successful (status code 200)
        if response.status_code == 200:

            # Retrieve the JSON data
            weather_data = response.json()

            # Access the 'temp' field
            temperature = weather_data['main']['temp']

            # Print the temperature
            # print(f"The temperature in Pehuajó is {temperature}°C")

            # Check if the temperature is greater than 28 degrees
            if temperature > 28:
                return True # It's hot in Pehuajo
            else:
                return False # It's not hot in Pehuajo
        else:
            return False # The request was not successful

# --------------------------------

# Test
GeoAPI.is_hot_in_pehuajo()
