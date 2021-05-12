from pydantic import BaseModel, validator
from loc import Location


class Temperature(BaseModel):
    temp: int
    feels_like: float
    temp_min: int
    temp_max: int
    @validator('temp')
    def to_celsius(cls, v):
        return int(v*1.8+32)


class Weather(BaseModel):
    temperature: Temperature
    pressure: int
    description: str
    name: str


def main(response):
    return{
                'temperature': {
                                'temp': response['main']['temp'],
                                'feels_like': response['main']['feels_like'],
                                'temp_min': response['main']['temp_min'],
                                'temp_max': response['main']['temp_max']
                            },
                'pressure': response['main']['pressure'],
                'description': response['weather'][0]['description'],
                'name': response['name']
            }


if __name__ == '__main__':
    city = Location(25, 60)
    weather_info = city.get_info()
    try:
        weather = main(weather_info)
        info = Weather(**weather)
        print(info)
    except:
        print('Ошибка получения и обработки данных!!!')
