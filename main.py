from loc import Location
from pydantic import BaseModel, validator


class Description(BaseModel):
    description: str


class WeatherInfo(BaseModel):
    main: dict
    weather: list[Description]
    name: str


city = Location(25, 60)
weather_info = city.get_info()
info = WeatherInfo.parse_raw(weather_info)

# out_info = {"Weather": {"temperature": {"temp": info.main["temp"],
#                                         "feels_like": info.main["feels_like"],
#                                         "temp_min": info.main["temp_min"],
#                                         "temp_max": info.main["temp_max"]
#                                         },
#                         "pressure": info.main["pressure"],
#                         "description": info.weather[0]["description"],
#                         "name": info.name
#                         }
#             }

print(info)
