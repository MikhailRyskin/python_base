# -*- coding: utf-8 -*-

# (if/elif/else)

# По номеру месяца вывести кол-во дней в нем (без указания названия месяца, в феврале 28 дней)
# Результат проверки вывести на консоль
# Если номер месяца некорректен - сообщить об этом

# Номер месяца получать от пользователя следующим образом
user_input = input('Введите, пожалуйста, номер месяца: ')
month = int(user_input)
# TODO Отлично, но куда проще использовать структуру данных, и оператор вхождения "in"
#  К примеру словарь.
#   calendar = {1: 'В Январе 31 день',
#             2: 'В Феврале 28 дней', ...
#
print('Вы ввели', month)
if month == 2:
    print('В этом месяце 28 дней')
elif month == 4 or month == 6 or month == 9 or month == 11:
    print('В этом месяце 30 дней')
elif month == 1 or month == 3 or month == 5 or month == 7 or month == 8 or month == 10 or month == 12:
    print('В этом месяце 31 день')
else:
    print('Такого месяца не существует')
