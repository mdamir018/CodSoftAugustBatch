from requests import get

def getWeather(apiKey,city):
     
     url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={apiKey}"
     response = get(url)
     data = response.json()

     if data["cod"] == 200:
          
          temperature = data["main"]["temp"]
          humidity = data["main"]["humidity"]
          windSpeed = data["wind"]["speed"]
          weatherInfo = data["weather"][0]["description"]
          
          print(f"Temperature: {temperature}°C")
          print(f"Humidity: {humidity}%")
          print(f"Wind speed: {windSpeed}m/s")
          print(f"Weather: {weatherInfo}")
     else:
          print("City not found")

apiKey = input("Enter your API key: ")
city = input("Enter city name : ")       
getWeather(apiKey,city)