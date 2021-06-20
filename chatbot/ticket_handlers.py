# -*- coding: utf-8 -*-
# функция, которая принимает на вход text(текст входящего сообщения) и context (dict), а возвращает bool:
# True если шаг пройден, False если данные введены неправильно
import datetime
import re

from chatbot.generate_ticket import generate_ticket
from schedule import SCHEDULE
from intents import RE_CITIES


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
        cities = ''
        for city in SCHEDULE.keys():
            cities += city + '\n'
        context['cities_list'] = cities
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
            if dispatcher(input_date, context):
                return True
            else:
                return False
        else:
            return False
    else:
        return False


def dispatcher(date, context):
    all_flights_list = SCHEDULE[context['departure']][context['destination']]
    for index, flight in enumerate(all_flights_list):
        flight_date = datetime.datetime.strptime(flight[:10], '%d-%m-%Y')
        if flight_date >= date:
            date_index = index
            break
    else:
        return False
    flights_list = []
    number_of_flights = 0
    for flight in all_flights_list[date_index:]:
        flights_list.append(flight)
        number_of_flights += 1
        if number_of_flights == 5:
            break
    context['flights'] = flights_list
    flights5 = ''
    #  Может вывалится с ошибкой неверного индекса
    for number in range(number_of_flights):
        flight_output = str(number + 1) + '. ' + flights_list[number] + '\n'
        flights5 += flight_output
    context['flights5'] = flights5
    return True


def handle_flights(text, context):
    choice = int(text)
    if 1 <= choice <= len(context['flights']):
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
        context['break-scenario'] = True
        return False


def handle_phone(text, context):
    if text.isdigit():
        context['phone'] = text
        return True
    else:
        return False


def generate_ticket_handler(text, context):
    return generate_ticket(departure=context['departure'], destination=context['destination'],
                           flight=context['flight'], seats=context['seats'])
