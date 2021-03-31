# -*- coding: utf-8 -*-

# День сурка
#
# Напишите функцию one_day() которая возвращает количество кармы от 1 до 7
# и может выкидывать исключения:
# - IamGodError
# - DrunkError
# - CarCrashError
# - GluttonyError
# - DepressionError
# - SuicideError
# Одно из этих исключений выбрасывается с вероятностью 1 к 13 каждый день
#
# Функцию оберните в бесконечный цикл, выход из которого возможен только при накоплении
# кармы до уровня ENLIGHTENMENT_CARMA_LEVEL. Исключения обработать и записать в лог.
# При создании собственных исключений максимально использовать функциональность
# базовых встроенных исключений.

from random import randint, choice

ENLIGHTENMENT_CARMA_LEVEL = 777

# Добавьте метод __str__ в классы


class IamGodError(Exception):
    def __str__(self):
        return 'I am God'


class DrunkError(Exception):
    def __str__(self):
        return 'Drunk'


class CarCrashError(Exception):
    def __str__(self):
        return 'Car Crash'


class GluttonyError(Exception):
    def __str__(self):
        return 'Gluttony'


class DepressionError(Exception):
    def __str__(self):
        return 'Depression'


class SuicideError(Exception):
    def __str__(self):
        return 'Suicide'


def one_day():
    dice = randint(1, 13)
    # Создайте здесь список исключений, и когда на кубике выпадает 13 - выбрасывайте одно из них.
    #  За место условий отлично подойдет random.choice
    groundhog_exceptions = [IamGodError, DrunkError, CarCrashError,
                            GluttonyError, DepressionError, SuicideError]
    if dice == 13:
        raise choice(groundhog_exceptions)
    else:
        carma = randint(1, 7)
        return carma


total_carma = 0
day = 1

with open('log_file.txt', 'w+', encoding='utf8') as log_file:
    while total_carma < ENLIGHTENMENT_CARMA_LEVEL:
        try:
            total_carma += one_day()
        # Исключения лучше перечислять в блоке "except",
        #  чтобы выводить\записывать различные сообщения дополните классы методом __str__
        except (IamGodError, DrunkError, CarCrashError,
                GluttonyError, DepressionError, SuicideError) as exc:
            except_content = f'день {day:>4} {str(exc)}\n'
            log_file.write(except_content)

        day += 1

print(f'день {day}, карма {total_carma}!!!')

# https://goo.gl/JnsDqu
