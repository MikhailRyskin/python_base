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

    # def __init__(self, file_name):
    #     # Читать сразу весь файл в память не лучшая идея, лучше использовать цикл for для создания маленько буфера
    #     #  Чтение всего фала в память влечет за собой накладные расходы,
    #     #  а вы можете не знать сколько есть свободной памяти там где запускается скрипт
    #     in_file = open(file_name, 'r', encoding='utf8')
    #     self.file = in_file.readlines()
    #     in_file.close()
    #     self.i = 0
    #
    # def __iter__(self):
    #     # Открывать файл стоит здесь
    #     self.i = 0
    #     return self
    #
    # def __next__(self):
    #     #  а здесь уже основной цикл по поиску "NOK" строк
    #     events_count = 0
    #     while self.i < len(self.file):
    #         line = self.file[self.i].rstrip()
    #         current_line = line[1:17]
    #         if line.endswith('NOK'):
    #             events_count += 1
    #         self.i += 1
    #         if self.i == len(self.file):
    #             if events_count:
    #                 return current_line, events_count
    #         else:
    #             next_line = self.file[self.i][1:17]
    #             if next_line != current_line:
    #                 if events_count:
    #                     return current_line, events_count
    #     raise StopIteration

    def __init__(self, file_name):
        self.file_name = file_name
        self.file = None

    def __iter__(self):
        self.file = open(self.file_name, 'r', encoding='utf8')
        return self

    def __next__(self):
        events_count = 0
        for line in self.file:
            line = line.rstrip()
            current_line = line[1:17]
            if line.endswith('NOK'):
                events_count += 1
# TODO мне непонятно, как идя по циклу for line in self.file анализировать следующую строку.
# Сейчас всё работает неверно, т.к. readline() двигает текущую позицию указателя в конец следующей строки.
# Как можно посмотреть след. строку, но в цикле проходить все строки без пропусков?

            # file_position = self.file.tell()
            next_line = self.file.readline().rstrip()
            # self.file.seek(file_position, 0)
            if next_line:
                next_line = next_line[1:17]
                if next_line != current_line:
                    if events_count:
                        return current_line, events_count
            else:
                if events_count:
                    return current_line, events_count
        self.file.close()
        raise StopIteration


my_file_name = 'events.txt'

grouped_events = LogParser(my_file_name)
for group_time, event_count in grouped_events:
    print(f'[{group_time}] {event_count}')