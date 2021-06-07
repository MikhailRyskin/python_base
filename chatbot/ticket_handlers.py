# -*- coding: utf-8 -*-
# функция, которая принимает на вход text(текст входящего сообщения) и context (dict)б а возвращает bool:
# True если шаг пройден, False если данные введены неправильно
from schedule import SCHEDULE
# import re

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


def handle_departure(text, context):
    if text in SCHEDULE:
        context['departure'] = text
        return True
    else:
        return False


def handle_destination(text, context):
    if text in SCHEDULE[context['departure']]:
        context['destination'] = text
        return True
    else:
        return False


def handle_phone(text, context):
    if text.isdigit():
        context['phone'] = text
        return True
    else:
        return False
