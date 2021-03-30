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

from random import randint

ENLIGHTENMENT_CARMA_LEVEL = 777


class IamGodError(Exception):
    pass


class DrunkError(Exception):
    pass


class CarCrashError(Exception):
    pass


class GluttonyError(Exception):
    pass


class DepressionError(Exception):
    pass


class SuicideError(Exception):
    pass


def one_day():
    dice = randint(1, 13)
    if dice == 13:
        dice = randint(1, 6)
        if dice == 1:
            raise IamGodError
        elif dice == 2:
            raise DrunkError
        elif dice == 3:
            raise CarCrashError
        elif dice == 4:
            raise GluttonyError
        elif dice == 5:
            raise DepressionError
        elif dice == 6:
            raise SuicideError
    else:
        carma = randint(1, 7)
        return carma


total_carma = 0
day = 1

with open('log_file.txt', 'w+', encoding='utf8') as log_file:
    while total_carma < ENLIGHTENMENT_CARMA_LEVEL:
        try:
            total_carma += one_day()
        except IamGodError:
            log_file.write(f'день {day:>4} I am God\n')
        except DrunkError:
            log_file.write(f'день {day:>4} Drunk\n')
        except CarCrashError:
            log_file.write(f'день {day:>4} Car Crash\n')
        except GluttonyError:
            log_file.write(f'день {day:>4} Gluttony\n')
        except DepressionError:
            log_file.write(f'день {day:>4} Depression\n')
        except SuicideError:
            log_file.write(f'день {day:>4} Suicide\n')

        day += 1

print(f'день {day}, карма {total_carma}!!!')

# https://goo.gl/JnsDqu
