# -*- coding: utf-8 -*-

# Умножить константу BRUCE_WILLIS на пятый элемент строки, введенный пользователем

BRUCE_WILLIS = 42
# BRUCE_WILLIS = None
# BRUCEWILLIS = 42

input_data = input('Если хочешь что-нибудь сделать, сделай это сам: ')
try:
    leeloo = int(input_data[4])
    result = BRUCE_WILLIS * leeloo
except ValueError:
    print(f'5-ый элемент "{input_data[4]}" невозможно преобразовать к числу')
except IndexError:
    print(f'Во введённых данных "{input_data}" нет 5-го элемента')
except Exception as exc:
    print('Неожиданная ошибка:', exc)
else:
    print(f'- Leeloo Dallas! Multi-pass № {result}!')

# Обернуть код и обработать исключительные ситуации для произвольных входных параметров
# - ValueError - невозможно преобразовать к числу
# - IndexError - выход за границы списка
# - остальные исключения
# для каждого типа исключений написать на консоль соотв. сообщение
