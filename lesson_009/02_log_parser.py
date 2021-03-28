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
class LogParser:
    # TODO Логики нужно упростить, хранить удобнее в словаре
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
        self.events_file = None
        self.events_quantity = None

    def _right_border_calc(self):
        if self.period == 2:
            self.right_border = 14
        elif self.period == 3:
            self.right_border = 11
        elif self.period == 4:
            self.right_border = 8
        elif self.period == 5:
            self.right_border = 5

    def open_files(self):
        self.events_file = open(self.file_in, 'r', encoding='utf8')
        self.events_quantity = open(self.file_out, 'w+', encoding='utf8')

    def parser_events(self):
        first_line = True
        not_changed = True
        events_count = 0
        prev_line = ''

        def _write_content():
            content = f'{prev_line}] {events_count}\n'
            self.events_quantity.write(content)

        def _count_init():
            if line[:-1].endswith('NOK'):
                count = 1
            else:
                count = 0
            return count

        self._right_border_calc()
        for line in self.events_file:
            current_line = line[:self.right_border]
            if first_line:
                first_line = False
                prev_line = current_line
                events_count = _count_init()
                continue
            if current_line == prev_line:
                if line[:-1].endswith('NOK'):
                    events_count += 1
            else:
                not_changed = False
                _write_content()
                prev_line = current_line
                events_count = _count_init()
        if not_changed:
            _write_content()

    def close_files(self):
        self.events_file.close()
        self.events_quantity.close()


file_in = 'events.txt'
file_out = 'out.txt'
print('Как выводить события: 1 по минутам, 2 по часам, 3 по дням, 4 по месяцу, 5 по году.')
user_choice = int(input('Введите период вывода событий: '))

parser = LogParser(file_in, file_out, user_choice)
parser.open_files()
parser.parser_events()
parser.close_files()

# После зачета первого этапа нужно сделать группировку событий
#  - по часам
#  - по месяцу
#  - по году
