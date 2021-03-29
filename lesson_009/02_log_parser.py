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

from collections import defaultdict


class LogParser:
    #  Логики нужно упростить, хранить удобнее в словаре
    #  defaultdict поможет упростить добавление в словарь.
    #  .
    #  В Первом методе наполняйте словарь ключами\значениями
    #  Добавлять удобнее сразу ключ с датой\временем 2018-05-14 19:37
    #  примерно такой срез думаю подойдет [1:-15]
    #  Во втором пишите в файл распаковывая словарь.
    #  Открытие\закрытие файла предоставьте - with

    def __init__(self, file_name, output_file, period):
        self.file_in = file_name
        self.file_out = output_file
        self.period = period
        self.right_border = 17
        self.nok_events = defaultdict(int)

    def _right_border_calc(self):
        if self.period == 2:
            self.right_border = 14
        elif self.period == 3:
            self.right_border = 11
        elif self.period == 4:
            self.right_border = 8
        elif self.period == 5:
            self.right_border = 5

    def collect_content(self):
        self._right_border_calc()
        with open(self.file_in, 'r', encoding='utf8') as file:
            for line in file:
                current_line = line[1:self.right_border]
                # Собираем только "NOK" остальные строки не нужны
                # TODO исправил, но вообще-то в задании - число событий NOK за каждую!!! минуту,
                # т.е. если 0 событий, тоже вроде нужно выводить.
                if line[:-1].endswith('NOK'):
                    self.nok_events[current_line] += 1
                # else:
                #     self.nok_events[current_line] += 0

    def write_content(self):
        with open(self.file_out, 'w+', encoding='utf8') as out_file:
            for date, quantity in self.nok_events.items():
                content_line = f'[{date}]  {quantity}\n'
                out_file.write(content_line)


file_in = 'events.txt'
file_out = 'out.txt'
print('Как выводить события: 1 по минутам, 2 по часам, 3 по дням, 4 по месяцу, 5 по году.')
user_choice = int(input('Введите период вывода событий: '))

parser = LogParser(file_in, file_out, user_choice)
parser.collect_content()
parser.write_content()


# После зачета первого этапа нужно сделать группировку событий
#  - по часам
#  - по месяцу
#  - по году
