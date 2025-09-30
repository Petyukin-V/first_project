import random


def weather_report():
    rain_probability = random.randint(0, 100)
    return f'Вероятность дождя: {rain_probability}'


if __name__ == '__main__':
    print(weather_report())