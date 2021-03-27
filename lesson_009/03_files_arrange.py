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


input_dir = 'icons'
output_dir = 'icons_by_year'

abs_path = os.path.abspath(input_dir)
total_files = 0
for dirpath, dirnames, filenames in os.walk(abs_path):
    total_files += len(filenames)
    for file in filenames:
        full_file_path = os.path.join(dirpath, file)
        secs = os.path.getmtime(full_file_path)
        file_time = time.gmtime(secs)
        file_year = file_time[0]
        file_month = file_time[1]
        os.makedirs(name=f'{output_dir}/{file_year}/{file_month}', exist_ok=True)
        shutil.copy2(full_file_path, f'{output_dir}/{file_year}/{file_month}')

print('Абсолютный путь исходной папки', abs_path)
print('Всего файлов в исходной папке', total_files)
print()
total_files_new = 0
abs_path_new = os.path.abspath(output_dir)
print('Абсолютный путь созданной папки', abs_path_new)
for dirpath, dirnames, filenames in os.walk(abs_path_new):
    total_files_new += len(filenames)
print('Всего файлов в созданной папке', total_files)

# Усложненное задание (делать по желанию)
# Нужно обрабатывать zip-файл, содержащий фотографии, без предварительного извлечения файлов в папку.
# Это относится только к чтению файлов в архиве. В случае паттерна "Шаблонный метод" изменяется способ
# получения данных (читаем os.walk() или zip.namelist и т.д.)
# Документация по zipfile: API https://docs.python.org/3/library/zipfile.html
