# -*- coding: utf-8 -*-

# Имеется файл events.txt вида:
#
# [2018-05-17 01:55:52.665804] NOK
# [2018-05-17 01:56:23.665804] OK
# [2018-05-17 01:56:55.665804] OK
# [2018-05-17 01:57:16.665804] NOK
# [2018-05-17 01:57:58.665804] OK
# ...
#
# Напишите программу, которая считывает файл
# и выводит число событий NOK за каждую минуту в другой файл в формате
#
# [2018-05-17 01:57] 1234
# [2018-05-17 01:58] 4321
# ...
#
# Входные параметры: файл для анализа, файл результата
#
# Требования к коду: он должен быть готовым к расширению функциональности - делать сразу на классах.
# Для этого пригодится шаблон проектирование "Шаблонный метод"
#   см https://refactoring.guru/ru/design-patterns/template-method
#   и https://gitlab.skillbox.ru/vadim_shandrinov/python_base_snippets/snippets/4

#
print('Как выводить события: 1 по минутам, 2 по часам, 3 по дням, 4 по месяцу, 5 по году.')
period = int(input('Введите период: '))
right_border = 17
if period == 2:
    right_border = 14
elif period == 3:
    right_border = 11
elif period == 4:
    right_border = 8
elif period == 5:
    right_border = 5

file_in = 'events.txt'
events_file = open(file_in, 'r', encoding='utf8')
file_out = 'out.txt'
events_quantity = open(file_out, 'w+', encoding='utf8')

first_line = True
not_changed = True
events_count = 0
prev_line = ''

for line in events_file:
    current_line = line[:right_border]
    if first_line:
        first_line = False
        prev_line = current_line
        if line[:-1].endswith('NOK'):
            events_count = 1
        else:
            events_count = 0
        continue
    if current_line == prev_line:
        if line[:-1].endswith('NOK'):
            events_count += 1
    else:
        not_changed = False
        content = f'{prev_line}] {events_count}\n'
        events_quantity.write(content)
        prev_line = current_line
        if line[:-1].endswith('NOK'):
            events_count = 1
        else:
            events_count = 0
if not_changed:
    content = f'{prev_line}] {events_count}\n'
    events_quantity.write(content)

events_file.close()
events_quantity.close()
#
print('Как выводить события: 1 по минутам, 2 по часам, 3 по месяцу, 4 по году.')
period = int(input('Введите период: '))
right_border = 17
if period == 2:
    right_border = 14
elif period == 3:
    right_border = 8
elif period == 4:
    right_border = 5

file_in = 'events.txt'
events_file = open(file_in, 'r', encoding='utf8')
file_out = 'out.txt'
events_quantity = open(file_out, 'w+', encoding='utf8')

first_line = True
not_changed = True
events_count = 0
prev_line = ''

for line in events_file:
    current_line = line[:right_border]
    if first_line:
        first_line = False
        prev_line = current_line
        if line[:-1].endswith('NOK'):
            events_count = 1
        else:
            events_count = 0
        continue
    if current_line == prev_line:
        if line[:-1].endswith('NOK'):
            events_count += 1
    else:
        not_changed = False
        content = f'{prev_line}] {events_count}\n'
        events_quantity.write(content)
        prev_line = current_line
        if line[:-1].endswith('NOK'):
            events_count = 1
        else:
            events_count = 0
if not_changed:
    content = f'{prev_line}] {events_count}\n'
    events_quantity.write(content)

events_file.close()
events_quantity.close()

# После зачета первого этапа нужно сделать группировку событий
#  - по часам
#  - по месяцу
#  - по году
