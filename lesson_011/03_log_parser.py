# -*- coding: utf-8 -*-

# На основе своего кода из lesson_009/02_log_parser.py напишите итератор (или генератор)
# который читает исходный файл events.txt и выдает число событий NOK за каждую минуту
# <время> <число повторений>
#
# пример использования:
#
# grouped_events = <создание итератора/генератора>  # Итератор или генератор? выбирайте что вам более понятно
# for group_time, event_count in grouped_events:
#     print(f'[{group_time}] {event_count}')
#
# на консоли должно появится что-то вроде
#
# [2018-05-17 01:57] 1234


class LogParser:

    def __init__(self, file_name):
        # TODO Читать сразу весь файл в память не лучшая идея, лучше использовать цикл for для создания маленько буфера
        #  Чтение всего фала в память влечет за собой накладные расходы,
        #  а вы можете не знать сколько есть свободной памяти там где запускается скрипт
        in_file = open(file_name, 'r', encoding='utf8')
        self.file = in_file.readlines()
        in_file.close()
        self.i = 0

    def __iter__(self):
        # TODO Открывать файл стоит здесь
        self.i = 0
        return self

    def __next__(self):
        # TODO а здесь уже основной цикл по поиску "NOK" строк
        events_count = 0
        while self.i < len(self.file):
            line = self.file[self.i].rstrip()
            current_line = line[1:17]
            if line.endswith('NOK'):
                events_count += 1
            self.i += 1
            if self.i == len(self.file):
                if events_count:
                    return current_line, events_count
            else:
                next_line = self.file[self.i][1:17]
                if next_line != current_line:
                    if events_count:
                        return current_line, events_count
        raise StopIteration


my_file_name = 'events.txt'

grouped_events = LogParser(my_file_name)
for group_time, event_count in grouped_events:
    print(f'[{group_time}] {event_count}')
