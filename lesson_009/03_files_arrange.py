# -*- coding: utf-8 -*-

# Нужно написать скрипт для упорядочивания фотографий (вообще любых файлов)
# Скрипт должен разложить файлы из одной папки по годам и месяцам в другую.
# Например, так:
#   исходная папка
#       icons/cat.jpg
#       icons/man.jpg
#       icons/new_year_01.jpg
#   результирующая папка
#       icons_by_year/2018/05/cat.jpg
#       icons_by_year/2018/05/man.jpg
#       icons_by_year/2017/12/new_year_01.jpg
#
# Входные параметры основной функции: папка для сканирования, целевая папка.
# Имена файлов в процессе работы скрипта не менять, год и месяц взять из времени последней модификации файла
# (время создания файла берется по разному в разых ОС - см https://clck.ru/PBCAX - поэтому берем время модификации).
#
# Файлы для работы взять из архива icons.zip - раззиповать проводником ОС в папку icons перед написанием кода.
# Имя целевой папки - icons_by_year (тогда она не попадет в коммит, см .gitignore в папке ДЗ)
#
# Пригодятся функции:
#   os.walk
#   os.path.dirname
#   os.path.join
#   os.path.normpath
#   os.path.getmtime
#   time.gmtime
#   os.makedirs
#   shutil.copy2
#
# Чтение документации/гугла по функциям - приветствуется. Как и поиск альтернативных вариантов :)
#
# Требования к коду: он должен быть готовым к расширению функциональности - делать сразу на классах.
# Для этого пригодится шаблон проектирование "Шаблонный метод"
#   см https://refactoring.guru/ru/design-patterns/template-method
#   и https://gitlab.skillbox.ru/vadim_shandrinov/python_base_snippets/snippets/4

import os
import time
import shutil


class SortByDate:

    def __init__(self, input_dir, output_dir):
        self.input_dir = input_dir
        self.output_dir = output_dir

    def _output_dir_path(self, file):
        secs = os.path.getmtime(file)
        file_time = time.gmtime(secs)
        file_year = file_time[0]
        file_month = file_time[1]
        output_dir = f'{self.output_dir}/{file_year}/{file_month}'
        return output_dir

    def sort_by_date(self):
        abs_path = os.path.abspath(self.input_dir)
        for dirpath, dirnames, filenames in os.walk(abs_path):
            for file in filenames:
                full_file_path = os.path.join(dirpath, file)
                output_dir = self._output_dir_path(full_file_path)
                os.makedirs(name=output_dir, exist_ok=True)
                shutil.copy2(full_file_path, output_dir)

    def check_number_files(self, check_dir):
        abs_path = os.path.abspath(check_dir)
        total_files = 0
        for dirpath, dirnames, filenames in os.walk(abs_path):
            total_files += len(filenames)
        return total_files


my_input_dir = 'icons'
my_output_dir = 'icons_by_year'

my_sort = SortByDate(my_input_dir, my_output_dir)
my_sort.sort_by_date()

print('Абсолютный путь исходной папки', os.path.abspath(my_input_dir))
print('Всего файлов в исходной папке', my_sort.check_number_files(my_input_dir))
print('Абсолютный путь созданной папки', os.path.abspath(my_output_dir))
print('Всего файлов в созданной папке', my_sort.check_number_files(my_output_dir))

# Усложненное задание (делать по желанию)
# Нужно обрабатывать zip-файл, содержащий фотографии, без предварительного извлечения файлов в папку.
# Это относится только к чтению файлов в архиве. В случае паттерна "Шаблонный метод" изменяется способ
# получения данных (читаем os.walk() или zip.namelist и т.д.)
# Документация по zipfile: API https://docs.python.org/3/library/zipfile.html

# зачет!
