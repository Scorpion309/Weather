import requests

class Location(object):

    def __init__(self, longitude, latitude):
        self.longitude = longitude
        self.latitude = latitude

    def GetInfo(self):
        url = f"https://fcc-weather-api.glitch.me/api/current?lat={self.latitude}&lon={self.longitude}"
        json = requests.get(url).text
        return json

