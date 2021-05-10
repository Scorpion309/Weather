import json

from loc import Location
from pydantic import BaseModel, validator

class Temperature(BaseModel):
    temp: int
    feels_like: float
    temp_min: int
    temp_max: int


class Weather(BaseModel):
    temperature: Temperature
    pressure: int
    description: str
    name: str


city = Location(25, 60)
weather_info = city.get_info()

weather = {
            'temperature': {
                            'temp': weather_info['main']['temp'],
                            'feels_like': weather_info['main']['feels_like'],
                            'temp_min': weather_info['main']['temp_min'],
                            'temp_max': weather_info['main']['temp_max']
                            },
            'pressure': weather_info['main']['pressure'],
            'description': weather_info['weather'][0]['description'],
            'name': weather_info['name']
        }

info = Weather.parse_raw(json.dumps(weather))
print(info)
