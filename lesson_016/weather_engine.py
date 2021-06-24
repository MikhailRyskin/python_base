from pprint import pprint

import requests
import datetime
from bs4 import BeautifulSoup
import cv2

FORECAST_SITE = 'https://pogoda.mail.ru/prognoz/sankt_peterburg/june-2021/'
MONTHS = {'июня': 'june', 'июля': 'july'}
PICTURES = {'облачно': ['weather_img/cloud.jpg', (0, 0, 0)],
            'дождь': ['weather_img/rain.jpg', (255, 0, 0)],
            'дождь/гроза': ['weather_img/rain.jpg', (255, 0, 0)],
            'ясно': ['weather_img/sun.jpg', (0, 255, 255)],
            'снег': ['weather_img/snow.jpg', (255, 255, 0)]
            }

IMAGE_TEMPLATE = 'weather_img/probe.jpg'
FONT = cv2.FONT_HERSHEY_COMPLEX
FONT_SIZE = 0.8
TEXT_COLOR = (255, 0, 0)
DATE_POZ = (160, 230)
TEMPERATURE_POZ = (100, 120)
WEATHER_POZ = (200, 180)
# WEATHER_PICTURE_POZ = (180, 60)


class WeatherMaker:
    def __init__(self, date_range):
        self.date_range = date_range
        self.forecast_dict = {}

    def get_forecast(self):
        self.weather_parser()
        pass

    def weather_parser(self):
        response = requests.get(FORECAST_SITE)
        if response.status_code == 200:
            html_doc = BeautifulSoup(response.text, features='html.parser')
            list_of_days = html_doc.find_all('div', 'day__date')
            list_of_temperatures = html_doc.find_all('div', 'day__temperature')
            list_of_weather = html_doc.find_all('div', 'day__description')

            for d, t, w in zip(list_of_days, list_of_temperatures, list_of_weather):
                day = d.text.lower()
                day_datetime, day_rus = self.date_conversion(day)
                temperature = t.text.split()[0][:-1]
                weather = w.text.strip().lower()
                self.forecast_dict[day_datetime] = [day_rus, temperature, weather]
        pprint(self.forecast_dict)

    def date_conversion(self, day):
        if day.startswith('с'):
            day = day[8:]
        day_rus = day
        for month_rus in MONTHS.keys():
            if day.find(month_rus) != -1:
                day = day.replace(month_rus, MONTHS[month_rus])
                break
        day_datetime = datetime.datetime.strptime(day, '%d %B %Y')
        return day_datetime, day_rus


class ImageMaker:
    def __init__(self, date, temperature, weather):
        self.date = date
        self.temperature = temperature
        self.weather = weather

    def generate_image(self):
        day_weather_image = cv2.imread(IMAGE_TEMPLATE)

        self.make_gradient(day_weather_image)
        self.insert_text(day_weather_image)
        self.insert_picture(day_weather_image)

        # cv2.imshow('Result1', img3)
        # self.viewimage(day_weather_image, 'weather image')

        with open('weather_img.jpg', 'w'):
            cv2.imwrite('weather_img.jpg', day_weather_image)

    def insert_picture(self, day_weather_image):
        if self.weather in PICTURES:
            picture_path = PICTURES[self.weather][0]
        else:
            picture_path = PICTURES['облачно'][0]
        weather_picture = cv2.imread(picture_path)
        day_weather_image[50:150, 200:300, :] = weather_picture

    def insert_text(self, day_weather_image):
        coord_texts = [{'coord': DATE_POZ, 'text': self.date}, {'coord': TEMPERATURE_POZ, 'text': self.temperature},
                       {'coord': WEATHER_POZ, 'text': self.weather}]
        for info in coord_texts:
            cv2.putText(img=day_weather_image, text=info['text'], org=info['coord'], fontFace=FONT,
                        fontScale=FONT_SIZE, color=TEXT_COLOR, thickness=1)

    def make_gradient(self, day_weather_image):
        g, b, r = PICTURES[self.weather][1]
        for n in range(255):
            color = (g, b, r)
            day_weather_image[n:n + 1, :] = color
            if g < 255:
                g += 1
            if b < 255:
                b += 1
            if r < 255:
                r += 1

    def viewimage(self, image, name_of_window):
        cv2.namedWindow(name_of_window, cv2.WINDOW_NORMAL)
        cv2.imshow(name_of_window, image)
        cv2.waitKey(0)
        cv2.destroyAllWindows()


forecast = WeatherMaker(date_range='week')
forecast.get_forecast()

my_data = '28 июня 2021'
ddt, d2 = forecast.date_conversion(my_data)
list1 = forecast.forecast_dict[ddt]


im = ImageMaker(list1[0], list1[1], list1[2])
im.generate_image()
