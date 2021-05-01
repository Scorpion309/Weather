import requests


class Location:

    def __init__(self, longitude, latitude):
        self.longitude = longitude
        self.latitude = latitude

    def get_info(self):
        url = f"https://fcc-weather-api.glitch.me/api/current?lat={self.latitude}&lon={self.longitude}"
        weather_info = requests.get(url).text
        return weather_info
