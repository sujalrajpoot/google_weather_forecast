import requests
from bs4 import BeautifulSoup

def Google_Weather_Scrapper(location_query) -> str:
    """
    Get weather information for a specific location.

    Args:
    location_query (str): The location to get weather information for.

    Returns:
    str: A string containing the weather information.
    """
    try:
        url = f"https://www.google.com/search?q=weather+in+{location_query}"

        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
        }

        response = requests.get(url, headers=headers)
        response.raise_for_status()  # Raise an exception for bad status codes

        soup = BeautifulSoup(response.text, "html.parser")

        div = soup.find('div', class_='YfftMc')
        extracted_url = div.find('a', href=True)['href']

        location_info = soup.find(class_="VQF4g")

        if location_info:
            location = soup.find('span', class_='BBwThe').text.strip()
            time = location_info.find(id="wob_dts").text
            condition = location_info.find(id="wob_dc").text
            location_time_greet = f"You're looking at the weather for {location} as of {time}. "
        else:
            return "Location or time information not found."

        temperature_celsius = soup.find(id="wob_tm")
        temperature_fahrenheit = soup.find(id="wob_ttm")
        precipitation = soup.find(id="wob_pp")
        humidity = soup.find(id="wob_hm")
        wind_speed = soup.find(id="wob_ws")

        if temperature_celsius and temperature_fahrenheit and precipitation and humidity and wind_speed:
            weather_greet = (
                f"The current temperature is {temperature_celsius.text} Degrees Celsius, or {temperature_fahrenheit.text} Degrees Fahrenheit. "
                f"The weather is {condition}. The precipitation level is {precipitation.text}, "
                f"with a humidity of {humidity.text}. The wind is blowing at {wind_speed.text}.\n"
            )
        else:
            return "Weather information not fully found."

        return location_time_greet + weather_greet

    except requests.exceptions.RequestException as e:
        return f"An error occurred: {e}"
    except Exception as e:
        return f"An unexpected error occurred: {e}"

# Example usage
if __name__ == "__main__":
    location_query = "Delhi"
    weather_info = Google_Weather_Scrapper(location_query)
    print(weather_info)
