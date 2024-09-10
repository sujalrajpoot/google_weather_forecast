
# Project Title

This is a Python script that scrapes weather information from Google for a given location. It uses the requests and BeautifulSoup libraries to fetch and parse the HTML content from Google's search results.
## Authors

- [@sujalrajpoot](https://github.com/sujalrajpoot)


## Features

- Scrapes weather data from Google
- Extracts current weather condition, temperature, precipitation, humidity, wind speed, and more information URL
- Returns weather data in a greet sentence format

## Usage/Examples
To run the script, simply execute the Python file using your preferred Python interpreter. For example:

```python
python Google_Weather.py
```

This will prompt you to enter the location you want to check the weather for. For example:

```python
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

Output:
Location: New York, NY, USA
Time: Tuesday, 12:00 am
Condition: Cloudy
Temperature (Celsius): 21
Temperature (Fahrenheit): 69
Precipitation: 6%
Humidity: 54%
Wind Speed: 13 km/h
```


## License

[MIT](https://choosealicense.com/licenses/mit/)


## Installation


```bash
Clone the repository:
git clone https://github.com/sujalrajpoot/google_weather_forecast.git

cd google_weather_forecast

Install the required packages: 
pip install -r requirements.txt
```
    
## 🚀 About Me
I'm a skilled Python programmer and experienced web developer. With a strong background in programming and a passion for creating interactive and engaging web experiences, I specialize in crafting dynamic websites and applications. I'm dedicated to transforming ideas into functional and user-friendly digital solutions. Explore my portfolio to see my work in action.
# Hi, I'm Sujal Rajpoot! 👋


## 🔗 Links
[![portfolio](https://img.shields.io/badge/my_portfolio-000?style=for-the-badge&logo=ko-fi&logoColor=white)](https://sujalrajpoot.netlify.app/)
[![linkedin](https://img.shields.io/badge/linkedin-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/sujal-rajpoot-469888305/)
[![twitter](https://img.shields.io/badge/twitter-1DA1F2?style=for-the-badge&logo=twitter&logoColor=white)](https://twitter.com/sujalrajpoot70)

## Disclaimer
This Project only created for education purpose only respect the term and services of Google.
