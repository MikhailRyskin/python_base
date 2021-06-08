# -*- coding: utf-8 -*-
# функция, которая принимает на вход text(текст входящего сообщения) и context (dict)б а возвращает bool:
# True если шаг пройден, False если данные введены неправильно
import datetime
import re
from schedule import SCHEDULE
from ticket_settings import RE_CITIES


# re_name = re.compile(r'^[\w\-\s]{3,40}$')
# re_email = re.compile(r'^\b[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+\b')
#
#
# def handle_name(text, context):
#     match = re.match(re_name, text)
#     if match:
#         context['name'] = text
#         return True
#     else:
#         return False
#
#
# def handle_email(text, context):
#     matches = re.findall(re_email, text)
#     if len(matches) > 0:
#         context['email'] = matches[0]
#         return True
#     else:
#         return False


def change_city_name(text):
    for re_city in RE_CITIES.keys():
        match = re.match(re_city, text)
        if match:
            full_city_name = RE_CITIES[re_city]
            return full_city_name
    else:
        return None


def handle_departure(text, context):
    context['break-scenario'] = False
    text = change_city_name(text)
    if text in SCHEDULE:
        context['departure'] = text
        return True
    else:
        context['cities_list'] = list(SCHEDULE.keys())
        return False


def handle_destination(text, context):
    text = change_city_name(text)
    if text in SCHEDULE[context['departure']]:
        context['destination'] = text
        return True
    else:
        context['break-scenario'] = True
        return False


def handle_date(text, context):
    re_date = re.compile(r'^(0[1-9]|[12][0-9]|3[01])[-](0[1-9]|1[012])[-](19|20)\d\d$')
    match = re.match(re_date, text)
    if match:
        today_date = datetime.date.today()
        temp = datetime.time(hour=00, minute=00, second=00)
        today = datetime.datetime.combine(today_date, temp)
        input_date = datetime.datetime.strptime(text, '%d-%m-%Y')
        if input_date >= today:
            dispatcher(text, context)
            return True
        else:
            return False
    else:
        return False


def dispatcher(date, context):
    all_flights_list = SCHEDULE[context['departure']][context['destination']]
    for index, flight in enumerate(all_flights_list):
        if flight[:10] >= date:
            date_index = index
            break
    flights_list = []
    for flight in all_flights_list[date_index: date_index + 5]:
        flights_list.append(flight)
    flights5 = []
    for number in range(5):
        flight_output = str(number + 1) + '. ' + flights_list[number]
        flights5.append(flight_output)
    context['flights'] = flights5


def handle_flights(text, context):
    choice = int(text)
    if 1 <= choice <= 5:
        context['flight'] = context['flights'][choice - 1][3:]
        return True
    else:
        return False


def handle_seats(text, context):
    number_seats = int(text)
    if 1 <= number_seats <= 5:
        context['seats'] = number_seats
        return True
    else:
        return False


def handle_comment(text, context):
    context['comment'] = text
    return True


def handle_confirm(text, context):
    if text == 'да':
        return True
    else:
        context['break-scenario'] = True
        return False


def handle_phone(text, context):
    if text.isdigit():
        context['phone'] = text
        return True
    else:
        return False
