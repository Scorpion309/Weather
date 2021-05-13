from pydantic import BaseModel, validator

from loc import Location


class Temperature(BaseModel):
    temp: int
    feels_like: float
    temp_min: int
    temp_max: int

    @validator('temp')
    def to_fahrenheit(cls, v):
        return int(v * 1.8 + 32)


class Weather(BaseModel):
    temperature: Temperature
    pressure: int
    description: str
    name: str


def main():
    city = Location(25, 60)
    weather_info = city.get_info()
    try:
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
        info = Weather(**weather)
        print(info)
    except KeyError:
        print('Error! Some value is empty!')


if __name__ == '__main__':
    main()
