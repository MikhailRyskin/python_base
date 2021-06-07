# -*- coding: utf-8 -*-
# функция, которая принимает на вход text(текст входящего сообщения) и context (dict)б а возвращает bool:
# True если шаг пройден, False если данные введены неправильно
from schedule import SCHEDULE
from ticket_settings import RE_CITIES
import re

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
        return False


def handle_date(text, context):
    context['date'] = text
    dispatcher(context)
    return True


def dispatcher(context):
    context['flights'] = ['r1', 'r2', 't3', 't4', 'f5']


def handle_flights(text, context):
    choice = int(text)
    if 1 <= choice <= 5:
        context['flight'] = context['flights'][choice - 1]
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
        return False


def handle_phone(text, context):
    if text.isdigit():
        context['phone'] = text
        return True
    else:
        return False
