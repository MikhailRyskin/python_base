# -*- coding: utf-8 -*-

# Есть файл с протоколом регистраций пользователей на сайте - registrations.txt
# Каждая строка содержит: ИМЯ ЕМЕЙЛ ВОЗРАСТ, разделенные пробелами
# Например:
# Василий test@test.ru 27
#
# Надо проверить данные из файла, для каждой строки:
# - присутсвуют все три поля
# - поле имени содержит только буквы
# - поле емейл содержит @ и .
# - поле возраст является числом от 10 до 99
#
# В результате проверки нужно сформировать два файла
# - registrations_good.log для правильных данных, записывать строки как есть
# - registrations_bad.log для ошибочных, записывать строку и вид ошибки.
#
# Для валидации строки данных написать метод, который может выкидывать исключения:
# - НЕ присутсвуют все три поля: ValueError
# - поле имени содержит НЕ только буквы: NotNameError (кастомное исключение)
# - поле емейл НЕ содержит @ и .(точку): NotEmailError (кастомное исключение)
# - поле возраст НЕ является числом от 10 до 99: ValueError
# Вызов метода обернуть в try-except.

#  Добавьте метод __str__ в классы

class NotNameError(Exception):
    def __str__(self):
        return 'поле имени содержит НЕ только буквы'


class NotEmailError(Exception):
    def __str__(self):
        return 'поле емейл НЕ содержит @ и .(точку)'


def data_validation(data_line):
    name, email, age = data_line.split(' ')
    age = int(age)
    if age < 10 or age > 99:
        raise ValueError('100')
    elif not name.isalpha():
        raise NotNameError([])
    elif not ('@' in email and '.' in email):
        raise NotEmailError([])
    else:
        return True


with open('registrations.txt', 'r', encoding='utf8') as reg_file,\
        open('registrations_good.log', 'w+', encoding='utf8') as good_file,\
        open('registrations_bad.log', 'w+', encoding='utf8') as bad_file:
    for line in reg_file:
        line = line[:-1]
        try:
            if data_validation(line):
                good_file.write(line + '\n')
        # Исключения лучше перечислять в блоке "except"
        except (ValueError, NotNameError, NotEmailError) as exc:
            if 'unpack' in exc.args[0]:
                message = 'НЕ присутствуют все три поля'
            elif '100' in exc.args[0]:
                message = 'поле возраст НЕ является числом от 10 до 99'
            else:
                message = str(exc)
            except_content = f'в записи {line} {message}\n'
            bad_file.write(except_content)

# зачет!
