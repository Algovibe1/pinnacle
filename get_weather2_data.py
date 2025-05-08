import requests
from datetime import datetime

def get_weather(city_name):
    # Use an environment variable for the API key
    API_Key = 'b24ec5a543b5e2bcdb530dd7c492a168'

    # Construct the API request URL
    url = f'https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={API_Key}&units=metric'

    # Send the GET request
    response = requests.get(url)
    # Check if the response was successful (HTTP status code 200)
    if response.status_code == 200:
        # Parse the JSON response into a Python dictionary
        data = response.json()

        print(f"\nWeather Report for {city_name.title()}:\n")
         # Extract and print weather description
        print('Weather:', data['weather'][0]['description'].title())
        # Extract and print current temperature in Celsius
        print('Temperature:', f"{data['main']['temp']}°C")
         # Extract and print "feels like" temperature in Celsius
        print('Feels Like:', f"{data['main']['feels_like']}°C")
         # Extract and print humidity percentage
        print('Humidity:', f"{data['main']['humidity']}%")
        #extract and print wind speed 
        print('Wind Speed:', f"{data['wind']['speed']} m/s")

        sunrise = datetime.fromtimestamp(data['sys']['sunrise']).strftime('%H:%M:%S')
        sunset = datetime.fromtimestamp(data['sys']['sunset']).strftime('%H:%M:%S')
        print('Sunrise:', sunrise)
        print('Sunset:', sunset)
    else:
        print(f"\nFailed to retrieve weather data for '{city_name}'.")
    # Print the HTTP error status code if the request failed
        print(f"Response code: {response.status_code}")
        try:
            print( response.json().get('message', 'No details provided'))
        except Exception:
            pass

# Ask the user for a city name kolkata
city = input("Enter city name: ")
get_weather(city)
