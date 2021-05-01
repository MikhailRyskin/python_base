# -*- coding: utf-8 -*-


# Заполнить все поля в билете на самолет.
# Создать функцию, принимающую параметры: ФИО, откуда, куда, дата вылета,
# и заполняющую ими шаблон билета Skillbox Airline.
# Шаблон взять в файле lesson_013/images/ticket_template.png
# Пример заполнения lesson_013/images/ticket_sample.png
# Подходящий шрифт искать на сайте ofont.ru
import os
from PIL import Image, ImageDraw, ImageFont, ImageColor
import argparse


def make_ticket(fio, from_, to, date, out_path=None):
    font_path = os.path.join('fonts', 'Arial_Cyr.ttf')
    template = 'ticket_template.png'
    im = Image.open(template)
    draw = ImageDraw.Draw(im)
    font = ImageFont.truetype(font_path, size=14)
    draw.text((45, 125), fio, font=font, fill=ImageColor.colormap['black'])
    draw.text((45, 195), from_, font=font, fill=ImageColor.colormap['black'])
    draw.text((45, 260), to, font=font, fill=ImageColor.colormap['black'])
    draw.text((285, 260), date, font=font, fill=ImageColor.colormap['black'])
    out_path = out_path if out_path else 'ticket.png'
    im.save(out_path)
    print(f'Билет сохранён как {out_path}')


# make_ticket('ИВАНОВ Т.П.', 'САНКТ-ПЕТЕРБУРГ', 'МОСКВА', '01.05')


# Усложненное задание (делать по желанию).
# Написать консольный скрипт c помощью встроенного python-модуля argparse.
# Скрипт должен принимать параметры:
#   --fio - обязательный, фамилия.
#   --from - обязательный, откуда летим.
#   --to - обязательный, куда летим.
#   --date - обязательный, когда летим.
#   --save_to - необязательный, путь для сохранения заполненнoго билета.
# и заполнять билет.

parser = argparse.ArgumentParser(description='Make ticket')
parser.add_argument('fio', type=str, help='FIO')
parser.add_argument('from_', type=str, help='FROM')
parser.add_argument('to', type=str, help='TO')
parser.add_argument('data', type=str, help='DATA')
parser.add_argument('--save_to', type=str, default='ticket.png', help='--save_to (default: ticket.png)')
args = parser.parse_args()
make_ticket(fio=args.fio, from_=args.from_, to=args.to, date=args.data, out_path=args.save_to)
