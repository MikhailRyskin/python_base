# -*- coding: utf-8 -*-

# Подсчитать статистику по буквам в романе Война и Мир.
# Входные параметры: файл для сканирования
# Статистику считать только для букв алфавита (см функцию .isalpha() для строк)
#
# Вывести на консоль упорядоченную статистику в виде
# +---------+----------+
# |  буква  | частота  |
# +---------+----------+
# |    А    |   77777  |
# |    Б    |   55555  |
# |   ...   |   .....  |
# |    a    |   33333  |
# |    б    |   11111  |
# |   ...   |   .....  |
# +---------+----------+
# |  итого  | 9999999  |
# +---------+----------+
#
# Упорядочивание по частоте - по убыванию. Ширину таблицы подберите по своему вкусу
#
# Требования к коду: он должен быть готовым к расширению функциональности - делать сразу на классах.
# Для этого пригодится шаблон проектирование "Шаблонный метод"
#   см https://refactoring.guru/ru/design-patterns/template-method
#   и https://gitlab.skillbox.ru/vadim_shandrinov/python_base_snippets/snippets/4

# здесь ваш код

class LettersStat:
    total_letters = 0

    def __init__(self, file_name, output_type):
        self.file_name = file_name
        self.output_type = output_type
        self.letters_stat = {}
        self.quantity_stat = {}

    def collect(self):
        file = open(self.file_name, 'r', encoding='cp1251')
        for line in file:
            for letter in line:
                if letter.isalpha():
                    if letter in self.letters_stat:
                        self.letters_stat[letter] += 1
                    else:
                        self.letters_stat[letter] = 1
        file.close()

    def _quantity_dict(self):
        for letter, quantity in self.letters_stat.items():
            if quantity in self.quantity_stat:
                self.quantity_stat[quantity].append(letter)
            else:
                self.quantity_stat[quantity] = [letter]

    def output_stat(self):
        print('_' * 19)
        print(f'| буква | частота |')
        print('-' * 19)
        revers = False
        if self.output_type == 1 or self.output_type == 4:
            revers = True
        if self.output_type == 1 or self.output_type == 2:
            self._quantity_dict()
            for quantity in sorted(self.quantity_stat.keys(), reverse=revers):
                for letter in self.quantity_stat[quantity]:
                    print(f'|{letter:^7}|{quantity:>8} |')
                    self.total_letters += quantity
        else:
            for letter in sorted(self.letters_stat.keys(), reverse=revers):
                print(f'|{letter:^7}|{self.letters_stat[letter]:>8} |')
                self.total_letters += self.letters_stat[letter]
        print('-' * 19)
        print(f'| всего  |{self.total_letters:^8}|')
        print('-' * 19)


our_file_name = 'voyna-i-mir.txt'
print('1 - по частоте  по убыванию, 2 - по частоте по возрастанию',
      '3 - по алфавиту по возрастанию, 4 - по алфавиту по убыванию.')
output_choice = int(input('Выберите тип вывода: '))

stat_file = LettersStat(file_name=our_file_name, output_type=output_choice)
stat_file.collect()
stat_file.output_stat()

# После зачета первого этапа нужно сделать упорядочивание статистики
#  - по частоте по возрастанию
#  - по алфавиту по возрастанию
#  - по алфавиту по убыванию
