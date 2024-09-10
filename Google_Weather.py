import requests
from bs4 import BeautifulSoup

class Google_Weather_Scrapper:
    """
    A class to scrape weather information for a given location from Google search results.

    # Attributes
    location_query : str
        The location for which the weather data is to be fetched.
    location : str
        The name of the location (e.g., city or region).
    time : str
        The time of the weather update.
    condition : str
        The weather condition (e.g., sunny, rainy, cloudy).
    temperature_celsius : str
        The temperature in Celsius.
    temperature_fahrenheit : str
        The temperature in Fahrenheit.
    precipitation : str
        The precipitation percentage.
    humidity : str
        The humidity percentage.
    wind_speed : str
        The wind speed.

    # Methods
    get_weather_data():
        Fetches and parses the weather data from Google using BeautifulSoup.
    """

    def __init__(self, location):
        """
        Initializes the Google_Weather_Scrapper class with a specified location and fetches weather data.

        # Parameters
        location : str
            The location for which the weather information needs to be retrieved.
        """
        self.location_query = location
        self.location = None
        self.time = None
        self.condition = None
        self.temperature_celsius = None
        self.temperature_fahrenheit = None
        self.precipitation = None
        self.humidity = None
        self.wind_speed = None

        self.get_weather_data()

    def get_weather_data(self):
        """
        Fetches the weather data from Google search results using a session.

        This method uses requests.Session to send a GET request to Google's search engine,
        and BeautifulSoup to parse the HTML response and extract the relevant weather information.

        After obtaining the response, the session cookies and data are cleared, and the session is closed.

        It updates the attributes (location, time, condition, temperature, precipitation, etc.)
        of the instance with the scraped data.

        If any information is not found or an error occurs, the corresponding attribute is set to None or an error message.
        """
        with requests.Session() as session:
            try:
                # Setting headers and making a GET request with a session
                response = session.get(f"https://www.google.com/search?q=weather+in+{self.location_query}", 
                                    headers={"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"},
                                    timeout=None)
                response.raise_for_status()

                soup = BeautifulSoup(response.text, "html.parser")

                location_info = soup.find('span', class_='BBwThe').text.strip()
                if location_info:
                    self.location = location_info

                time_info = soup.find(id="wob_dts")
                if time_info:
                    self.time = time_info.text

                condition_info = soup.find(id="wob_dc")
                if condition_info:
                    self.condition = condition_info.text

                temp_celsius_info = soup.find(id="wob_tm")
                if temp_celsius_info:
                    self.temperature_celsius = temp_celsius_info.text

                temp_fahrenheit_info = soup.find(id="wob_ttm")
                if temp_fahrenheit_info:
                    self.temperature_fahrenheit = temp_fahrenheit_info.text

                precipitation_info = soup.find(id="wob_pp")
                if precipitation_info:
                    self.precipitation = precipitation_info.text

                humidity_info = soup.find(id="wob_hm")
                if humidity_info:
                    self.humidity = humidity_info.text

                wind_speed_info = soup.find(id="wob_ws")
                if wind_speed_info:
                    self.wind_speed = wind_speed_info.text

            except AttributeError:self.location = "Please Check the enterd location and make sure you entered the correct location."
            except Exception as e:self.location = f"An error occurred: {e}"
            # Clearing all session cookies and data, and closing the session
            session.cookies.clear()

# Example usage
if __name__=="__main__":
    weather = Google_Weather_Scrapper("New York")
    # Access the weather data
    print(f"Location: {weather.location}")
    print(f"Time: {weather.time}")
    print(f"Condition: {weather.condition}")
    print(f"Temperature (Celsius): {weather.temperature_celsius}")
    print(f"Temperature (Fahrenheit): {weather.temperature_fahrenheit}")
    print(f"Precipitation: {weather.precipitation}")
    print(f"Humidity: {weather.humidity}")
    print(f"Wind Speed: {weather.wind_speed}")
